# listings/exemple_aliasing.py
from matplotlib import pyplot as plt
from math import sin, pi
from signal_sinusoidal import signal_sinusoidal as signal
from numpy import arange, floor
beaucoup = 1000
f = 1. # Frequence du signal
D = 2./f # Duree d'observation
t_min = 0. # Debut du calcul du signal
t_max = t_min+D # Fin du calcul du signal
fe = 2.1*f # Frequence d'echantillonage
N = int(floor(D*fe)) # Nombre de points d'evaluation
plt.figure(0)
plt.clf()
plt.xlabel('Temps $t$', fontsize=20)
plt.ylabel('Signal $x$', fontsize=20)
kmin,kmax =-1, 2
t = arange(beaucoup)/float(beaucoup)*(t_max-t_min)+t_min
for k in xrange(kmin,kmax):
  f1 = f + k*fe
  x = [signal(tt,T=1./f1) for tt in t]
  plt.plot(t,x,'b-',linewidth=1.)
tn = arange(N)/(D*fe)*(t_max-t_min)+t_min
xn = [signal(tt,T=1./f) for tt in tn]
plt.plot(tn,xn,'or')
x = [signal(tt,T=1./f) for tt in t]
plt.plot(t,x,'r-',linewidth=2.)
plt.savefig('../figures/exemple_aliasing.pdf')
