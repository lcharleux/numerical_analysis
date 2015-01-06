
#----------------------------------------------------
# Carte d'altitude de l'Europe
#----------------------------------------------------


# PACKAGES
from PIL import Image # On charge Python Image Library
import numpy as np    # On charge Numpy 
from matplotlib import pyplot as plt # On charge pyplot (un sous module de Matplotlib) et on le renomme plt

# TRAITEMENT IMAGE
im = Image.open('europe.tif')           # PIL permet de lire tous les formats d'images
Nx, Ny = im.size                        # On reduit la definition de l'image
im = im.resize((Nx/10, Ny/10), Image.ANTIALIAS)
Z = np.array(im).astype(np.float64)     # On convertir l'image en array 
max_altitude = 1000.                    # Altitude maximale en metres, cette donnee est un peu douteuse, (a confirmer).
Z = Z / Z.max() * max_altitude          # On recale les altitudes 

# AFFICHAGE
plt.figure(0)
plt.clf()
plt.imshow(Z)                    # Affichage de l'altitude
cbar = plt.colorbar()            # Ajout d'une barre d'echelle
cbar.set_label('Altitude $m$')   # On specifie le label en z
plt.xlabel('$x 10 km$')   # On specifie le label en x
plt.ylabel('$x 10 km$')   # On specifie le label en y
plt.title('Altitudes en Europe') # On specifie le titre
plt.show()                       # On affiche l'image

