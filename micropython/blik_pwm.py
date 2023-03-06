from time import sleep
from machine import Pin, PWM
pin_tlacitko = Pin(0, Pin.IN)
pin_diody = Pin(14, Pin.OUT)

pwm = PWM(pin_diody, freq=50, duty=512)
