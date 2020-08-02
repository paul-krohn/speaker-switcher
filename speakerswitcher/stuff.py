import redis
from gpiozero.output_devices import DigitalOutputDevice


class Listener(object):

    def __init__(self, pin=17):

        self.r = redis.Redis()
        self.p = self.r.pubsub(ignore_subscribe_messages=True)
        self.pin = DigitalOutputDevice(pin)

    def message_handler(self, message):
        print('message: {}'.format(message))
        if message['data'] == b'start':
            self.pin.on()
        else:
            self.pin.off()

    def run(self):
        self.p.subscribe(**{'play': self.message_handler})

        thread = self.p.run_in_thread(sleep_time=0.01)


def listener():
    Listener().run()
