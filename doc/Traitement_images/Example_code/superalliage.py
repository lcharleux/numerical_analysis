from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage

im = Image.open('superalliage.jpg')
R, V, B = im.split()
R = np.asarray(R, np.float64)
V = np.asarray(R, np.float64)
B = np.asarray(R, np.float64)

# On choisit le canal rouge
Z = R


# Correction vignetage
ny, nx = Z.shape
x = np.arange(nx) -nx/2.
y = np.arange(ny) -ny/2.
X,Y = np.meshgrid(x,y)
kx, ky = .0007, 0.001
Z += kx * X**2 + ky * Y**2

plt.figure(2)
plt.contourf(X,Y,Z)
plt.show()


bins = 16
plt.figure(1)
plt.clf()
plt.hist(R.flatten(), bins = bins)
plt.show()



Zs = np.where(Z > 90., 1., 0.) # Gros debat sur la valeur du seuil ici...

Zse = ndimage.morphology.binary_erosion(Zs, structure = np.ones([3,3]))

n, Zl = ndimage.label(Zs)