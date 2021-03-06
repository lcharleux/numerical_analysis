# listings/exemple_FFT_bruit.py
from math import pi,sin, exp
from scipy.fftpack import fft
from random import gauss
from numpy import array, arange, floor
from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec
from signal_sinusoidal import *
beaucoup = 1000
fe = 64. # Frequence d'echantillonage
N = 4096 # Nombre de points d'echantillonage
D = N/fe # Duree d'observation
f = 8./D # Frequence du signal
t_min = 0. # Debut du calcul du signal
t_max = t_min+D # Fin du calcul du signal
stddev = 0. # Ecart type du bruit
nom = '../figures/FFT_bruit.pdf'
amort = 0.
val = [1.,1.e-1,1.e-2,0.] # Bruit
lab = 'Ecart type bruit: {0}'
tn = arange(N)/(D*fe)*D+t_min
for i in xrange(N): 
  if tn[i]<=1./f: i_t = i
xn = [sin(2*pi*f*t) for t in tn]
fk = arange(N)/D # Discretisation des frequences
plt.figure(0,figsize=(12,8))
plt.clf()
gs = gridspec.GridSpec(4, 3) # Grille de zone de trace
p0 = plt.subplot(gs[:,:2])
p0.set_title(r'$x(t) = \sin(2 \pi f t)+$ bruit')
p0.grid()
p0.set_xlabel(r'$f_k$', fontsize=20)
p0.set_ylabel(r'$\frac{2}{N}|X_k|$', fontsize=20)
p0.set_xscale('log')
p0.set_yscale('log')
for z in xrange(len(val)):
  v = val[z]
  stddev = v
  v_amort = array([exp(-t*amort) for t in tn])
  color = ['r','b','g','c'][z]
  bruit = array([gauss(0,stddev) for i in xrange(N)])
  xxn = (xn + bruit)*v_amort
  Xk = abs(fft(xxn))*2./N
  p0.plot(fk[0:N/2],Xk[0:N/2],'-'+color, label = lab.format(v))
  p0.legend()
  p1 = plt.subplot(gs[z,-1])
  p1.grid()
  p1.plot(tn[:i_t],xxn[:i_t],'-'+color)
p1.set_xlabel('Temps $t$')
plt.savefig(nom)

