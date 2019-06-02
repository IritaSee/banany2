import logging
#logging.basicConfig(filename='run.log', level=logging.NOTSET)
print ("..... starting copyer .....")
logging.debug('SD Detected, starting copyer')
print ("currently running: yeyeye.py")
print ("By: Iga Narendra, Nanjaya Satya, Awi Wigraha, Agni Prema, Dwiweka Naratama, 2018")
import os
import shutil
import datetime
import RPi_I2C_driver
import pyfastcopy
from time import *

def copytree (src, dst, symlinks=False, ignore=None):
   # print ("using 2nd library")
    for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks, ignore)
            else:
                shutil.copy2(s, d)


penghitung = 65
errvar=0
mylcd = RPi_I2C_driver.lcd()
temp = chr(penghitung)
#dengan code DIBAWAH jadi tempat sd dan hdd jangan dituker!
sd=os.popen("sudo df /dev/sda1").read().split()[-1]
#gotta solve this part, under me if the partition more than 2
#idea on this part, mainin codes di bawah ini biar bisa support 2 backup drives
#use while loop, like penghitung
cekpar=os.popen("sudo blkid /dev/sdb1").read().split()[3]
cekfool=os.popen("sudo blkid /dev/sdb1").read().split()[4]
if cekpar=='TYPE="ntfs"' or cekfool=='TYPE="ntfs"':
	cekpar='sdb1'
else: 
	cekpar='sdb2'
hdda=os.popen("sudo df /dev/"+cekpar).read().split()[-2:]
if (hdda[0].count("%")>0):
    hdda[0]=''
hdd=hdda[0]+" "+hdda[1]
#hddnew=hdd.replace('LABEL="','')
#hddnew= hddnew.replace('"','');
#hddnew=hdd;
#yak code DIATAS
#asal = "/media/pi/"+sd+"/DCIM" , ini kode lama
asal=sd+"/DCIM"
print("backup target: "+asal)
logging.warning('backup target: {}'.format(asal))
#tempat = "/media/pi/"+hdd+"/BANANY_%s" % datetime.datetime.now().date() + temp
tempat = hdd+"/BANANY2/BANANY_%s" % datetime.datetime.now().date() + temp
while os.path.exists(tempat):
    logging.warning('checking existance: {}'.format(tempat))
    #os.makedirs(tempat)
    penghitung = penghitung + 1
    temp = chr(penghitung)
    #tempat = "/media/pi/"+hdd+"/BANANY_%s" % datetime.datetime.now().date() + temp
    tempat = hdd+"/BANANY2/BANANY_%s" % datetime.datetime.now().date() + temp
#while os.path.exists(asal+"/"+namafile): manual way
   #yang dibawah tab dulu kalo mau dipake sm while nya
#os.makedirs(tempat)

print(tempat+" setted as destination")
logging.warning('{} setted as destination'.format(tempat))
def get_size(start_path = asal+"/"):
	total_size=0
	for dirpath, dirnames, filenames in os.walk(start_path):
		for f in filenames:
			fp= os.path.join(dirpath, f)
			total_size+= os.path.getsize(fp)
	return total_size/1000000
mylcd.lcd_clear()
uku=get_size()
if (uku>1000):
	kur=str(round(uku/1000,2))
	mylcd.lcd_display_string("Copying "+kur+"GB",1)
else:
	kur=str(round(uku,2))
	mylcd.lcd_display_string("Copying "+kur+"MB",1)
mylcd.lcd_display_string("to: %s/"% datetime.datetime.now().date()+temp,2)
sleep(4)
esttime=uku/11.0
mylcd.lcd_clear()
mylcd.lcd_display_string("ETA: "+str(round(esttime,2)),1)
mylcd.lcd_display_string("Seconds",2)
print ("Copying...")
logging.warning('copying {} to destination, ETA {} secs'.format(uku,round(esttime,4)))
try:
    shutil.copytree(asal, tempat)
except shutil.Error as e:
    print("Error: %s" % e)
    logging.error('%s' %e)
    print("backup failed and canceled")
    errvar=errvar+1
except IOError as e:
    print ("Error: %s" % e.strerror)
    logging.error('%s' %e.strerror)
    print ("backup failed and canceled")
    errvar=errvar+1

print ("ejecting SD, 2s delay")
mylcd.lcd_clear()
mylcd.lcd_display_string("BACKUP SUCCESS", 1)
mylcd.lcd_display_string("Ejecting.", 2)
sleep(0.5)
mylcd.lcd_display_string("Ejecting..",2)
sleep(0.5)
mylcd.lcd_display_string("Ejecting...",2)
sleep(0.5)
mylcd.lcd_display_string("Ejecting....",2)
sleep(0.5)
print ("error value: ")
print (errvar)
print ("process from "+asal+" to "+tempat+" complete")
logging.warning('process from {} to {} complete'.format(asal,tempat))
mylcd.lcd_clear()
if errvar <1:
    mylcd.lcd_display_string("BACKUP SUCCESS", 1)
    mylcd.lcd_display_string("Remove SDCard!", 2)
    mylcd.backlight(0)
    sleep(1)
    mylcd.backlight(1)
    sleep(1)
    mylcd.backlight(0)
    sleep(1)
    print("backup success, ...")
    mylcd.backlight(1)
    sleep(1)
    mylcd.backlight(0)
    sleep(1)
    mylcd.backlight(1)
    os.popen("sudo umount "+sd)
    logging.warning('unmounting sd card')
    os.system ("sudo systemctl stop nyala.service")
    logging.warning('nyala.service should stop')
    exit()
    
if errvar >0:
    print("backup error")
    mylcd.lcd_display_string("%s"%e.strerror, 1)
    mylcd.lcd_display_string("Open myBANANY", 2)
    mylcd.backlight(0)
    sleep(0.3)
    mylcd.backlight(1)
    sleep(0.3)
    mylcd.backlight(0)
    sleep(0.3)
    mylcd.backlight(1)
    sleep(0.3)
    mylcd.backlight(0)
    sleep(0.3)
    mylcd.backlight(1)
    sleep(0.3)
    mylcd.backlight(0)
    sleep(0.3)
    mylcd.backlight(1)
    os.popen("sudo umount "+sd)
    logging.error('sd unmounted with an error, nyala.service should stop')
    os.system ("sudo systemctl stop nyala.service")
    exit()
    

#script baru untuk unmount sdcard
    #target = tempat+"/"+namafile
    #os.rename(asal+"/"+namafile, target)
    #namafile=#update
    #take a research soal hubungan berbanding terbalik volt dan oc
    #serta hubungan berbanding lurus speed dan oc
#normal w/ flashdrive as test bisa 56 secs half gigs of random files
#lowvolt speed 1.893MBps
#lowvolt Optimized: 3.1976744MBps, udah 2x test same result
#cek da name, kesalahan terletak pada corrupted file, bila sebuah transfer gagal dengan nama yang sama...
#maka untuk transfer selanjutnya yang pake nama tsb akan error dengan errno 5


#PALING BARU: GAADA ISTILAH LOWVOLT, SPEED DISAMAKAN
