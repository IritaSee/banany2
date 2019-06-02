import RPi_I2C_driver
import os
from time import *
def out_ke_lcd():
    mylcd = RPi_I2C_driver.lcd()
    # test 2
    mylcd.lcd_clear()
    mylcd.lcd_display_string("  BANANY READY ",1)
    mylcd.lcd_display_string("----WELCOME!----",2)
    sleep(3)
    mylcd.lcd_clear()
    mylcd.lcd_display_string("WiFi:BANANY01",1)
    mylcd.lcd_display_string("PWD:bananybanany",2)
    sleep(3)

def idle_screen():
    mylcd = RPi_I2C_driver.lcd()
    mylcd.lcd_clear()
    mylcd.lcd_display_string(direk[2],1)
    mylcd.lcd_display_string(hdd+"B Free",2)

    
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
os.system("sudo systemctl stop nyala.service")
os.system("sudo systemctl start devurules.service")
#fungsi out ke lcd sementara dipadamkan karena lagi rusak
out_ke_lcd()
sleep(3)
#   sd=os.popen("sudo df /dev/sda1").read().split()[-2]
  #  print sd
direk=os.popen("sudo df /dev/"+cekpar+" -h").read().split()[-3:]
hdda=os.popen("sudo df /dev/"+cekpar+" -h").read().split()[-4:]
print (hdda) 
if(hdda[0].count("G")>0 or hdda[0].count("T")>0 ):
    hdd=hdda[0]
else:
    hdd=hdda[1]
idle_screen()
sleep(2)
print("Ready!")
