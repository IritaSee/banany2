import os
import shutil
import RPi_I2C_driver
from time import *
import logging
#logging.basicConfig(filename='run.log', level=logging.NOTSET ,format='%(asciitime)s:%(message)s')
#import yeyeye 
#CARA GOBLOK
mylcd = RPi_I2C_driver.lcd()
os.system("sudo service stop devurules.service")
logging.debug('card detected, devurules should stop')
mylcd.lcd_display_string("SD CARD In!", 1)
mylcd.lcd_display_string("Mounting...", 2)
mylcd.backlight(0)
sleep(0.5)
mylcd.backlight(1)
sleep(0.5)
mylcd.backlight(0)
sleep(0.5)
mylcd.backlight(1)
sleep(0.5)
mylcd.backlight(0)
sleep(0.5)
mylcd.backlight(1)
logging.warning('starting nyala.service')
os.system ("sudo systemctl start nyala.service")
exit()
