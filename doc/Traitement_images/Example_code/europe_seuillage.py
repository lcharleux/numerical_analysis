#----------------------------------------------------
# Recherche des zones marines par seuillage
#----------------------------------------------------


# PACKAGES
from PIL import Image # On charge Python Image Library
import numpy as np    # On charge Numpy 
from matplotlib import pyplot as plt # On charge pyplot (un sous module de Matplotlib) et on le renomme plt

# TRAITEMENT IMAGE
im = Image.open('europe.tif')           # PIL permet de lire tous les formats d'images
Nx, Ny = im.size                        # On reduit la definition de l'image
im = im.resize((Nx/5, Ny/5), Image.ANTIALIAS)
Z = np.array(im).astype(np.float64)     # On convertir l'image en array 
max_altitude = 1000.                    # Altitude maximale en metres, cette donnee est un peu douteuse, (a confirmer).
Z = Z / Z.max() * max_altitude          # On recale les altitudes 

Z = np.where(Z > 200., 1., 0.) # La fonction np.where permet d'appliquer un test booleen a chaque pixel et de specifier la reponse.

# AFFICHAGE
plt.figure()
plt.clf()
plt.imshow(Z)                    # Affichage de l'altitude
plt.colorbar()
plt.xlabel('$km$')   # On specifie le label en x
plt.ylabel('$km$')   # On specifie le label en y
plt.title('Zones marines') # On specifie le titre
plt.show()                       # On affiche l'image

