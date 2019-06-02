import os
import time
lo="sda1"
#os.popen("sudo python3 /home/pi/Desktop/w8.py")
while 2>1:
    cek=os.system("df /dev/sda1")
    print (cek)
    if cek!=256:
        os.system("sudo python3 /home/pi/Desktop/siap.py")
        exit()
    time.sleep(0.5)