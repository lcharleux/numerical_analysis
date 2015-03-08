from PIL import Image 
import numpy as np    
from matplotlib import pyplot as plt
from matplotlib import cm 
im = Image.open('../Slides/figures/image.jpg')           
channels = im.split()
z = np.array(channels[0])              
seuil = 150.
zs = z > seuil              
fig = plt.figure()
plt.clf()
fig.add_subplot(2, 1, 1)
plt.imshow(z, origin = "upper")
plt.colorbar()
fig.add_subplot(2, 1, 2)
plt.imshow(zs, origin = "upper", cmap = cm.gray)
plt.colorbar()
plt.show()                       

