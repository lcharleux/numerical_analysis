from PIL import Image 
import numpy as np    
from matplotlib import pyplot as plt
from matplotlib import cm 
from scipy import ndimage
im = Image.open('../Slides/figures/image.jpg')           
channels = im.split()
z = np.array(channels[0])              
seuil = 150.
zs = z > seuil 
zse = ndimage.morphology.binary_erosion(zs, structure=np.ones((3,3))) 
zsd = np.float64(ndimage.morphology.binary_erosion(zse, structure=np.ones((3,3))))              
zgx = ndimage.sobel(zsd, axis=0, mode='constant')
zgy = ndimage.sobel(zsd, axis=1, mode='constant')
zsob = np.hypot(zgx, zgy)
fig = plt.figure()
plt.clf()
fig.add_subplot(2, 1, 1)
plt.imshow(zsd, origin = "upper", cmap = cm.gray)
plt.colorbar()
fig.add_subplot(2, 1, 2)
plt.imshow(zsob, origin = "upper", cmap = cm.gray)
plt.colorbar()
plt.show()                       

