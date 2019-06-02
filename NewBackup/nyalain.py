import RPi_I2C_driver
import os
from time import *
mylcd= RPi_I2C_driver.lcd()
mylcd.backlight(1)
print("ON, and LCD has been reset")
