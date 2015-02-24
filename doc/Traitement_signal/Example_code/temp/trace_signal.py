# trace_signal.py
import matplotlib.pyplot as plt

def trace_signal(t,x,fichier,xlabel='Temps $t$',
ylabel='Signal $x$',grid=True, style='r-'):
  plt.figure(0,figsize=(9,5))
  plt.clf()
  plt.plot(t,x,style,linewidth=2.0)
  plt.xlabel(xlabel, fontsize=15)
  plt.ylabel(ylabel, fontsize=15)
  plt.grid(grid)
  plt.savefig(fichier)
