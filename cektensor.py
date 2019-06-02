import tensorflow as tf
versi=tf.__version__
halo=tf.constant('hello, library tensorflow sudah ter install dengan versi: '+versi)
sesi=tf.Session()
print(sesi.run(halo))
