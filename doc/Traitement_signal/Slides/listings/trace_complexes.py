# trace_complexes.py
import matplotlib.pyplot as plt

def trace_complexes(x,y,fichier,xlabel='Frequence $f$', title='', style='ro'):
  plt.figure(0,figsize=(9,5))
  plt.clf()
  plt.grid(True)
  p0 = plt.subplot(2,1,1)
  p0.set_title(title)
  p0.grid()
  p0.plot(x,[yy.real for yy in y],style,linewidth=2.0)
  p0.set_ylabel('Partie reelle', fontsize=15)
  p1 = plt.subplot(2,1,2)
  p1.grid()
  p1.plot(x,[yy.imag for yy in y],style,linewidth=2.0)
  p1.set_xlabel(xlabel, fontsize=15)
  p1.set_ylabel('Partie imaginaire', fontsize=15)
  plt.savefig(fichier)
