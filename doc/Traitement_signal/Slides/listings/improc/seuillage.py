import numpy as np
from matplotlib import pyplot as plt

def func(X,Y):
  A = np.cos(2 * np.pi * X) * np.cos(2 * np.pi * Y)
  B = X**2 + Y**2 + 1.
  return A / B
x = np.linspace(-1, 1, 1000)
X, Y = np.meshgrid(x, x)
Z = func(X,Y)
s = 0.5 # Choix du seuil
Z_seuil = Z > s
fig = plt.figure(0)
plt.clf()
ax = fig.add_subplot(121)
grad = plt.imshow(Z) 
plt.colorbar(grad)
ax = fig.add_subplot(122)
ax.set_title('$s = {0}$'.format(s))
grad = plt.imshow(Z_seuil) 
plt.colorbar(grad)
plt.savefig('../../figures/seuillage0.png')



