import os
import logging
logging.basicConfig(filename='daily.log', level=logging.DEBUG , format='%(ascitime)s:%s(levelname)s:%(message)s') 
from time import *
import RPi_I2C_driver
mylcd=RPi_I2C_driver.lcd()
mylcd.lcd_clear()
mylcd.lcd_display_string("   Loading",1)
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
logging.debug('NEW SEISSON')
import lcd
