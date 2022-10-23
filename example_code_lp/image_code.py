"""

import numpy as numpy
import matplotlib.pyplot as plt 

lines = 5401
samples = 600
bands = 2048
path = "cube.bip"

band_r = 400
band_g = 600
band = 800

data = numpy.fromfile(path, count=lines*bands*samples, dtype='uint16')

data.shape = (lines, samples, bands)
data_rgb = numpy.zeros()

plt.imshow(data[:,:,[400, 600, 800]]/16)
plt.show()

"""

import numpy as np
import matplotlib.pyplot as plt

lines = 1000
samples = 600
bands = 2048
s
path = 'cube.bip'
data = np.fromfile(path, count=lines*bands*samples, dtype='uint16')

data.shape = (lines, samples, bands)

band_r = 400
band_g = 600
band_b = 800

data_rgb = np.zeros([lines, samples, 3], dtype='uint8')

data_rgb[:,:,0] = data[:,:,band_r]/16
data_rgb[:,:,1] = data[:,:,band_g]/16
data_rgb[:,:,2] = data[:,:,band_b]/16

plt.imshow(data_rgb)
plt.show()
