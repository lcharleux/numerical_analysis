# -*- coding: utf-8 -*-

# Exemple de minisation en Python



from scipy import optimize as opt # on importe le sous package d'otpimisation de scipy
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def ma_fonction(x, y):
  '''
  Fonction coût à minimiser
  '''
  return (1. - x)**2 + 100. * (y - x**2)**2

def ma_fonction2(params):
  '''
  Mise en forme de la fonction coût pour usage dans fmin
  '''
  return ma_fonction(params[0], params[1])

# Méthode primitive: on évalue la fonction cout sur une grille cartésienne
    
t = np.linspace(-5., 5., 100)
X, Y = np.meshgrid(t,t)
Z = ma_fonction(X,Y)




fig = plt.figure()
plt.clf()
plt.contourf(X,Y,Z, 100, cmap = cm.gist_yarg)
plt.colorbar()
#plt.contour(X,Y,Z, 100, colors = 'black')
x0 = np.array([-3., 3.])
for func in [opt.fmin, opt.fmin_powell, opt.fmin_cg, opt.fmin_bfgs]:
    sol, steps = func(ma_fonction2, x0, retall = True)
    steps = np.array(steps).transpose()
    x = steps[0]
    y = steps[1]
    plt.plot(x, y, 'o-', label = '{0}: {1} iters'.format(func.__name__, len(x)))
plt.legend()
plt.grid()
plt.show()




