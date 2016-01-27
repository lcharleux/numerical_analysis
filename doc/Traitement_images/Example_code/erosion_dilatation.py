import numpy as np    # On charge Numpy 
from matplotlib import pyplot as plt # On charge pyplot (un sous module de Matplotlib) et on le renomme plt
from scipy.ndimage import morphology # Module de morphologie mathematique de Scipy


# On construit un cas test
N_pixels = 20
x = np.linspace(0., 1., N_pixels)
X, Y = np.meshgrid(x, x)
Za = np.where((X-.25)**2 + (Y-.25)**2 < .2**2, 1., 0.)
Zb = np.where((X-.75)**2 + (Y-.75)**2 < .05**2, 1., 0.)
Z = Za + Zb

# On applique l'erosion et la dilatation
structure = np.ones([3,3]) # On definit l'element structurant
Ze = morphology.binary_erosion(Z, structure = structure) + 0.    # On applique l'erosion
Zed = morphology.binary_dilation(Ze, structure = structure) + 0. # On applique l'erosion
fig = plt.figure()
plt.clf()
fig.add_subplot(131)
plt.title('Gros et petit objet')
plt.imshow(Z, interpolation = 'nearest')
fig.add_subplot(132)
plt.title('Erosion')
plt.imshow(Ze, interpolation = 'nearest')
fig.add_subplot(133)
plt.title('Erosion + Dilatation')
plt.imshow(Zed, interpolation = 'nearest')
plt.show()
