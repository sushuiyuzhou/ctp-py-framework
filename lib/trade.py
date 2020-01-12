import lib.redis_cli as rc
import lib.ctp_structs as structs
import config as cfg

from lib.logger import get_logger


class TradeStatus(object):
    PENDING = 'pending'
    DONE = 'done'


class Order(object):
    OrderRef = None,

    OrderPriceType = None,

    Instrument = None,
    Direction = None,

    CombOffsetFlag = None,
    CombHedgeFlag = None,

    LimitPrice = None,

    VolumeTotalOriginal = None,
    MinVolume = None,

    TimeCondition = None,
    VolumeCondition = None,
    ContingentCondition = None,

    StopPrice = None,

    ForceCloseReason = None,
    UserForceClose = None,

    IsAutoSuspend = None,

    # for cancel
    FrontID = None,
    SessionID = None,

    # for monitoring status
    OrderStatus = None,
    OrderSubmitStatus = None,
    StatusMsg = None,

    #
    TradeStatus = TradeStatus.PENDING


def _ascii_to_order_status(code):
    if code == 48:
        return structs.OrderStatus.THOST_FTDC_OST_AllTraded
    elif code == 49:
        return structs.OrderStatus.THOST_FTDC_OST_PartTradedQueueing
    elif code == 50:
        return structs.OrderStatus.THOST_FTDC_OST_PartTradedNotQueueing
    elif code == 51:
        return structs.OrderStatus.THOST_FTDC_OST_NoTradeQueueing
    elif code == 52:
        return structs.OrderStatus.THOST_FTDC_OST_NoTradeNotQueueing
    elif code == 53:
        return structs.OrderStatus.THOST_FTDC_OST_Canceled
    elif code == 97:
        return structs.OrderStatus.THOST_FTDC_OST_Unknown
    elif code == 98:
        return structs.OrderStatus.THOST_FTDC_OST_NotTouched
    elif code == 99:
        return structs.OrderStatus.THOST_FTDC_OST_Touched


def _ascii_to_order_submit_status(code):
    if code == 48:
        return structs.OrderSubmitStatus.THOST_FTDC_OSS_InsertSubmitted
    elif code == 49:
        return structs.OrderSubmitStatus.THOST_FTDC_OSS_CancelSubmitted
    elif code == 50:
        return structs.OrderSubmitStatus.THOST_FTDC_OSS_ModifySubmitted
    elif code == 51:
        return structs.OrderSubmitStatus.THOST_FTDC_OSS_Accepted
    elif code == 52:
        return structs.OrderSubmitStatus.THOST_FTDC_OSS_InsertRejected
    elif code == 53:
        return structs.OrderSubmitStatus.THOST_FTDC_OSS_CancelRejected
    elif code == 54:
        return structs.OrderSubmitStatus.THOST_FTDC_OSS_ModifyRejected


