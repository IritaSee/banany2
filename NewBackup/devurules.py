import os
import time
lo="sda1"

while 2>1:
    cek=os.system("df /dev/sda1")
    print (cek)
    if cek!=256:
        os.system("sudo python /home/pi/Desktop/siap.py")
        exit()
    time.sleep(0.5)