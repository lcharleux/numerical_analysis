#------------------------------------------------------------------------
# RECHERCHE DU CHEMIN LE PLUS RAPIDE ENTRE 2 POINTS A ET B
#------------------------------------------------------------------------

#------------------------------------------------------------------------
# PACKAGES
from scipy import optimize as opt # Optimize
import numpy as np                # Numpy
import matplotlib.pyplot as plt   # Pyplot
from matplotlib import cm         # Colormaps
#------------------------------------------------------------------------

#------------------------------------------------------------------------
# POSITION DES POINTS ET DONNEES PHYSIQUES
xa, xb = 0., 1.
ya, yb = 1., 0.
m = 1.  # masse en kg
g = 10. # gravite en ms**-2
#------------------------------------------------------------------------

#------------------------------------------------------------------------

#------------------------------------------------------------------------
# MAILLAGE EN X 
Np = 30 # Nombre de noeuds souhaites
X = np.linspace(xa, xb, Np) # Coordonnees en x des noeuds
#------------------------------------------------------------------------

#------------------------------------------------------------------------
# PROPOSITION D'UNE SOLUTION INTUITIVE: LA LIGNE DROITE 
Y = ya + (yb - ya) / (xb - xa) * X # Altitude des noeuds
#------------------------------------------------------------------------

#------------------------------------------------------------------------
# CALCUL DU TEMPS DE PARCOURS
def temps(Y):
  # On calcule l'energie potentielle en supposant qu'elle est nulle en A
  Ep = m * g * (Y - Y[0])
  # On calcule l'energie cinetique (via le theoreme de l'energie cinetique integre)
  Ec = - Ep
  # On calcule la vitesse
  V = (2. / m * Ec) **.5 
  # On calcule la vitesse moyenne sur chaque element
  Ve = (V[1:] + V[:-1]) / 2.
  # On calcule le pas en X:
  dx = X[1] - X[0]
  # On calcule la longueur de chaque element
  Le = ( ( Y[1:] - Y[:-1] )**2 + dx**2)**.5
  # On calcule le temps de parcours par element
  te = Le / Ve
  # On calcule le temps de parcours total
  t = te.sum()
  return t, V
#------------------------------------------------------------------------
 

#------------------------------------------------------------------------
# MISE EN APPLICATION
t, V = temps(Y)  
#------------------------------------------------------------------------

#------------------------------------------------------------------------
# AFFICHAGE
fig = plt.figure(0)
ax = fig.add_subplot(211)
plt.title('Temps de parcours: $t = {0:.2f} s$'.format(t))
plt.ylabel('Altitude $Y$')
plt.plot(X, Y)
plt.grid()
ax = fig.add_subplot(212)
plt.xlabel('Position $X$')
plt.ylabel('Vitesse $V$')
plt.plot(X, V)
plt.grid()
plt.show()
#------------------------------------------------------------------------



  