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
zsd = ndimage.morphology.binary_dilation(zse, structure=np.ones((3,3)))              
fig = plt.figure()
plt.clf()
fig.add_subplot(2, 1, 1)
plt.imshow(zse, origin = "upper", cmap = cm.gray)
plt.colorbar()
fig.add_subplot(2, 1, 2)
plt.imshow(zse, origin = "upper", cmap = cm.gray)
plt.colorbar()
plt.show()                       

