#----------------------------------------------------
# Creation d'une image monochrome a partir d'une photographie
#----------------------------------------------------

# PACKAGES
from PIL import Image # On charge Python Image Library
import numpy as np    # On charge Numpy 
from matplotlib import pyplot as plt # On charge pyplot (un sous module de Matplotlib) et on le renomme plt
from matplotlib import cm

# LECTURE IMAGE
im = Image.open('lapin.jpg') # PIL permet de lire tous les formats d'images
rouge, vert, bleu = im.split()
R = np.array(rouge).astype(np.float64) # On cree des matrices contenant les informations de chaque canal sous forme de flotants.
V = np.array(vert).astype(np.float64)
B = np.array(bleu).astype(np.float64)

# CONSTRUCTION IMAGE MONOCHROME
#Z = V**2# On cree un combinaison des canaux R, V et B qu'on nomme Z
Z = V

# AFFICHAGE IMAGE
fig = plt.figure(0) # On cree une figure
plt.clf()
plt.imshow(Z, cmap = cm.jet, interpolation = 'nearest')
cbar = plt.colorbar()
cbar.set_label('Echelle $Z$')
plt.xlabel('$i$')
plt.ylabel('$j$')
plt.title('$Z_{ij}$')
plt.show()
