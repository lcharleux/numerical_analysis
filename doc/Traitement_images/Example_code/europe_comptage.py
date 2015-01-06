#----------------------------------------------------
# Comptage des iles et continents
#----------------------------------------------------


# PACKAGES
from PIL import Image # On charge Python Image Library
import numpy as np    # On charge Numpy 
from matplotlib import pyplot as plt # On charge pyplot (un sous module de Matplotlib) et on le renomme plt
from scipy.ndimage import morphology # Module de morphologie mathematique de Scipy
from scipy.ndimage import measurements # Module de morphologie mathematique de Scipy


# TRAITEMENT IMAGE
im = Image.open('europe.tif')           # PIL permet de lire tous les formats d'images
Nx, Ny = im.size                        # On reduit la definition de l'image
im = im.resize((Nx/5, Ny/5), Image.ANTIALIAS)
Z = np.array(im).astype(np.float64)     # On convertir l'image en array 

max_altitude = 1000.                    # Altitude maximale en metres, cette donnee est un peu douteuse, (a confirmer).
Z = Z / Z.max() * max_altitude          # On recale les altitudes 


Z = np.where(Z > 0., 1., 0.) # La fonction np.where permet d'appliquer un test booleen a chaque pixel et de specifier la reponse.

# EROSION / DILATATION
structure = np.ones([10,10]) # On definit l'element structurant
Z = morphology.binary_erosion(Z, structure = structure) + 0.    # On applique l'erosion
Z = morphology.binary_dilation(Z, structure = structure) + 0. # On applique l'erosion

# COMPTAGE
Zl, nombre = measurements.label(Z) # On compte les zones

# ISOLEMENT D'UNE ZONE
zone = 5 # Label de la zone a isoler
Zli = np.where(Zl == zone, 1, np.nan) # On masque la mer

# AFFICHAGE
fig = plt.figure(0)
plt.clf()
fig.add_subplot(131)
plt.title('Image initiale')
plt.imshow(Z, interpolation = 'nearest')
fig.add_subplot(132)
plt.title('Comptage: {0} zones'.format(nombre))
plt.imshow(np.where(Zl == 0, np.nan, Zl), interpolation = 'nearest')
fig.add_subplot(133)
plt.title('Zone {0} isolee'.format(zone))
plt.imshow(Zli, interpolation = 'nearest')
plt.show()         

