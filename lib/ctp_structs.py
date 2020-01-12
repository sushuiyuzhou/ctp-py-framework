# response topics from CTP
class RspTopics(object):
    OnRspAuthenticate = "OnRspAuthenticate"
    OnRspUserLogin = "OnRspUserLogin"
    OnRspUserLogout = "OnRspUserLogout"
    OnRspUserPasswordUpdate = "OnRspUserPasswordUpdate"
    OnRspTradingAccountPasswordUpdate = "OnRspTradingAccountPasswordUpdate"
    OnRspUserAuthMethod = "OnRspUserAuthMethod"
    OnRspGenUserCaptcha = "OnRspGenUserCaptcha"
    OnRspGenUserText = "OnRspGenUserText"
    OnRspOrderInsert = "OnRspOrderInsert"
    OnRspParkedOrderInsert = "OnRspParkedOrderInsert"
    OnRspParkedOrderAction = "OnRspParkedOrderAction"
    OnRspOrderAction = "OnRspOrderAction"
    OnRspQueryMaxOrderVolume = "OnRspQueryMaxOrderVolume"
    OnRspSettlementInfoConfirm = "OnRspSettlementInfoConfirm"
    OnRspRemoveParkedOrder = "OnRspRemoveParkedOrder"
    OnRspRemoveParkedOrderAction = "OnRspRemoveParkedOrderAction"
    OnRspExecOrderInsert = "OnRspExecOrderInsert"
    OnRspExecOrderAction = "OnRspExecOrderAction"
    OnRspForQuoteInsert = "OnRspForQuoteInsert"
    OnRspQuoteInsert = "OnRspQuoteInsert"
    OnRspQuoteAction = "OnRspQuoteAction"
    OnRspBatchOrderAction = "OnRspBatchOrderAction"
    OnRspOptionSelfCloseInsert = "OnRspOptionSelfCloseInsert"
    OnRspOptionSelfCloseAction = "OnRspOptionSelfCloseAction"
    OnRspCombActionInsert = "OnRspCombActionInsert"
    OnRspQryOrder = "OnRspQryOrder"
    OnRspQryTrade = "OnRspQryTrade"
    OnRspQryInvestorPosition = "OnRspQryInvestorPosition"
    OnRspQryTradingAccount = "OnRspQryTradingAccount"
    OnRspQryInvestor = "OnRspQryInvestor"
    OnRspQryTradingCode = "OnRspQryTradingCode"
    OnRspQryInstrumentMarginRate = "OnRspQryInstrumentMarginRate"
    OnRspQryInstrumentCommissionRate = "OnRspQryInstrumentCommissionRate"
    OnRspQryExchange = "OnRspQryExchange"
    OnRspQryProduct = "OnRspQryProduct"
    OnRspQryInstrument = "OnRspQryInstrument"
    OnRspQryDepthMarketData = "OnRspQryDepthMarketData"
    OnRspQrySettlementInfo = "OnRspQrySettlementInfo"
    OnRspQryTransferBank = "OnRspQryTransferBank"
    OnRspQryInvestorPositionDetail = "OnRspQryInvestorPositionDetail"
    OnRspQryNotice = "OnRspQryNotice"
    OnRspQrySettlementInfoConfirm = "OnRspQrySettlementInfoConfirm"
    OnRspQryInvestorPositionCombineDetail = "OnRspQryInvestorPositionCombineDetail"
    OnRspQryCFMMCTradingAccountKey = "OnRspQryCFMMCTradingAccountKey"
    OnRspQryEWarrantOffset = "OnRspQryEWarrantOffset"
    OnRspQryInvestorProductGroupMargin = "OnRspQryInvestorProductGroupMargin"
    OnRspQryExchangeMarginRate = "OnRspQryExchangeMarginRate"
    OnRspQryExchangeMarginRateAdjust = "OnRspQryExchangeMarginRateAdjust"
    OnRspQryExchangeRate = "OnRspQryExchangeRate"
    OnRspQrySecAgentACIDMap = "OnRspQrySecAgentACIDMap"
    OnRspQryProductExchRate = "OnRspQryProductExchRate"
    OnRspQryProductGroup = "OnRspQryProductGroup"
    OnRspQryMMInstrumentCommissionRate = "OnRspQryMMInstrumentCommissionRate"
    OnRspQryMMOptionInstrCommRate = "OnRspQryMMOptionInstrCommRate"
    OnRspQryInstrumentOrderCommRate = "OnRspQryInstrumentOrderCommRate"
    OnRspQrySecAgentTradingAccount = "OnRspQrySecAgentTradingAccount"
    OnRspQrySecAgentCheckMode = "OnRspQrySecAgentCheckMode"
    OnRspQrySecAgentTradeInfo = "OnRspQrySecAgentTradeInfo"
    OnRspQryOptionInstrTradeCost = "OnRspQryOptionInstrTradeCost"
    OnRspQryOptionInstrCommRate = "OnRspQryOptionInstrCommRate"
    OnRspQryExecOrder = "OnRspQryExecOrder"
    OnRspQryForQuote = "OnRspQryForQuote"
    OnRspQryQuote = "OnRspQryQuote"
    OnRspQryOptionSelfClose = "OnRspQryOptionSelfClose"
    OnRspQryInvestUnit = "OnRspQryInvestUnit"
    OnRspQryCombInstrumentGuard = "OnRspQryCombInstrumentGuard"
    OnRspQryCombAction = "OnRspQryCombAction"
    OnRspQryTransferSerial = "OnRspQryTransferSerial"
    OnRspQryAccountregister = "OnRspQryAccountregister"
    OnRspQryContractBank = "OnRspQryContractBank"
    OnRspQryParkedOrder = "OnRspQryParkedOrder"
    OnRspQryParkedOrderAction = "OnRspQryParkedOrderAction"
    OnRspQryTradingNotice = "OnRspQryTradingNotice"
    OnRspQryBrokerTradingParams = "OnRspQryBrokerTradingParams"
    OnRspQryBrokerTradingAlgos = "OnRspQryBrokerTradingAlgos"
    OnRspQueryCFMMCTradingAccountToken = "OnRspQueryCFMMCTradingAccountToken"
    OnRspFromBankToFutureByFuture = "OnRspFromBankToFutureByFuture"
    OnRspFromFutureToBankByFuture = "OnRspFromFutureToBankByFuture"
    OnRspQueryBankAccountMoneyByFuture = "OnRspQueryBankAccountMoneyByFuture"

