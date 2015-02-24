# listings/exemple_FFT_frequence.py

from scipy.fftpack import fft
from random import gauss
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec



beaucoup = 1000
fe = 50. # Frequence d'echantillonage
N = 1024 # Nombre de points d'echantillonage
D = N/fe # Duree d'observation
f = 8./D # Frequence du signal
t_min = 0. # Debut du calcul du signal
t_max = t_min+D # Fin du calcul du signal
val = [1., 2., 4., 8.] # Frequence 
lab = '$f={0}$'
tn = np.arange(N)/(D*fe)*D+t_min
for i in xrange(N): 
  if tn[i]<=1./f: i_t = i

fk = np.linspace(0., fe/2., N/2) # Discretisation des frequences
plt.figure(0,figsize=(12,8))
plt.clf()
gs = gridspec.GridSpec(4, 3) # Grille de zone de trace
p0 = plt.subplot(gs[:,:2])
p0.set_title(r'$x(t) = \sin(2 \pi f t)$ avec $f$ variable, $f_e={}$'.format(fe))
p0.grid()
p0.set_xlabel(r'$f_k$', fontsize=20)
p0.set_ylabel(r'$\frac{2}{N}|X_k|$', fontsize=20)
#p0.set_xscale('log')
p0.set_yscale('log')
for z in xrange(len(val)):
  f = val[z]
  xn = [np.sin(2*np.pi*f*t) for t in tn]
  color = ['r','b','g','c'][z]
  Xk = abs(fft(xn))*2./N
  p0.plot(fk[0:N/2],Xk[0:N/2],'-'+color, label = lab.format(f))
  p0.legend()
  p1 = plt.subplot(gs[z,-1])
  p1.grid()
  p1.plot(tn[:i_t],xn[:i_t],'-'+color)
p1.set_xlabel('Temps $t$')
plt.show()

