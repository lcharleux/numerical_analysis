#listings/signal_carre.py
from numpy import floor
# T: periode, k: amplitude
def signal_carre(t,T=1.,k=1.):
  t = t - floor(t/T)
  x = -1.
  if t > T/2.: x = 1.
  return x
