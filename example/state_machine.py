import threading
import time
import random

class Machine(object):
    ''' sample stata machine '''
    def __init__(self):
        self.cv = threading.Condition()

    def _listen_for_tick(self, cv):
        while(True):
            with cv:
                time.sleep(random.random())
                print('trigger signal')
                cv.notify()

    def listen_for_tick(self):
        s = threading.Thread(target=self._listen_for_tick, args=(self.cv,))
        s.start()

    def run(self):
        print("wait for signal")
        while(True):
            with self.cv:
                avail = self.cv.wait(timeout=0.5)
                if not avail:
                    print("wait too long")
                else:
                    print("got signal")

if __name__ == "__main__":
    m = Machine()
    m.listen_for_tick()
    m.run()