# rtn topics from CTP
class RtnTopics(object):
    OnRtnOrder = "OnRtnOrder"
    OnRtnTrade = "OnRtnTrade"
    OnRtnInstrumentStatus = "OnRtnInstrumentStatus"
    OnRtnBulletin = "OnRtnBulletin"
    OnRtnTradingNotice = "OnRtnTradingNotice"
    OnRtnErrorConditionalOrder = "OnRtnErrorConditionalOrder"
    OnRtnExecOrder = "OnRtnExecOrder"
    OnRtnQuote = "OnRtnQuote"
    OnRtnForQuoteRsp = "OnRtnForQuoteRsp"
    OnRtnCFMMCTradingAccountToken = "OnRtnCFMMCTradingAccountToken"
    OnRtnOptionSelfClose = "OnRtnOptionSelfClose"
    OnRtnCombAction = "OnRtnCombAction"
    OnRtnFromBankToFutureByBank = "OnRtnFromBankToFutureByBank"
    OnRtnFromFutureToBankByBank = "OnRtnFromFutureToBankByBank"
    OnRtnRepealFromBankToFutureByBank = "OnRtnRepealFromBankToFutureByBank"
    OnRtnRepealFromFutureToBankByBank = "OnRtnRepealFromFutureToBankByBank"
    OnRtnFromBankToFutureByFuture = "OnRtnFromBankToFutureByFuture"
    OnRtnFromFutureToBankByFuture = "OnRtnFromFutureToBankByFuture"
    OnRtnRepealFromBankToFutureByFutureManual = \
        "OnRtnRepealFromBankToFutureByFutureManual"
    OnRtnRepealFromFutureToBankByFutureManual = \
        "OnRtnRepealFromFutureToBankByFutureManual"
    OnRtnQueryBankBalanceByFuture = "OnRtnQueryBankBalanceByFuture"
    OnRtnRepealFromBankToFutureByFuture = \
        "OnRtnRepealFromBankToFutureByFuture"
    OnRtnRepealFromFutureToBankByFuture = \
        "OnRtnRepealFromFutureToBankByFuture"
    OnRtnOpenAccountByBank = "OnRtnOpenAccountByBank"
    OnRtnCancelAccountByBank = "OnRtnCancelAccountByBank"
    OnRtnChangeAccountByBank = "OnRtnChangeAccountByBank"

