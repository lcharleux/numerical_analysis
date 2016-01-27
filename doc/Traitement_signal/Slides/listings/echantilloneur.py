# echantilloneur.py
import matplotlib.pyplot as plt

def echantilloneur(t,tn,signal,fichier,xlabel='Temps $t$',
ylabel='Signal $x$',grid=True, title=''):
  plt.figure(0,figsize=(11,5))
  plt.clf()
  x = [signal(tt) for tt in t]
  xn =  [signal(tt) for tt in tn]
  plt.plot(t,x,'r-',linewidth=2.0)
  plt.plot(tn,xn,'bo--',linewidth=2.0)
  plt.xlabel(xlabel, fontsize=20)
  plt.ylabel(ylabel, fontsize=20)
  plt.title(title, fontsize=20)
  plt.legend(['signal','signal echantillone'],'upper right', shadow=True)
  plt.grid(grid)
  plt.savefig(fichier)
