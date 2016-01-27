#----------------------------------------------------
# Histogramme d'altitude de l'Europe
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







# AFFICHAGE
n_classes = 10                                   # Nombre de classes
fig = plt.figure()
fig.add_subplot(121)
plt.title('Hisogramme') 
plt.ylabel('Surfaces $km^2$')                    # On specifie le label en y
plt.hist(Z.flatten(), bins=n_classes)            # Histogramme
fig.add_subplot(122)
plt.title('Hisogramme cumule') 
plt.hist(Z.flatten(), bins=n_classes, cumulative=True) # Histogramme cumule
plt.xlabel('Altitudes $m$')                      # On specifie le label en x


plt.show()                       # On affiche l'image

