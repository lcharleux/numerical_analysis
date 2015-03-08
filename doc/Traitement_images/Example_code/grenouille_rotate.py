from PIL import Image 
import numpy as np   
from matplotlib import pyplot as plt 
from matplotlib import cm
from scipy import ndimage
im = Image.open('../data/grenouille.jpg') 
rouge, vert, bleu = im.split()
z = np.array(rouge)
zrr = ndimage.rotate(z, 30.) 
zrn = ndimage.rotate(z, 30.,
  reshape = False) 

ny, nx = z.shape
nyrr, nxrr = zrr.shape
nyrn, nxrn = zrn.shape

fig = plt.figure(0) # On cree une figure
plt.clf()
ax1 =fig.add_subplot(3,1,1)
plt.imshow(z, origin = "upper")
plt.xticks([0, nx])
plt.yticks([0, ny])
ax2 =  fig.add_subplot(3,1,2)
plt.imshow(zrr,  origin = "upper")
plt.xticks([0, nxrr])
plt.yticks([0, nyrr])
ax2 =  fig.add_subplot(3,1,3)
plt.imshow(zrn,  origin = "upper")
plt.xticks([0, nxrn])
plt.yticks([0, nyrn])
plt.show()


