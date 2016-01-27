#----------------------------------------------------
# Erosion - Dilatation de l'Europe
#----------------------------------------------------


# PACKAGES
from PIL import Image # On charge Python Image Library
import numpy as np    # On charge Numpy 
from matplotlib import pyplot as plt # On charge pyplot (un sous module de Matplotlib) et on le renomme plt
from scipy.ndimage import morphology # Module de morphologie mathematique de Scipy
from matplotlib import cm

# TRAITEMENT IMAGE
im = Image.open('europe.tif')           # PIL permet de lire tous les formats d'images
Nx, Ny = im.size                        # On reduit la definition de l'image
im = im.resize((Nx/10, Ny/10), Image.ANTIALIAS)
Z = np.array(im).astype(np.float64)     # On convertir l'image en array 

max_altitude = 1000.                    # Altitude maximale en metres, cette donnee est un peu douteuse, (a confirmer).
Z = Z / Z.max() * max_altitude          # On recale les altitudes 


Z = np.where(Z > 0., 1., 0.) # La fonction np.where permet d'appliquer un test booleen a chaque pixel et de specifier la reponse.

structure = np.ones([30,30]) # On definit l'element structurant
Ze = morphology.binary_erosion(Z, structure = structure) + 0.    # On applique l'erosion
Zed = morphology.binary_dilation(Ze, structure = structure) + 0. # On applique l'erosion

# AFFICHAGE
fig = plt.figure()
fig.add_subplot(131)
plt.title('S = ${0:1.2e} \; km^2$'.format(Z.sum()))
plt.imshow(Z, interpolation = 'nearest', cmap= cm.gray)
fig.add_subplot(132)
plt.title('S = ${0:1.2e} \; km^2$'.format(Ze.sum()))
plt.imshow(Ze, interpolation = 'nearest', cmap= cm.gray)
fig.add_subplot(133)
plt.title('S = ${0:1.2e} \; km^2$'.format(Zed.sum()))
plt.imshow(Zed, interpolation = 'nearest', cmap= cm.gray)
plt.show()         

