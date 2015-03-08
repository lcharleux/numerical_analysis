from PIL import Image 
import numpy as np   
from matplotlib import pyplot as plt 
im = Image.open('../data/grenouille.jpg') 
rouge, vert, bleu = im.split()
Z = np.array(rouge)
Z = np.flipud(Z)
ny, nx = Z.shape
x = np.arange(nx)
y = np.arange(ny)
X, Y = np.meshgrid(x, y)
fig = plt.figure(0) 
plt.clf()
plt.title("Image monochrome")
plt.contourf(X, Y, Z, 100)
cbar = plt.colorbar()
cbar.set_label("Valeurs pixels")
plt.grid()
plt.xlabel("Pixels selon x")
plt.ylabel("Pixels selon y")
plt.show()
