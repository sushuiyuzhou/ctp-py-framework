import datetime
import bisect
import statistics

class TSFields(object):
    AskPrice1 = 'AskPrice1'
    AskVolume1 = 'AskVolume1'
    AveragePrice = 'AveragePrice'
    BidPrice1 = 'BidPrice1'
    BidVolume1 = 'BidVolume1'
    LastPrice = 'LastPrice'
    HighestPrice = 'HighestPrice'
    LowerLimitPrice = 'LowerLimitPrice'

    Time = 'Time'
    Score = 'Score'

def tick_time(tick):
    return datetime.datetime.strptime(tick['TradingDay'] +
                                      tick['UpdateTime'] + '.' +
                                      tick['UpdateMillisec'],
                                      "%Y%m%d%H:%M:%S.%f")

def tick_score(tick):
    time = tick_time(tick)
    return tick_score_from_time(time)

def tick_score_from_time(time):
    return (3600 * time.hour + 60 * time.minute +
            time.second) * 1000 + time.microsecond % 1000


class TSData(object):
    def __init__(self, data_p, data_s, window_size = 10):
        self.window_size = window_size # mins

        # assuming data in order
        tpf, tpl = tick_time(data_p[0]), tick_time(data_p[-1])
        tsf, tsl = tick_time(data_s[0]), tick_time(data_s[-1])
        self.start, self.current = min(tpf, tsf), max(tpl, tsl)

        # init primary data set
        self.data_p = []
        for t in data_p:
            time = tick_time(t)
            self.data_p.append({
                TSFields.Time: time,
                TSFields.Score: tick_score_from_time(time),
                TSFields.AskPrice1: float(t[TSFields.AskPrice1]),
                TSFields.AskVolume1: float(t[TSFields.AskVolume1]),
                TSFields.AveragePrice: float(t[TSFields.AveragePrice]),
                TSFields.BidPrice1: float(t[TSFields.BidPrice1]),
                TSFields.BidVolume1: float(t[TSFields.BidVolume1]),
                TSFields.HighestPrice: float(t[TSFields.HighestPrice]),
                TSFields.LastPrice: float(t[TSFields.LastPrice]),
                TSFields.LowerLimitPrice: float(t[TSFields.LowerLimitPrice]),
            })

        # init secondary data set
        self.data_s = []
        for t in data_s:
            time = tick_time(t)
            self.data_s.append({
                TSFields.Time: time,
                TSFields.Score: tick_score_from_time(time),
                TSFields.AskPrice1: float(t[TSFields.AskPrice1]),
                TSFields.AskVolume1: float(t[TSFields.AskVolume1]),
                TSFields.AveragePrice: float(t[TSFields.AveragePrice]),
                TSFields.BidPrice1: float(t[TSFields.BidPrice1]),
                TSFields.BidVolume1: float(t[TSFields.BidVolume1]),
                TSFields.HighestPrice: float(t[TSFields.HighestPrice]),
                TSFields.LastPrice: float(t[TSFields.LastPrice]),
                TSFields.LowerLimitPrice: float(t[TSFields.LowerLimitPrice]),
            })

        self.init_ts_data()

    def init_ts_data(self):
        tpf, tpl = self.data_p[0].get(TSFields.Time), self.data_p[-1].get(TSFields.Time)
        tsf, tsl = self.data_s[0].get(TSFields.Time), self.data_s[-1].get(TSFields.Time)
        self.start, self.current = min(tpf, tsf), max(tpl, tsl)

        print('tick data start time:', self.start)
        print('tick data end time:', self.current)
        if self.current - self.start < datetime.timedelta(minutes=self.window_size):
            raise RuntimeError('window size not satisfied')

        def trange(start, end):
            for n in range(int((end - start).seconds * 2)):
                yield start + datetime.timedelta(milliseconds=500*n)

        self.data_b = {}
        time_p = [t[TSFields.Time] for t in self.data_p]
        time_s = [t[TSFields.Time] for t in self.data_s]
        l_p, l_s = len(time_p) - 1, len(time_s) - 1
        for time in trange(self.start, self.current):
            if not self.data_b.get(time):
                dp = self.data_p[min(bisect.bisect_left(time_p, time), l_p)]
                ds = self.data_s[min(bisect.bisect_left(time_s, time), l_s)]
                self.data_b[time] = (dp, ds)

    def _tweak_tick_data(self):
        # adjust the tick data with new tick coming in
        tpl = self.data_p[-1].get(TSFields.Time)
        tsl = self.data_s[-1].get(TSFields.Time)
        start, end = min(min(tpl, tsl), self.current), max(tpl, tsl)  # start making adjustment
        self.current = end

        def trange(start, end):
            for n in range(int((end - start).seconds * 2)):
                yield start + datetime.timedelta(milliseconds=500 * n)

        time_p = [t[TSFields.Time] for t in self.data_p]
        time_s = [t[TSFields.Time] for t in self.data_s]
        l_p, l_s = len(time_p) - 1, len(time_s) - 1
        for time in trange(start, end):
            dp = self.data_p[min(bisect.bisect_left(time_p, time), l_p)]
            ds = self.data_s[min(bisect.bisect_left(time_s, time), l_s)]
            self.data_b[time] = (dp, ds)

        self.start = min(self.data_p[0].get(TSFields.Time), self.data_s[0].get(TSFields.Time))

    def _add_tick_p(self, t):
        last_tick_time = tick_time(t)
        self.data_p.append({
                TSFields.Time: last_tick_time,
                TSFields.Score: tick_score_from_time(last_tick_time),
                TSFields.AskPrice1: float(t[TSFields.AskPrice1]),
                TSFields.AskVolume1: float(t[TSFields.AskVolume1]),
                TSFields.AveragePrice: float(t[TSFields.AveragePrice]),
                TSFields.BidPrice1: float(t[TSFields.BidPrice1]),
                TSFields.BidVolume1: float(t[TSFields.BidVolume1]),
                TSFields.HighestPrice: float(t[TSFields.HighestPrice]),
                TSFields.LastPrice: float(t[TSFields.LastPrice]),
                TSFields.LowerLimitPrice: float(t[TSFields.LowerLimitPrice]),
            })

        if self.data_p[0][TSFields.Time] < last_tick_time - datetime.timedelta(minutes=self.window_size):
            self.data_p.pop(0)

    def add_ticks_p(self, ts):
        for t in ts:
            self._add_tick_p(t)
        self._tweak_tick_data()

    def _add_tick_s(self, t):
        time = tick_time(t)
        self.data_s.append({
            TSFields.Time: time,
            TSFields.Score: tick_score_from_time(time),
            TSFields.AskPrice1: float(t[TSFields.AskPrice1]),
            TSFields.AskVolume1: float(t[TSFields.AskVolume1]),
            TSFields.AveragePrice: float(t[TSFields.AveragePrice]),
            TSFields.BidPrice1: float(t[TSFields.BidPrice1]),
            TSFields.BidVolume1: float(t[TSFields.BidVolume1]),
            TSFields.HighestPrice: float(t[TSFields.HighestPrice]),
            TSFields.LastPrice: float(t[TSFields.LastPrice]),
            TSFields.LowerLimitPrice: float(t[TSFields.LowerLimitPrice]),
        })

        if self.data_s[0][TSFields.Time] < time - datetime.timedelta(minutes=self.window_size):
            self.data_s.pop(0)

    def add_ticks_s(self, ts):
        for t in ts:
            self._add_tick_s(t)
        self._tweak_tick_data()

    # def add_tick(self, tp, ts):
    #     self.add_tick_p(tp)
    #     self.add_tick_s(ts)
    #     self._tweak_tick_data()

    def calc_last_price_difference(self):
        t, r = [],[]
        for tp, tv in self.data_b.items():
            t.append(tp)
            r.append(tv[0][TSFields.LastPrice] - tv[1][TSFields.LastPrice])
        return t,r

    def calc_difference(self, field = None):
        t, r = [], []
        for tp, tv in self.data_b.items():
            t.append(tp)
            r.append(tv[0][field] - tv[1][field])
        return t, r

    def calc_mean_and_std(self):
        _, vs = self.calc_last_price_difference()
        return statistics.mean(vs), statistics.stdev(vs)

    def calc_curr_price_diff(self):
        return self.data_p[-1][TSFields.LastPrice] - self.data_s[-1][TSFields.LastPrice]

    def calc_last_price_s(self):
        return self.data_s[-1][TSFields.LastPrice]

    def calc_last_price_p(self):
        return self.data_p[-1][TSFields.LastPrice]

    def calc_last_price_diff_p(self):
        return self.data_p[-1][TSFields.LastPrice] - self.data_p[-2][TSFields.LastPrice]



