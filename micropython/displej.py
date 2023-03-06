# Importy
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# Komunikační protokol I2C a display SSD1306, 128x 64 bodů
i2c = I2C(scl=Pin(4, Pin.OUT), sda=Pin(14, Pin.OUT))
oled = SSD1306_I2C(width=128, height=64, i2c=i2c, addr=0x3c)

# Různé kreslící příkazy (se objeví až po zavolání show())
# oled.line(0, 0, 64, 64, 1)
oled.text("VASEK IS COOL", 0, 20, 1)
oled.text("HELLO", 0, 40, 1)
# oled.rect(110, 2, 10, 5, 1)
# oled.fill_rect(100, 20, 10, 5, 1)
# oled.show()

ICON = [
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 1, 1, 0, 0, 0, 1, 1, 0],
    [ 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [ 0, 1, 1, 1, 1, 1, 1, 1, 0],
    [ 0, 0, 1, 1, 1, 1, 1, 0, 0],
    [ 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [ 0, 0, 0, 0, 1, 0, 0, 0, 0],
]

# oled.fill(0) # Clear the display
for y, row in enumerate(ICON):
    for x, c in enumerate(row):
        oled.pixel(x, y, c)

oled.show()
