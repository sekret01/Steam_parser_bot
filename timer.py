import time


SEC = 1
MIN = 60
HOUR = 1200

class Timer:
    """ ... """

    def __init__(self):
        self.pause = 12 * HOUR
        self.discount_monitor = ...

    def wait(self):
        time.sleep(self.pause)

    def monitoring(self):
        pass