# err rtn topics from CTP
class ErrRtnTopics(object):
    OnErrRtnOrderInsert = "OnErrRtnOrderInsert"
    OnErrRtnOrderAction = "OnErrRtnOrderAction"
    OnErrRtnExecOrderInsert = "OnErrRtnExecOrderInsert"
    OnErrRtnExecOrderAction = "OnErrRtnExecOrderAction"
    OnErrRtnForQuoteInsert = "OnErrRtnForQuoteInsert"
    OnErrRtnQuoteInsert = "OnErrRtnQuoteInsert"
    OnErrRtnQuoteAction = "OnErrRtnQuoteAction"
    OnErrRtnBatchOrderAction = "OnErrRtnBatchOrderAction"
    OnErrRtnOptionSelfCloseInsert = "OnErrRtnOptionSelfCloseInsert"
    OnErrRtnOptionSelfCloseAction = "OnErrRtnOptionSelfCloseAction"
    OnErrRtnCombActionInsert = "OnErrRtnCombActionInsert"
    OnErrRtnBankToFutureByFuture = "OnErrRtnBankToFutureByFuture"
    OnErrRtnFutureToBankByFuture = "OnErrRtnFutureToBankByFuture"
    OnErrRtnRepealBankToFutureByFutureManual = \
        "OnErrRtnRepealBankToFutureByFutureManual"
    OnErrRtnRepealFutureToBankByFutureManual = \
        "OnErrRtnRepealFutureToBankByFutureManual"
    OnErrRtnQueryBankBalanceByFuture = "OnErrRtnQueryBankBalanceByFuture"

# the following are CTP structs related to trade status
class OrderPriceType(object):
    # TFtdcOrderPriceTypeType是一个报单价格条件类型
    # 任意价
    THOST_FTDC_OPT_AnyPrice = '1'
    # 限价
    THOST_FTDC_OPT_LimitPrice = '2'
    # 最优价
    THOST_FTDC_OPT_BestPrice = '3'
    # 最新价
    THOST_FTDC_OPT_LastPrice = '4'
    # 最新价浮动上浮1个ticks
    THOST_FTDC_OPT_LastPricePlusOneTicks = '5'
    # 最新价浮动上浮2个ticks
    THOST_FTDC_OPT_LastPricePlusTwoTicks = '6'
    # 最新价浮动上浮3个ticks
    THOST_FTDC_OPT_LastPricePlusThreeTicks = '7'
    # 卖一价
    THOST_FTDC_OPT_AskPrice1 = '8'
    # 卖一价浮动上浮1个ticks
    THOST_FTDC_OPT_AskPrice1PlusOneTicks = '9'
    # 卖一价浮动上浮2个ticks
    THOST_FTDC_OPT_AskPrice1PlusTwoTicks = 'A'
    # 卖一价浮动上浮3个ticks
    THOST_FTDC_OPT_AskPrice1PlusThreeTicks = 'B'
    # 买一价
    THOST_FTDC_OPT_BidPrice1 = 'C'
    # 买一价浮动上浮1个ticks
    THOST_FTDC_OPT_BidPrice1PlusOneTicks = 'D'
    # 买一价浮动上浮2个ticks
    THOST_FTDC_OPT_BidPrice1PlusTwoTicks = 'E'
    # 买一价浮动上浮3个ticks
    THOST_FTDC_OPT_BidPrice1PlusThreeTicks = 'F'
    # 五档价
    THOST_FTDC_OPT_FiveLevelPrice = 'G'


class Direction(object):
    # TFtdcDirectionType是一个买卖方向类型
    # 买
    THOST_FTDC_D_Buy = '0'
    # 卖
    THOST_FTDC_D_Sell = '1'


class CombOffsetFlag(object):
    # TFtdcOffsetFlagType是一个开平标志类型
    # 开仓
    THOST_FTDC_OF_Open = '0'
    # 平仓
    THOST_FTDC_OF_Close = '1'
    # 强平
    THOST_FTDC_OF_ForceClose = '2'
    # 平今
    THOST_FTDC_OF_CloseToday = '3'
    # 平昨
    THOST_FTDC_OF_CloseYesterday = '4'
    # 强减
    THOST_FTDC_OF_ForceOff = '5'
    # 本地强平
    THOST_FTDC_OF_LocalForceClose = '6'


class CombHedgeFlag(object):
    # TFtdcHedgeFlagType是一个投机套保标志类型
    # 投机
    THOST_FTDC_HF_Speculation = '1'
    # 套利
    THOST_FTDC_HF_Arbitrage = '2'
    # 套保
    THOST_FTDC_HF_Hedge = '3'
    # 做市商
    THOST_FTDC_HF_MarketMaker = '5'
    # 第一腿投机第二腿套保
    # 大商所专用
    THOST_FTDC_HF_SpecHedge = '6'
    # 第一腿套保第二腿投机
    # 大商所专用
    THOST_FTDC_HF_HedgeSpec = '7'


class TimeCondition(object):
    # TFtdcTimeConditionType是一个有效期类型类型
    # 立即完成，否则撤销
    THOST_FTDC_TC_IOC = '1'
    # 本节有效
    THOST_FTDC_TC_GFS = '2'
    # 当日有效
    THOST_FTDC_TC_GFD = '3'
    # 指定日期前有效
    THOST_FTDC_TC_GTD = '4'
    # 撤销前有效
    THOST_FTDC_TC_GTC = '5'
    # 集合竞价有效
    THOST_FTDC_TC_GFA = '6'


