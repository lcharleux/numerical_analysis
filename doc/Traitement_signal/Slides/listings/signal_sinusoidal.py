# signal_sinusoidal.py
from math import sin,pi
# T: periode, k: amplitude, phi: dephasage
def signal_sinusoidal(t,T=1.,k=1.,phi=0.):
  return k*sin(2*pi*t/T+phi)
