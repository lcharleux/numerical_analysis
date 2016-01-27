import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from PIL import Image
N = 256
filt_core1, filt_core2 = 4, 2
noise = .05
im = np.random.rand(N,N)
im = ndimage.gaussian_filter(im,filt_core1)
im = (im > im.mean()) * 1.
im = ndimage.morphology.binary_erosion(im, structure=np.ones((10,10))) *1.
im = ndimage.morphology.binary_dilation(im, structure=np.ones((10,10))) *1.
im = ndimage.gaussian_filter(im,filt_core2)
im = (im - im.min()) / (im.max() - im.min()) * 255
im = np.where(np.random.rand(N, N) > .95, 255, im)
image = Image.fromarray(np.asarray(im, dtype = np.uint8))
image.save('image.jpg')

plt.figure()
plt.imshow(im)
plt.colorbar()
plt.show()
