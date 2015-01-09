#----------------------------------------------------
# Histogramme d'une image
#----------------------------------------------------


# PACKAGES
from PIL import Image # On charge Python Image Library
import numpy as np    # On charge Numpy 
from matplotlib import pyplot as plt # On charge pyplot (un sous module de Matplotlib) et on le renomme plt

# TRAITEMENT IMAGE
im = Image.open('image.png')           # PIL permet de lire tous les formats d'images
channels = im.split()
Z = np.array(channels[0])              # On convertir l'image en array 
Nx, Ny = Z.shape                       # On determine les dimensions de l'image

# AFFICHAGE
n_classes = Nx                         # Nombre de classes
fig = plt.figure()
plt.title('Hisogramme') 
plt.ylabel('Pixels')                   # On specifie le label en y
plt.xlabel('Valeurs des pixels')       # On specifie le label en x
plt.hist(Z.flatten(), bins=n_classes, histtype = "step")            # Histogramme
plt.grid()
plt.show()                       # On affiche l'image

