from scipy.fftpack import fft2, ifft2,fftshift, ifftshift
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm

# Ouverture image
im = Image.open("houle.png")
z = np.array(im) # image to array

# Image originale    
fig = plt.figure(0)
plt.clf()
plt.xticks([])
plt.yticks([])
grad = plt.imshow(z, cmap = cm.gray)
plt.colorbar(grad)
plt.savefig(figdir+'lapin_original.png')

# FFT 2D
Z = fftshift(fft2(z))
fig = plt.figure(0)
plt.clf()
plt.xticks([])
plt.yticks([])
grad = plt.imshow(np.log(abs(Z)), cmap = cm.gray)
plt.colorbar(grad)
plt.savefig(figdir+'lapin_spectre.png')

# Filtre passe bas
x = np.linspace(-1., 1., len(Z[0]))
y = np.linspace(-1., 1., len(Z))
X, Y = np.meshgrid(x, y)
R = (X**2 + Y**2)**.5
F = R < .1 # Voici notre filtre
#F = abs(X) <0.05
fig = plt.figure(0)
plt.clf()
plt.xticks([])
plt.yticks([])
grad = plt.imshow(F, cmap = cm.gray)
plt.colorbar(grad)
plt.savefig(figdir+'lapin_lowpass.png')

# Application du filtre passe bas
Z = Z * F
fig = plt.figure(0)
plt.clf()
plt.xticks([])
plt.yticks([])
grad = plt.imshow(np.log(abs(Z+1)), cmap = cm.gray)
plt.colorbar(grad)
plt.savefig(figdir+'lapin_lowpass2.png')

# FFT inverse
z_lp = abs(ifft2(ifftshift(Z))) 
fig = plt.figure(0)
plt.clf()
plt.xticks([])
plt.yticks([])
grad = plt.imshow(z_lp, cmap = cm.gray)
plt.colorbar(grad)
plt.savefig(figdir+'lapin_lowpass3.png')

# Filtre passe haut
x = np.linspace(-1., 1., len(Z[0]))
y = np.linspace(-1., 1., len(Z))
X, Y = np.meshgrid(x, y)
R = (X**2 + Y**2)**.5
F = R > .05 # Voici notre filtre
#F = abs(Y) >0.05
Z = fftshift(fft2(z))
z_hp = abs(ifft2(ifftshift(Z * F))) 
fig = plt.figure(0)
plt.clf()
plt.xticks([])
plt.yticks([])
grad = plt.imshow(z_hp, cmap = cm.gray)
plt.colorbar(grad)
plt.savefig(figdir+'lapin_highpass.png')

#zs = seuillage(z,100)
#Zs = fft2(zs)
#f = passebas(z,50)
f = passehaut(z,150)
z2 = abs(ifft2(ifftshift(Z*f)))


