import os
asd='/Users/iganarendra/Desktop/BANANY_TEST_FILE'
alamat=asd+"/DCIM"
def get_size(start_path = alamat+'/'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size/1000000
#MADE IT MEGABYTES
a=round(get_size()/1000,2)
s="hop"

#if (a>1000):
#    a=a/1000
print(s,a)
#print(get_size()/13.128)
print(get_size()/11.5)
