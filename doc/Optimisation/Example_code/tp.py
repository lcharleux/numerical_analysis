#------------------------------------------------------------------------
# Regression ou "fit"
#------------------------------------------------------------------------

# PACKAGES
from scipy import optimize as opt # Optimize
import numpy as np                # Numpy
import matplotlib.pyplot as plt   # Pyplot
from matplotlib import cm         # Colormaps


# CONDITIONS INITIALES
# Remarque: il est hautement conseille de jouer avec ces parametres pour voir leur effet.
tau0 = 1.     # Amortissement initial
omega0 = 1.   # Pulsation initiale



# FONCTIONS UTILES
def fonction(tau, omega, x):
  '''
  Une fonction 
  '''
  return np.sin(omega * x ) * np.exp(-x/tau)
  

def erreur(params):
  '''
  Mise en forme de la fonction cout pour usage dans fmin
  '''
  e = 0.
  for i in xrange(len(x)):
    e += (fonction(params[0], params[1], x[i]) - y[i])**2 
  return e  


# RESOLUTION
Np = 100
tau_sol = 5.
omega_sol = 4.
bruit = 1.
x = np.linspace(0., 10., Np)
y_perfect = fonction(tau_sol, omega_sol, x)
y = y_perfect + bruit * (np.random.rand(Np) -.5) 


# Methode intuitive  
t = np.linspace(1., 5., 100)
Tau, Omega = np.meshgrid(t,t)
Err = erreur((Tau, Omega))


# Methode du simplexe
params0 = np.array([tau0, omega0])
sol, steps = opt.fmin(erreur, params0, retall = True)
steps = np.array(steps).transpose()
tau = steps[0]
omega = steps[1]
tau_f = sol[0]
omega_f = sol[1]
y_f = fonction(tau_f, omega_f, x)  

# AFFICHAGE
N = 20
fig = plt.figure()
plt.clf()
fig.add_subplot(121)
plt.plot(x,y_perfect, 'kd', linewidth = 2., label = 'Donnees')
plt.plot(x,y, 'or', label = 'Donnees + Bruit')
for i in xrange(len(tau)):
  tau_i = tau[i]
  omega_i = omega[i]
  y_i = fonction(tau_i, omega_i, x)  
  plt.plot(x,y_i, 'g-', linewidth = 1.)
plt.plot(x,y_f, 'b-', linewidth = 1., label = 'Solution')
plt.legend()
fig.add_subplot(122)
plt.title('Erreur')
plt.contourf(Tau, Omega, Err, N)
plt.colorbar()
plt.contour(Tau, Omega, Err, N, colors = 'black')
plt.grid()
plt.plot(tau, omega, 'go-', linewidth = 2.)
plt.show()
