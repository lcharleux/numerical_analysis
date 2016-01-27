from PIL import Image 
import numpy as np   
from matplotlib import pyplot as plt 
from matplotlib import cm
im = Image.open('../data/grenouille.jpg') 
rouge, vert, bleu = im.split()
z = np.array(rouge)
ny, nx = z.shape
cx, cy = 200, 250
zc = z[cx:-cx, cy:-cy]
nyc, nxc = zc.shape

fig = plt.figure(0) # On cree une figure
plt.clf()
ax1 =fig.add_subplot(3,1,1)
plt.imshow(z, origin = "upper")
plt.xticks([0, nx])
plt.yticks([0, ny])
ax2 =  fig.add_subplot(3,1,2)
plt.imshow(zc,  origin = "upper", interpolation = "nearest")
plt.xticks([0, nxc])
plt.yticks([0, nyc])
plt.show()


