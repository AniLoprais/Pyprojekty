from machine import Pin, PWM
from time import sleep
from onewire import OneWire
from ds18x20 import DS18X20

pin = Pin(2, Pin.IN)
ow = DS18X20(OneWire(pin))
sensory = ow.scan()
print('Pripojene teplomery:', sensory)

ow.convert_temp()
sleep(1)
teplota = ow.read_temp(sensory[0])
print('Teplosta je', teplota)
