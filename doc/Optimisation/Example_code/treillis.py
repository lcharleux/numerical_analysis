#------------------------------------------------------------------------
# Resolution d'un probleme de treillis par une methode d'optimisation
#------------------------------------------------------------------------

# PACKAGES
from scipy import optimize as opt # Optimize
import numpy as np                # Numpy
import matplotlib.pyplot as plt   # Pyplot
from matplotlib import cm         # Colormaps
import time

class Stalker(object):
  """
  A stalker class to spy inputs and outputs of a function.
  """

  def __init__(self, func, speak = False, label = "Function"):
      self.func = func
      self.args = []
      self.kwargs = []
      self.speak = speak
      self.label = label
      self.out =  []
      self.time = []         
  def __call__(self, *args, **kwargs):
    self.args.append(args)
    self.kwargs.append(kwargs)
    out = self.func(*args, **kwargs)
    self.out.append(out)
    self.time.append(time.time())
    # Some messages
    if self.speak:
      a = ""
      if args != (): 
        for v in args:
          a += str(v) + ","
      a = a[:-1] + ", "   
      if kwargs != {}:
        for k in kwargs.keys():
          a += "{0} = {1},".format(k, kwargs[k])
      a = a[:-1]    
      print "{0} => f({1}) = {2}".format(self.label, a, out)
    return out


# CONDITIONS INITIALES
# Remarque: il est hautement conseille de jouer avec ces parametres pour voir leur effet.
xa, ya = 0., 0. # Position initiale de A
xb, yb = 1., 1. # Position initiale de B
xc, yc = 0., 2. # Position initiale de C
m = 5.          # Masse en B
g = 10.         # Gravite
k = 100.        # Raideur des ressorts


# FONCTIONS UTILES
def Epot(xb1, yb1):
  '''
  Energie potentielle du systeme
  '''
  AB  = ((xb -xa)**2 + (yb -ya)**2)**.5
  AB1 = ((xb1-xa)**2 + (yb1-ya)**2)**.5
  CB  = ((xb -xc)**2 + (yb -yc)**2)**.5
  CB1 = ((xb1-xc)**2 + (yb1-yc)**2)**.5
  Ep = .5 * k * (  (AB - AB1)**2 + (CB - CB1)**2) + m * g * yb1
  return Ep

def ma_fonction(params):
  '''
  Mise en forme de la fonction cout pour usage dans fmin
  '''
  return Epot(params[0], params[1])

# RESOLUTION

# Methode intuitive  
t = np.linspace(-2., 2., 100)
Xb, Yb = np.meshgrid(t,t)
E = Epot(Xb, Yb)

# Methode du simplexe
params0 = np.array([xb, yb])
sfonc = Stalker(ma_fonction)
sol = opt.minimize(sfonc, params0, method = "Nelder-Mead")
steps = np.array(sfonc.args).transpose()
x = steps[0][0]
y = steps[1][0]
xb2, yb2 = steps[0][0][-1],steps[1][0][-1] 

# AFFICHAGE
deport = .05    # Deport du texte
N = 50
fig = plt.figure()
plt.clf()
plt.title('Treillis')
plt.plot([xa, xb, xc], [ya, yb, yc], 'g-',linewidth = 2., label = 'Depart')
plt.annotate('A', xy=(xa, ya), xytext= (xa + deport, ya - deport), xycoords='data', )
plt.annotate('B', xy=(xb, xb), xytext= (xb + deport, yb - deport), xycoords='data', )
plt.annotate('C', xy=(xc, yc), xytext= (xc + deport, yc - deport), xycoords='data', )
plt.xlabel('$x_b$')
plt.ylabel('$y_b$')
plt.contourf(Xb, Yb, E, N, cmap = cm.jet)
cbar = plt.colorbar()
plt.contour(Xb, Yb, E, N, colors = 'black')
cbar.set_label(r'$E_{pot} \; (J)$', fontsize = 15.)
plt.grid()
plt.plot(x,y, 'og-', linewidth = 2., label = 'Trajet')
plt.plot([xa, xb2, xc], [ya, yb2, yc], 'y-',linewidth = 2., label = 'Solution')
plt.legend()
plt.show()
