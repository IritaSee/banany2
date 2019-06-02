import os
import logging
#logging.basicConfig(filename='run.log', level=logging.NOTSET) 
from time import *
import RPi_I2C_driver
#STARTUP IS COMING FROM CRON
mylcd=RPi_I2C_driver.lcd()
mylcd.lcd_clear()
mylcd.lcd_display_string("    Loading",1)
sleep(0.5)
mylcd.lcd_display_string("..",2)
sleep(0.5)
mylcd.lcd_display_string(".....",2)
sleep(0.5)
mylcd.lcd_display_string("........",2)
sleep(0.5)
mylcd.lcd_display_string("............",2)
sleep(0.5)
mylcd.lcd_display_string("..............",2)
sleep(0.5)
logging.warning('--------NEW SEISSON--------')
import lcd
