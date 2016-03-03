import RPi.GPIO as GPIO
import time

class GPIOManager:

    PIN_MODE_NONE = 0
    PIN_MODE_INPUT = 1
    PIN_MODE_OUTPUT = 2

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.pins = {
            7: self.PIN_MODE_NONE,
            11: self.PIN_MODE_NONE,
            12: self.PIN_MODE_NONE,
            13: self.PIN_MODE_NONE,
            15: self.PIN_MODE_NONE,
            16: self.PIN_MODE_NONE,
            18: self.PIN_MODE_NONE,
            22: self.PIN_MODE_NONE,
            29: self.PIN_MODE_NONE,
            31: self.PIN_MODE_NONE,
            32: self.PIN_MODE_NONE,
            33: self.PIN_MODE_NONE,
            34: self.PIN_MODE_NONE,
            35: self.PIN_MODE_NONE,
            36: self.PIN_MODE_NONE,
            37: self.PIN_MODE_NONE,
            38: self.PIN_MODE_NONE,
            40: self.PIN_MODE_NONE,
        }

    def __enter__(self):
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        self.all_off()
        GPIO.cleanup()

    def register_output(self, pin_number):
        self.pins[pin_number] = self.PIN_MODE_OUTPUT
        GPIO.setup(pin_number, GPIO.OUT)

    def on(self, pin_number):
        if pin_number in self.pins and self.pins[pin_number] is self.PIN_MODE_OUTPUT:
            GPIO.output(pin_number, GPIO.HIGH)

    def off(self, pin_number):
        if pin_number in self.pins and self.pins[pin_number] is self.PIN_MODE_OUTPUT:
            GPIO.output(pin_number, GPIO.LOW)

    def all_off(self):
        for pin_number, pin_type in self.pins.iteritems():
            if pin_type == self.PIN_MODE_OUTPUT:
                self.off(pin_number)

    def all_on(self):
        for pin_number, pin_type in self.pins.iteritems():
            if pin_type == self.PIN_MODE_OUTPUT:
                self.on(pin_number)

with GPIOManager() as gpio_manager:
    gpio_manager.register_output(11)
    gpio_manager.register_output(12)
    gpio_manager.register_output(13)
    gpio_manager.register_output(15)
    gpio_manager.all_on()
    time.sleep(5)
