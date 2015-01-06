# PACKAGES
import numpy as np
from matplotlib import pyplot as plt # On import pyplot (un sous module de Matplotlib) et on le renomme plt

# FONCTIONS
def ma_fonction(x,y):
  '''
  Une fonction a tracer.
  '''
  return np.sin(np.pi * 2 *x) * np.sin(np.pi * 2 *y) / (x**2 + y**2)**.5
  

# DEFINITIONS DIVERSES  
x = np.linspace(1., 5., 100) # On demande un array contenant 100 points equirepartis entre 0 et 5.
y = np.linspace(1., 5., 100) 
X, Y = np.meshgrid(x,y) # On cree des grilles X, Y qui couvrent toutes les combinaisons de x et de y
Z = ma_fonction(X, Y) # Grace a numpy, on applique la fonction a tous les points x d'un coup

# TRACE DE LA COURBE
niveaux = 20 
fig = plt.figure() # On cree une figure
plt.clf()          # On purge la figure
plt.contourf(X, Y, Z, niveaux)
cbar = plt.colorbar()
plt.contour(X, Y, Z, niveaux, colors = 'black')

cbar.set_label('Z')
plt.xlabel('$X$')    # On definit le label de l'axe x
plt.ylabel('$Y$')
plt.grid()         # On demande d'avoir une grille
plt.title(r'$z = \sin (2 \pi x) \sin (2 \pi y) / \sqrt{x^2 + y^2}$') # On definit le titre et on utilise la syntaxe de LaTeX pour y introduire des maths.
plt.show()

