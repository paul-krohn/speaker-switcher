import syslog
from syslog import LOG_DEBUG as DEBUG, LOG_INFO as INFO  # LOG_WARNING as WARNING, LOG_ERR as ERROR
import os
import sys

import redis
from gpiozero.output_devices import DigitalOutputDevice


class Listener(object):

    def __init__(self, pin=17):

        self.r = redis.Redis()
        self.p = self.r.pubsub(ignore_subscribe_messages=True)
        self.pin = DigitalOutputDevice(pin)
        syslog.openlog(
            ident=os.path.basename(sys.argv[0]),
            facility=syslog.LOG_USER
        )
        self.log = syslog.syslog

    def message_handler(self, message):
        self.log(DEBUG, 'message: {}'.format(message))
        if message['data'] == b'start':
            self.pin.on()
        else:
            self.pin.off()

    def run(self):
        self.log(INFO, "listener started")
        self.p.subscribe(**{'play': self.message_handler})
        self.p.run_in_thread(sleep_time=0.01)


def listener():
    Listener().run()
