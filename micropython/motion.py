from machine import Pin, PWM
from time import sleep

pin = Pin(2, Pin.OUT)
pwm = PWM(pin, freq=50, duty=120)

while True:
    sleep(1)
    pwm.duty(35)
    sleep(1)
    pwm.duty(50)
    sleep(1)
    pwm.duty(120)
