import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy import ndimage
from PIL import Image

N = 256
filt_core1, filt_core2 = 4, 3
noise = .1

im = np.random.rand(N,N)
im = ndimage.gaussian_filter(im,filt_core1)
im = (im > im.mean()) * 1.
im = ndimage.morphology.binary_erosion(im, structure=np.ones((10,10))) *1.
im = ndimage.morphology.binary_dilation(im, structure=np.ones((10,10))) *1.

im = ndimage.gaussian_filter(im,filt_core2)

#im = ndimage.morphology.grey_erosion(im, structure = np.ones([5,5])) * 1.

im += np.random.rand(N,N) * noise
im = (im / im.max())*255

image = Image.fromarray(np.asarray(im, dtype = np.uint8))
image.save('image.png')

plt.figure()
plt.imshow(im)
plt.show()
