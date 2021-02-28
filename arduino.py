from pyfirmata import Arduino, util
import time


class ArduinoLeds:
    def __init__(self):

        self.Uno = Arduino('/dev/ttyUSB0')

        print('LEDS INICIADOS!')

        self.Uno.digital[12].write(1)
        self.Uno.digital[11].write(1)

        print('LEDS OFF!')

    def yellow_led_on(self):
        self.Uno.digital[12].write(0)

    def yellow_led_off(self):
        self.Uno.digital[12].write(1)

    def blue_led_blink(self):
        for i in range(1, 5):
            self.Uno.digital[11].write(1)
            time.sleep(0.5)
            self.Uno.digital[11].write(0)
            time.sleep(0.5)
        self.Uno.digital[11].write(1)

    def yello_led_blink(self):
        for i in range(1, 5):
            self.Uno.digital[12].write(1)
            time.sleep(0.5)
            self.Uno.digital[12].write(0)
            time.sleep(0.5)
        self.Uno.digital[12].write(1)
