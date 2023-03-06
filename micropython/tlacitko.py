from machine import Pin
pin_diody = Pin(14, Pin.OUT)
pin_tlacitko = Pin(0, Pin.IN)

while True:
    pin_diody.value(1 - pin_tlacitko.value())

# mpremote connect /dev/tty.usbserial-0001 run displej.py
