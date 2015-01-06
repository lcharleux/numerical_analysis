#----------------------------------------------------
# Decomposition d'une image a polychrome en 3 canaux
#----------------------------------------------------

# PACKAGES
from PIL import Image # On charge Python Image Library
import numpy as np    # On charge Numpy 
from matplotlib import pyplot as plt # On charge pyplot (un sous module de Matplotlib) et on le renomme plt

# LECTURE IMAGE
im = Image.open('lapin.jpg') # PIL permet de lire tous les formats d'images
rouge, vert, bleu = im.split()

# AFFICHAGE IMAGE
fig = plt.figure() # On cree une figure
fig.add_subplot(221) # On cree une sous figure
plt.xticks([]) 
plt.yticks([])
plt.imshow(im,origin='lower')
plt.title('RVB')
fig.add_subplot(222) # On cree une sous figure
plt.xticks([])
plt.yticks([])
plt.imshow(rouge,origin='lower')
plt.title('Canal Rouge')
fig.add_subplot(223) # On cree une sous figure
plt.xticks([])
plt.yticks([])
plt.imshow(vert,origin='lower')
plt.title('Canal Vert')
fig.add_subplot(224) # On cree une sous figure
plt.xticks([])
plt.yticks([])
plt.imshow(bleu,origin='lower')
plt.title('Canal Bleu')
plt.show()