class VolumeCondition(object):
    # TFtdcVolumeConditionType是一个成交量类型类型
    # 任何数量
    THOST_FTDC_VC_AV = '1'
    # 最小数量
    THOST_FTDC_VC_MV = '2'
    # 全部数量
    THOST_FTDC_VC_CV = '3'


class ContingentCondition(object):
    # TFtdcContingentConditionType是一个触发条件类型
    # 立即
    THOST_FTDC_CC_Immediately = '1'
    # 止损
    THOST_FTDC_CC_Touch = '2'
    # 止赢
    THOST_FTDC_CC_TouchProfit = '3'
    # 预埋单
    THOST_FTDC_CC_ParkedOrder = '4'
    # 最新价大于条件价
    THOST_FTDC_CC_LastPriceGreaterThanStopPrice = '5'
    # 最新价大于等于条件价
    THOST_FTDC_CC_LastPriceGreaterEqualStopPrice = '6'
    # 最新价小于条件价
    THOST_FTDC_CC_LastPriceLesserThanStopPrice = '7'
    # 最新价小于等于条件价
    THOST_FTDC_CC_LastPriceLesserEqualStopPrice = '8'
    # 卖一价大于条件价
    THOST_FTDC_CC_AskPriceGreaterThanStopPrice = '9'
    # 卖一价大于等于条件价
    THOST_FTDC_CC_AskPriceGreaterEqualStopPrice = 'A'
    # 卖一价小于条件价
    THOST_FTDC_CC_AskPriceLesserThanStopPrice = 'B'
    # 卖一价小于等于条件价
    THOST_FTDC_CC_AskPriceLesserEqualStopPrice = 'C'
    # 买一价大于条件价
    THOST_FTDC_CC_BidPriceGreaterThanStopPrice = 'D'
    # 买一价大于等于条件价
    THOST_FTDC_CC_BidPriceGreaterEqualStopPrice = 'E'
    # 买一价小于条件价
    THOST_FTDC_CC_BidPriceLesserThanStopPrice = 'F'
    # 买一价小于等于条件价
    THOST_FTDC_CC_BidPriceLesserEqualStopPrice = 'H'


class ForceCloseReason(object):
    # TFtdcForceCloseReasonType是一个强平原因类型
    # 非强平
    THOST_FTDC_FCC_NotForceClose = '0'
    # 资金不足
    THOST_FTDC_FCC_LackDeposit = '1'
    # 客户超仓
    THOST_FTDC_FCC_ClientOverPositionLimit = '2'
    # 会员超仓
    THOST_FTDC_FCC_MemberOverPositionLimit = '3'
    # 持仓非整数倍
    THOST_FTDC_FCC_NotMultiple = '4'
    # 违规
    THOST_FTDC_FCC_Violation = '5'
    # 其它
    THOST_FTDC_FCC_Other = '6'
    # 自然人临近交割
    THOST_FTDC_FCC_PersonDeliv = '7'


class UserForceClose(object):
    YES = '1'
    NO = '0'


class IsAutoSuspend(object):
    YES = '1'
    NO = '0'


class OrderStatus(object):
    # TFtdcOrderStatusType是一个报单状态类型
    # 全部成交
    THOST_FTDC_OST_AllTraded = '0'
    # 部分成交还在队列中
    THOST_FTDC_OST_PartTradedQueueing = '1'
    # 部分成交不在队列中
    THOST_FTDC_OST_PartTradedNotQueueing = '2'
    # 未成交还在队列中
    THOST_FTDC_OST_NoTradeQueueing = '3'
    # 未成交不在队列中
    THOST_FTDC_OST_NoTradeNotQueueing = '4'
    # 撤单
    THOST_FTDC_OST_Canceled = '5'
    # 未知
    THOST_FTDC_OST_Unknown = 'a'
    # 尚未触发
    THOST_FTDC_OST_NotTouched = 'b'
    # 已触发
    THOST_FTDC_OST_Touched = 'c'


class OrderSubmitStatus(object):
    # TFtdcOrderSubmitStatusType是一个报单提交状态类型
    # 已经提交
    THOST_FTDC_OSS_InsertSubmitted = '0'
    # 撤单已经提交
    THOST_FTDC_OSS_CancelSubmitted = '1'
    # 修改已经提交
    THOST_FTDC_OSS_ModifySubmitted = '2'
    # 已经接受
    THOST_FTDC_OSS_Accepted = '3'
    # 报单已经被拒绝
    THOST_FTDC_OSS_InsertRejected = '4'
    # 撤单已经被拒绝
    THOST_FTDC_OSS_CancelRejected = '5'
    # 改单已经被拒绝
    THOST_FTDC_OSS_ModifyRejected = '6'
