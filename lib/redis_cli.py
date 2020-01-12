# storage model for ctp
import redis
import threading

from lib.logger import get_logger


def decode(ctn):
    '''
    convert bytes to string
    :param ctn:
    :return:
    '''
    if isinstance(ctn, bytes):
        return ctn.decode('gbk')
    if isinstance(ctn, list) or isinstance(ctn, tuple):
        return [decode(c) for c in ctn]
    if isinstance(ctn, dict):
        return dict(zip([k.decode('gbk') for k in ctn.keys()], [v.decode(
            'gbk') for v in ctn.values()]))


class RedisClient(object):
    def __init__(self,
                 host='localhost',
                 port=6379,
                 db=0,
                 name='ctp-redis'):
        # connection params
        self.name = name
        self.host = host
        self.port = port
        self.db = db

        # logger
        self.logger = get_logger(self.name)

        # pubsub handler
        self._ps = None

        # if to preserve rtn signals
        self.queue = None
        self._lock = threading.Lock()

        self.logger.info("[RedisClient]: start connection...")
        self.r = redis.Redis(host=host, port=port, db=db)

        if not self.r.ping():
            raise RuntimeError("[RedisClient]: fail to establish redis connection")

        # ps handlers
        self.ps_handlers = dict()
        self._listener_started = False

        self.logger.info("[RedisClient]: init complete")

    def __str__(self):
        return "RedisClient connected to host {}, at port {}, db {}".format(self.host, self.port, self.db)

    def ps(self):
        '''
        getter for ps handle
        :return:
        '''
        if not self._ps:
            self.logger.debug('[RedisClient]: init pubsub process')
            self._ps = self.r.pubsub()
        return self._ps

    def add_ps_handler(self, name, handler):
        '''
        add handler for pubsub rtn key
        the handler should accept one argument which is the hash key in redis db
        :param handler:
        :return:
        '''
        self.ps_handlers[name] = handler

    def remove_ps_handler(self, name):
        '''
        remote a handler
        :param name:
        :return:
        '''
        self.ps_handlers.pop(name, None)

    def subscribe_to_topic(self, topic):
        '''
        subscribe to topic
        then start the pubsub listener
        :param topic:
        :return:
        '''
        self.ps().subscribe(topic)

    def start_pubsub_listener(self):
        '''
        start pubsub listener in current thread
        this must start after all topics were subscribed
        :return:
        '''
        for msg in self.ps().listen():
            self.logger.debug("[RedisClient]: subscriber received - %s", msg)
            # key to the hash in redis db
            channel = decode(msg.get('channel')) # topic
            key = decode(msg.get('data'))
            # exclude subscribe success message for now
            if isinstance(key, str):
                for handler in self.ps_handlers.values():
                    handler(channel, key)

    def start_pubsub_listener_on_thread(self):
        '''
        start the listener in separate thread
        :return:
        '''
        if self._listener_started:
            raise RuntimeError('ps listener already started')

        if not self._listener_started:
            self._listener_started = True

        thread = threading.Thread(target=self.start_pubsub_listener, args=())
        thread.start()

    def subscribe_to_topics_and_attache_to_queue(self):
        '''
        debug helper to register pub/sub rtn keys, this will attach full history to queue
        note: do not use this in production, as ps handle can only be monitored by one thread only
        :return:
        '''

        def f():
            for m in self.ps().listen():
                self._lock.acquire()
                try:
                    self.queue.append(m)
                    self.logger.debug('[RedisClient]: msg - ', m)
                finally:
                    self._lock.release()

        t = threading.Thread(target=f)
        t.start()
        return t


if __file__ == "__main__":
    print("RedisClient: utils for ctp storage connection")
