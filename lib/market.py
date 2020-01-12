import lib.redis_cli as rc
import config as cfg


class Market(object):
    '''
    Connetion to CTP market module

    Current storage model:
    key "CThostFtdcReqUserLoginField" - user login details
    key "SubscribeMarketData.Instruments" - all instruments to subscribe
    '''
    KeyUserLogin = "CThostFtdcReqUserLoginField"
    KeyInstruments = "SubscribeMarketData.Instruments"
    KeyMarketData = "OnRtnDepthMarketData"

    def __init__(self,
                 name='[market]'):
        self.name = name

        # redis client handle
        self.c = rc.RedisClient(name='market',
                                host=cfg.RedisConfig.Host,
                                port=cfg.RedisConfig.PortMarket)
        # redis utils handle
        self.r = self.c.r

        # initialize pubsub handle
        self.p = self.c.ps()

        # response queue
        self.q = None

    # strategy methods
    def req_user_login(self):
        '''
        req CTP user login
        :return:
        '''
        self.r.publish("ReqUserLogin", "run")

    def subscribe_to_market_data(self):
        '''
        subscribe to CTP market data
        :return:
        '''
        self.p.subscribe(self.KeyMarketData)
        self.r.publish("SubscribeMarketData", "run")

    def query_currently_instruments_settings(self):
        '''
        query current settings for subscribed instruments
        :return:
        '''
        return rc.decode(self.r.smembers(self.KeyInstruments))

    def query_market_data_by_key(self, key):
        # return everything under key
        return rc.decode(self.r.zrangebylex(key, '[a', '[z'))
