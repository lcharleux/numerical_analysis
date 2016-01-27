# image.py
# Opening image file
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
from scipy import ndimage
import matplotlib.cm as cm
im = Image.open("SiNb.bmp")
z = np.array(im) # image to array
figdir = ''
plt.figure(0)
plt.clf()
grad = plt.imshow(z, cmap = cm.gray)
plt.colorbar(grad)
plt.xticks([])
plt.yticks([])
plt.savefig(figdir+'image_original.png')

# Trace de l'histogramme
n_classes = 64 # Nombre de classes
plt.figure(1)
plt.clf()
plt.hist(z.flatten(), bins=n_classes)
plt.savefig(figdir+'image_hist.png')

# Seuillage de l'image
zs = z<50
plt.figure(2)
plt.clf()
grad = plt.imshow(zs,cmap = cm.gray)
plt.colorbar(grad)
plt.xticks([])
plt.yticks([])
plt.savefig(figdir+'image_threshold.png')


# Erosion
n_ero = 10 # Nombre de passes
ze = zs
for i in xrange(n_ero):
  ze = ndimage.binary_erosion(ze)
plt.figure(3)
plt.clf()
grad = plt.imshow(ze,cmap = cm.gray)
plt.colorbar(grad)
plt.xticks([])
plt.yticks([])
plt.savefig(figdir+'image_erosion.png')

# Dilatation
for i in xrange(n_ero):
  ze = ndimage.binary_dilation(ze)
plt.figure(4)
plt.clf()
grad = plt.imshow(ze,cmap = cm.gray)
plt.colorbar(grad)
plt.xticks([])
plt.yticks([])
plt.savefig(figdir+'image_dilation.png')

# Labeling
zl, nombre = ndimage.label(ze)
plt.figure()
plt.clf()
grad = plt.imshow(zl)
plt.colorbar(grad)
plt.xticks([])
plt.yticks([])
plt.savefig(figdir+'image_labels.png')

# Comptage
surface_dendrite = float(ze.sum())
surface_totale = float(np.size(ze))
taille_moyenne = surface_dendrite / nombre
proportion = surface_dendrite / surface_totale
 

