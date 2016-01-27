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
xa, xb = 0., 5.
ya, yb = 1., 0.
m = 1.  # masse en kg
g = 10. # gravite en ms**-2
#------------------------------------------------------------------------

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
  return t
  
def add_AB(Yc):
  Y = np.zeros([len(Yc) + 2])
  Y[1:-1] = Yc
  Y[0], Y[-1] = ya, yb
  return Y

def temps2(Yc):
  return temps(add_AB(Yc))  
#------------------------------------------------------------------------
 

#------------------------------------------------------------------------
# MISE EN APPLICATION

manual = False # Mode de fonctionnement: True pour manuel, False pour automatique

# MAILLAGE EN X 
Np = 4 # Nombre de noeuds souhaites
X = np.linspace(xa, xb, Np) # Coordonnees en x des noeuds
# COORDONNEES EN Y ?
Y_init = np.linspace(ya, yb, Np) # Altitude des noeuds
if manual:
  Yc_final = zeros_like(Y_init[1:-1])
  Yc_final[0] = 0.
  Yc_final[1] = 0.
  
else:  
  Yc_final, steps = opt.fmin(
    temps2, 
    Y_init[1:-1], 
    retall  = True,
    maxiter = 10**5,
    maxfun  = 10**5)

Y_final = add_AB(Yc_final)
t_init  = temps(Y_init)
t_final = temps(Y_final)
#------------------------------------------------------------------------

#------------------------------------------------------------------------
# AFFICHAGE
fig = plt.figure(0)
plt.clf()
#plt.gca().set_aspect('equal')
plt.title('Courbe brachistochrone')
plt.plot(X, Y_init, 
  'or-', 
  label = "Ligne droite ?: $t = {0:.3} s$".format(t_init),
  linewidth = 2.)
plt.plot(X, Y_final, 
  'db-', 
  label = 'Meilleure solution ? : $t = {0:.3} s$'.format(t_final),
  linewidth = 2.)
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.grid()
plt.legend()
plt.show()
#------------------------------------------------------------------------



  