from time import sleep
from machine import Pin, PWM
pin_tlacitko = Pin(0, Pin.IN)
pin_diody = Pin(14, Pin.OUT)

while True:
    pin_diody.value(0)
    sleep(1/6)
    pin_diody.value(1)
    sleep(1/6)
