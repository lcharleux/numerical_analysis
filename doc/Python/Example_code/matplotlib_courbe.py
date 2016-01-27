# PACKAGES
import numpy as np
from matplotlib import pyplot as plt # On import pyplot (un sous module de Matplotlib) et on le renomme plt

# FONCTIONS
def ma_fonction(x):
  '''
  Une fonction a tracer.
  '''
  return np.sin(2 * np.pi * x ) / x
  

# DEFINITIONS DIVERSES  
x = np.linspace(0., 5., 500) # On demande un array contenant 100 points equirepartis entre 0 et 5.
y = ma_fonction(x) # Grace a numpy, on applique la fonction a tous les points x d'un coup

# TRACE DE LA COURBE
fig = plt.figure() # On cree une figure
plt.clf()          # On purge la figure
plt.plot(x, y, 'b-', linewidth = 2.)     # On trace y en fonction de x
plt.xlabel('$x$')    # On definit le label de l'axe x
plt.ylabel('$y$')
plt.grid()         # On demande d'avoir une grille
plt.title(r'$y = \sin (2 \pi x) / x$') # On definit le titre et on utilise la syntaxe de LaTeX pour y introduire des maths.
plt.show()

