# listings/exemple_FFT.py
from math import pi,sin
from scipy.fftpack import fft
N = 8
xn = [sin(2*pi*n/N) for n in xrange(N)]
Xk = fft(xn)
