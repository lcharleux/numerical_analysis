from PIL import Image 
import numpy as np   
from matplotlib import pyplot as plt 
from scipy import ndimage
im = Image.open('../data/grenouille.jpg') 
rouge, vert, bleu = im.split()
z =  ndimage.gaussian_filter(np.array(rouge), 4)
# Sharpen
k = .5
zs1 = z + k * (z - ndimage.gaussian_filter(z, 1.))
zs2 = z + k * (z - ndimage.gaussian_filter(z, 2.))

fig = plt.figure(0) # On cree une figure
plt.clf()
ax1 =fig.add_subplot(3,1,1)
plt.imshow(z, origin = "upper")
plt.xticks([])
plt.yticks([])
plt.ylabel("Raw (blurred)")
ax2 =  fig.add_subplot(3,1,2)
plt.imshow(zs1,  origin = "upper")
plt.xticks([])
plt.yticks([])
plt.ylabel("Sharpened")
ax2 =  fig.add_subplot(3,1,3)
plt.imshow(zs2,  origin = "upper")
plt.xticks([])
plt.yticks([])
plt.ylabel("Sharpened")
plt.show()
