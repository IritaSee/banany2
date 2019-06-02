import os
from time import *
#sleep(5)
import RPi_I2C_driver
import logging
logging.basicConfig(filename='run.log',level=logging.NOTSET)
#print ("initializing")
mylcd=RPi_I2C_driver.lcd()
print ("\t\tBANANY Console ver. 0.2")
print ("------------------------------------------------------------------------")
print ("By: Iga Narendra, Nanjaya Satya, \nAwi Wigraha, Agni Prema, Dwiweka Naratama, 2018")
print ("currently running: lcd.py\n")
#print("\n")
cekpar=os.popen("sudo blkid /dev/sdb1").read().split()[4]
print (cekpar)
if cekpar=='TYPE="ntfs"':
	cekpar='sdb1'
else: 
	cekpar='sdb2'

print ("active partition: "+cekpar)
logging.warning('active partition: {}'.format(cekpar))
os.system("sudo systemctl stop nyala.service")
logging.warning('nyala.service should stop')
os.system("sudo systemctl start devurules.service")
logging.warning('devurules.service should start, and lcd running')
#fungsi out ke lcd sementara dipadamkan karena lagi rusak
#out_ke_lcd()
#import RPi_I2C_driver
#sleep(5)
#mylcd = RPi_I2C_driver.lcd()
    # test 2
mylcd.lcd_clear()
mylcd.lcd_display_string("  BANANY READY ",1)
mylcd.lcd_display_string("----WELCOME!----",2)
sleep(5)
mylcd.lcd_clear()
mylcd.lcd_display_string("WiFi:BANANY01",1)
mylcd.lcd_display_string("PWD:bananybanany",2)
sleep(5)
#   sd=os.popen("sudo df /dev/sda1").read().split()[-2]
#  print sd
#partition check part, should wait bcs this tool
#prioritise startup, then mount things up
print("Searching for drive and mounting it")
mylcd.lcd_clear()
mylcd.lcd_display_string("Searching drive",1)
mylcd.lcd_display_string("  please wait",2)
logging.warning('waiting for drive to be mounted')
sleep(5)
direk=os.popen("sudo df /dev/"+cekpar+" -h").read().split()[-3:]
hdda=os.popen("sudo df /dev/"+cekpar+" -h").read().split()[-4:]
logging.warning('directory: {}'.format(direk))
logging.warning('drive: {}'.format(hdda))
print (hdda) 
if(hdda[0].count("G")>0 or hdda[0].count("T")>0 ):
    hdd=hdda[0]
else:
    hdd=hdda[1]
#idle_screen()
mylcd.lcd_clear()
mylcd.lcd_display_string(direk[1][6:]+" "+direk[2],1)
mylcd.lcd_display_string("  "+hdd+"B Free",2)
print("Ready!")
logging.warning('BANANY swithcing to idle (devurules)')

