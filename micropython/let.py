from time import sleep
from machine import Pin, PWM
from neopixel import NeoPixel

pin = Pin(2, Pin.OUT)
np = NeoPixel(pin, 8)
np[0] = (255,0,255)
np[1] = (50,205,50)
np[2] = (0,0,255)
np[3] = (255, 191, 0)
np[4] = (159, 43, 104)
np[5] = (50,205,50)
np[6] = (0,0,255)
np[7] = (255, 191, 0)
np.write()
