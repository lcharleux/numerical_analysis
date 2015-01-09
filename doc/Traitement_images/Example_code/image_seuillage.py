#----------------------------------------------------
# Recherche des zones marines par seuillage
#----------------------------------------------------


# PACKAGES
from PIL import Image # On charge Python Image Library
import numpy as np    # On charge Numpy 
from matplotlib import pyplot as plt # On charge pyplot (un sous module de Matplotlib) et on le renomme plt
from matplotlib import cm


# TRAITEMENT IMAGE
im = Image.open('image.png')           # PIL permet de lire tous les formats d'images
channels = im.split()
Z = np.array(channels[0])              # On convertir l'image en array 

Z = Z > 120 # La fonction np.where permet d'appliquer un test booleen a chaque pixel et de specifier la reponse.

# AFFICHAGE
plt.figure()
plt.clf()
plt.imshow(Z, cmap = cm.gist_yarg)                    # Affichage de l'altitude
plt.colorbar()
plt.grid()
plt.xlabel('pixels')   # On specifie le label en x
plt.ylabel('pixels')   # On specifie le label en y
plt.show()                       # On affiche l'image

