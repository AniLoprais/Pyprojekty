from machine import Pin, PWM, sleep

pin_1a = Pin(5, Pin.OUT)  # D1 na destičce, 1A na čipu
pin_2a = Pin(4, Pin.OUT)  # D2 na destičce, 2A na čipu
pin_12en = Pin(0, Pin.OUT)  # D3 na destičce, 1,2EN na čipu

pin_3a = Pin(12, Pin.OUT)  # D1 na destičce, 1A na čipu
pin_4a = Pin(13, Pin.OUT)  # D2 na destičce, 2A na čipu
pin_34en = Pin(15, Pin.OUT)

pin_tlacitko = Pin(14, Pin.IN, Pin.PULL_UP)

frekvence = 50
duty = 800

pin_1a.value(1)
pin_2a.value(0)
pwm_1 = PWM(pin_12en, freq=frekvence, duty=duty)

pin_3a.value(0)
pin_4a.value(1)
pwm_2 = PWM(pin_34en, freq=frekvence, duty=duty)

while True:
    if pin_tlacitko.value():
        pwm_1.duty(0)
        pwm_2.duty(0)
    else:
        pwm_1.duty(duty)
        pwm_2.duty(duty)

# mpremote connect /dev/tty.usbserial-0001 run displej.py

# # pin_12en.value(1)
# # for fr in range(0, 100):
#     pin_1a.value(0)
#     pin_2a.value(1)

#     pwm_1 = PWM(pin_12en, freq=fr, duty=duty)
# # pwm_1.duty(128)

#     pin_3a.value(0)
#     pin_4a.value(1)
# # pin_34en.value(1)
#     pwm_2 = PWM(pin_34en, freq=fr, duty=duty)
# # pwm_2.duty(128)

#     # sleep(1/3)
