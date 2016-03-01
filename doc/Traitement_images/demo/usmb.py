from PIL import Image 
import numpy as np   
from matplotlib import pyplot as plt 
from scipy import ndimage, misc
from matplotlib import cm
im = Image.open('usmb.jpg') 


R, V, B = im.split()
Z = np.array(R)


"""
fig = plt.figure("Greyscale") 
plt.clf()
plt.imshow(Z, origin = "upper", cmap = cm.terrain)
plt.colorbar()
plt.grid()

# Histogramme
fig = plt.figure("Histogram") 
plt.clf()
plt.hist(Z.flatten(), bins = 256)
plt.grid()
"""

Z = Z < 70.
fig = plt.figure("Seuillage") 
plt.clf()
plt.imshow(Z, origin = "upper", cmap = cm.binary)
plt.colorbar()
plt.grid()

# Erosion + dilatation
n = 5
Ze = ndimage.morphology.binary_erosion(Z, structure = np.ones((n,n)))
Zd = ndimage.morphology.binary_dilation(Ze, structure = np.ones((n,n)))
"""
fig = plt.figure("Erosion/Dilatation") 
plt.clf()
ax = fig.add_subplot(1,3,1)
plt.imshow(Z, origin = "upper", cmap = cm.binary)
plt.grid()
ax = fig.add_subplot(1,3,2)
plt.imshow(Ze, origin = "upper", cmap = cm.binary)
plt.grid()
ax = fig.add_subplot(1,3,3)
plt.imshow(Zd, origin = "upper", cmap = cm.binary)
plt.grid()
"""
R *= Zd
fig = plt.figure("Greyscale") 
plt.clf()
plt.imshow(R, origin = "upper", cmap = cm.gray)
plt.colorbar()
plt.grid()


plt.show()
