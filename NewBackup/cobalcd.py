import os
import shutil
import RPi_I2C_driver
import datetime

from time import *

mylcd=RPi_I2C_driver.lcd()
mylcd.backlight(1)
mylcd.lcd_clear()
mylcd.lcd_display_string("  Blink test ",1)
mylcd.lcd_display_string("ctrl c to finish",2)
a=0
while (a<5):
	mylcd.backlight(0)
	sleep(0.3)
	mylcd.backlight(1)
	sleep(0.3)
	a=a+1
mylcd.lcd_clear()
while (1>0):
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Banany's DATE:..",1)
    mylcd.lcd_display_string("%s" %datetime.datetime.now().date(),2)
    sleep(2)
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Banany's TIME:.",1)
    mylcd.lcd_display_string("%s" %datetime.datetime.now().time(),2)
    sleep(2)
    
