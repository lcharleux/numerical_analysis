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
# CALCUL DU TEMPS DE PARCOURS
def temps(Y):
  # On calcule l'energie potentielle en supposant qu'elle est nulle en A
  Ep = m * g * (Y - Y[0])
  # On calcule l'energie cinetique 
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

def func(Yc):
  Y = add_AB(Yc)
  return temps(Y)

# Brute force
P = 20
X = np.linspace(xa, xb, 4)
y = np.linspace(-.5, .9, P)
Y0, Y1 = np.meshgrid(y,y)
Y0 = Y0.flatten()
Y1 = Y1.flatten()
Y = np.array([Y0, Y1]).transpose()
t = np.zeros(len(Y))
for i in xrange(len(Y0)):
  Yc  = add_AB(Y[i])
  t[i] = temps(Yc)

# Trace
fig = plt.figure(0)
plt.clf()
plt.plot(Y0, Y1, 'om',label= "Evaluations de $f$")
Y0 = Y0.reshape(P,P)
Y1 = Y1.reshape(P,P)
t = t.reshape(P,P)

plt.contourf(Y0, Y1, t, 20)
plt.contour(Y0, Y1, t, 20, colors = "black")
plt.grid()
plt.legend()
plt.savefig("brachi_BF.pdf")
  
  
   
