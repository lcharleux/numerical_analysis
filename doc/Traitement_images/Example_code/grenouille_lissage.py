from PIL import Image 
import numpy as np   
from matplotlib import pyplot as plt 
from scipy import ndimage
im = Image.open('../data/grenouille.jpg') 
rouge, vert, bleu = im.split()
z = np.array(rouge)
# Blur
zg10 = ndimage.gaussian_filter(z, 10.)
# Blur more !
zg30 = ndimage.gaussian_filter(z, 30.)

fig = plt.figure(0) # On cree une figure
plt.clf()
ax1 =fig.add_subplot(3,1,1)
plt.imshow(z, origin = "upper")
plt.xticks([])
plt.yticks([])
plt.ylabel("Raw")
ax2 =  fig.add_subplot(3,1,2)
plt.imshow(zg10,  origin = "upper")
plt.xticks([])
plt.yticks([])
plt.ylabel("Blurred")
ax2 =  fig.add_subplot(3,1,3)
plt.imshow(zg30,  origin = "upper")
plt.xticks([])
plt.yticks([])
plt.ylabel("Blurred more !")
plt.show()
