# listings/serieF_carre.py
from cmath import exp
from numpy import arange, array
from math import pi
from matplotlib import pyplot as plt
from trace_complexes import *
N = 1 # Nombre de coefficients calcules
for N in [1,2,4,8,16,32,64,128,256,1024]: # Valeurs de N
  # Indices n impairs
  n = [2*k+1 for k in range(-N,0)]+[2*k+1 for k in range(N)]
  c = [-2j/(pi*nn) for nn in n] # Coefficients c
  T,beaucoup= 1., 2000
  t,f = arange(beaucoup)/float(beaucoup)*T, array(n[N:2*N])/T
  trace_complexes(f,c[N:2*N],'../figures/serieF_carre_c_{0}.pdf'.format(N),title='Coefficients $c_n$ pour $N = {0}$'.format(N))
  x = []
  for tt in t:
    x.append(0.)
    for i in xrange(len(n)):
      x[-1] = x[-1]+c[i]*exp(2j*pi*n[i]*tt/T)
  x1 = [xx.real for xx in x]
  plt.figure(0,figsize=(10,2))
  plt.clf()
  plt.plot(t,x1)
  plt.title('$N={0}$'.format(N))
  plt.savefig('../figures/serieF_carre_{0}.pdf'.format(N))
