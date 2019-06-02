print ("BANANY Console Ver 0.1")
import os
import shutil
import datetime

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
temp = chr(penghitung)
#namafile=....
asal = "/media/pi/6461-6131/DCIM" #yep ini targetnya , kita harus segera adaptasi var. asal
print("backup target: "+asal)
tempat = "/media/pi/Narendra/BANANY_%s" % datetime.datetime.now().date() + temp
while os.path.exists(tempat):
    #os.makedirs(tempat)
    penghitung = penghitung + 4
    temp = chr(penghitung)
    tempat = "/media/pi/Narendra/BANANY_%s" % datetime.datetime.now().date() + temp
#while os.path.exists(asal+"/"+namafile): manual way
   #yang dibawah tab dulu kalo mau dipake sm while nya
#os.makedirs(tempat)
print(tempat+" setted as destination")
print ("Copying...")
try:
    shutil.copytree(asal, tempat)
except shutil.Error as e:
    print("Error: %s" % e)
    print("backup failed and canceled")
except IOError as e:
    print ("Error: %s" % e.strerror)
    print ("backup failed and canceled")
    
print ("process from "+asal+" to "+tempat+" complete")
    #target = tempat+"/"+namafile
    #os.rename(asal+"/"+namafile, target)
    #namafile=#update

#lowvolt speed 1.893MBps
#lowvolt Optimized: 3.1976744MBps, udah 2x test same result
#cek da name, kesalahan terletak pada corrupted file, bila sebuah transfer gagal dengan nama yang sama...
#maka untuk transfer selanjutnya yang pake nama tsb akan error dengan errno 5