class Trade(object):
    MODEL_PATH = 'ModelPath'
    REQ_METHOD = '.Req.Method'
    REQ_CONTENT = '.Req.Content'
    REQ_SIGNAL = '.SendRequest'

    def __init__(self,
                 name='[trade]'):
        self.name = name
        self.cfg = cfg.Config()
        self.logger = get_logger('trade')

        # redis client handle
        self.c = rc.RedisClient(name='trade',
                                host=cfg.RedisConfig.Host,
                                port=cfg.RedisConfig.PortTrade)
        # redis utils handle
        self.r = self.c.r

        # initialize pubsub handle
        self.p = self.c.ps()

        # response queue
        self.q = None

        # order registry
        self.orders = {}

        # order index wheel
        self.index = 0

    def query_model_path(self):
        return rc.decode(self.r.get(self.MODEL_PATH))

    def subscribe_to_trade_topics(self):
        extract_topics = lambda clz: [attr for attr in dir(clz) if
                                      not callable(getattr(clz,
                                                           attr)) and not attr.startswith(
                                          '__')]

        topics = extract_topics(structs.RspTopics) \
                 + extract_topics(structs.RtnTopics) \
                 + extract_topics(structs.ErrRtnTopics)

        mp = self.query_model_path()
        for t in topics:
            self.c.subscribe_to_topic(mp + "." + t)

    def submit_trade_action(self, method, content):
        '''
        portal to trigger ctp trade API method
        :param method:
        :param content:
        :return:
        '''
        mp = self.query_model_path()
        self.r.set(mp + self.REQ_METHOD, method)
        self.r.delete(mp + self.REQ_CONTENT)
        self.r.hmset(mp + self.REQ_CONTENT, content)
        self.r.publish(mp + self.REQ_SIGNAL, 'OK')

    def authenticate(self, BrokerID, UserID, AppID, AuthCode):
        self.submit_trade_action('ReqAuthenticate', {'BrokerID': BrokerID,
                                                     'UserID': UserID,
                                                     'AppID': AppID,
                                                     'AuthCode': AuthCode})

    def login(self, BrokerID, UserID, Password):
        self.submit_trade_action('ReqUserLogin',
                                 {'BrokerID': BrokerID,
                                  'UserID': UserID,
                                  'Password': Password})

    def add_order_rtn_handler(self):
        self.c.add_ps_handler(self._order_rtn_handler)

    def _order_rtn_handler(self, topic, key):
        mp = self.query_model_path()

        if topic == mp + '.' + structs.RtnTopics.OnRtnOrder:
            ctn = rc.decode(self.r.hgetall(key))
            self.logger.info("OnRtnOrder: %s", ctn)

            orderRef = ctn['OrderRef']
            frontID = ctn['FrontID']
            sessionID = ctn['SessionID']

            orderStatus = int(ctn['OrderStatus'])
            orderSubmitStatus = int(ctn['OrderSubmitStatus'])

            t_order = self.orders[int(orderRef)]

            t_order.FrontID = frontID
            t_order.SessionID = sessionID

            t_order.OrderStatus = _ascii_to_order_status(orderStatus)
            t_order.OrderSubmitStatus = _ascii_to_order_submit_status(
                orderSubmitStatus)
            t_order.StatusMsg = ctn['StatusMsg']

        if topic == mp + '.' + structs.RtnTopics.OnRtnTrade:
            ctn = rc.decode(self.r.hgetall(key))
            self.logger.info("OnRtnTrade: %s", ctn)

            orderRef = ctn['OrderRef']
            self.orders[int(orderRef)].TradeStatus = TradeStatus.DONE

    # order utils
    def submit_order(self, order):
        self.submit_trade_action('ReqOrderInsert',
                                 {'BrokerID':
                                      self.cfg.BrokerID,
                                  'InvestorID':
                                      self.cfg.UserID,
                                  'UserID':
                                      self.cfg.UserID,
                                  'ExchangeID': 'SHFE',
                                  'OrderRef': order.OrderRef,
                                  'InstrumentID': order.Instrument,
                                  'Direction': order.Direction,
                                  'CombOffsetFlag': order.CombOffsetFlag,
                                  'CombHedgeFlag': order.CombHedgeFlag,
                                  'VolumeTotalOriginal': order.VolumeTotalOriginal,
                                  'VolumeCondition': order.VolumeCondition,
                                  'MinVolume': order.MinVolume,
                                  'LimitPrice': order.LimitPrice,
                                  'TimeCondition': order.TimeCondition,
                                  'ContingentCondition': order.ContingentCondition,
                                  'ForceCloseReason': order.ForceCloseReason,
                                  'IsAutoSuspend': order.IsAutoSuspend,
                                  'UserForceClose': order.UserForceClose,
                                  'OrderPriceType': order.OrderPriceType,
                                  })

    def submit_cancel_order(self, FrontID, SessionID, OrderRef):
        self.t.send_trade_action('ReqOrderAction',
                                 {'BrokerID': self.cfg.BrokerID,
                                  'InvestorID': self.cfg.UserID,
                                  'FrontID': FrontID,
                                  'SessionID': SessionID,
                                  'OrderRef': OrderRef,
                                  'ExchangeID': 'SHFE'})

    def build_order_base(self):
        order = Order()

        self.index += 1
        order.OrderRef = self.index

        # fixed for all orders
        order.CombHedgeFlag = structs.CombHedgeFlag.THOST_FTDC_HF_Speculation
        order.ForceCloseReason = structs.ForceCloseReason.THOST_FTDC_FCC_NotForceClose
        order.IsAutoSuspend = structs.IsAutoSuspend.NO
        order.UserForceClose = structs.UserForceClose.NO

        # add to manager
        self.orders[order.OrderRef] = order
        return order

    def build_limit_order(self,
                          instrument,
                          direction,
                          limit_price):
        order = self.build_order_base()

        order.Instrument = instrument

        order.Direction = direction
        if direction == structs.Direction.THOST_FTDC_D_Buy:
            order.CombOffsetFlag = structs.CombOffsetFlag.THOST_FTDC_OF_Open
        else:
            order.CombOffsetFlag = structs.CombOffsetFlag.THOST_FTDC_OF_CloseToday  # default cancel today

        order.VolumeTotalOriginal = 1
        order.VolumeCondition = structs.VolumeCondition.THOST_FTDC_VC_AV
        order.MinVolume = 1

        order.LimitPrice = limit_price
        order.OrderPriceType = structs.OrderPriceType.THOST_FTDC_OPT_LimitPrice

        order.TimeCondition = structs.TimeCondition.THOST_FTDC_TC_GFD  # otherwise, always rejected
        order.ContingentCondition = structs.ContingentCondition.THOST_FTDC_CC_Immediately

        self.orders[order.OrderRef] = order
        return order

    def build_market_order(self,
                           instrument,
                           direction,
                           ):
        # currently not supported by SHFE
        order = self.build_order_base()
        order.Instrument = instrument

        order.Direction = direction
        if direction == structs.Direction.THOST_FTDC_D_Buy:
            order.CombOffsetFlag = structs.CombOffsetFlag.THOST_FTDC_OF_Open
        else:
            order.CombOffsetFlag = structs.CombOffsetFlag.THOST_FTDC_OF_Close

        order.VolumeTotalOriginal = 1
        order.VolumeCondition = structs.VolumeCondition.THOST_FTDC_VC_AV
        order.MinVolume = 1

        order.LimitPrice = 0
        order.OrderPriceType = structs.OrderPriceType.THOST_FTDC_OPT_AnyPrice

        order.TimeCondition = structs.TimeCondition.THOST_FTDC_TC_GFD
        order.ContingentCondition = structs.ContingentCondition.THOST_FTDC_CC_Immediately

        self.orders[order.OrderRef] = order
        return order
