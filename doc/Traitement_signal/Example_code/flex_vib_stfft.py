import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack

def read_file(path, skip = 1, ncol = 3):
  """
  Reads the data from the
  """
  lines = open(path, "r").readlines()
  header = lines[skip]
  data = lines[skip:]
  out = [[] for i in xrange(ncol)]
  for line in data:
    words = line.split()
    for i in xrange(ncol):
      out[i].append(float(words[i]))
  out = np.array(out)
  return out

def stfft(x, y, wind_size):
  """
  Computes the short term FFT spectre of a signal
  """
  n = len(x)
  dx = x[1] - x[0] 
  fe = 1./ dx # sampling rate
  Z = np.zeros(n - wind_wsize +1, wind_size)
  t = np.zeros()
  for i in xrange(n - wind_wsize +1):
    x_slice = y[(win_size-1)/2 + i: (win_size-1)/2 + i + 1]
    y_slice = y[(win_size-1)/2 + i: (win_size-1)/2 + i + 1]
    Y_slice = fftpack.fft(y_slice)
    out[i,:] = 
    
  X = np.linspace(0., fe/2., n/2)  
  return X, Y
 
data = read_file("../Samples/poutre_Al_flexion.txt")
time, force, accel = data[0], data[1], data[2]
force -= force.mean() # Removing mean value
accel -= accel.mean() # Removing mean value
Freq, Force = spectre(time, force)
Freq, Accel = spectre(time, accel)

fig = plt.figure(0)  
plt.clf()
ax = fig.add_subplot(2,1,1)
plt.plot(Freq, abs(Force))
plt.grid()
plt.ylabel("Force, $|fft(f)|$ [N]")
ax = fig.add_subplot(2,1,2)
plt.plot(Freq, abs(Accel))
plt.grid()
plt.ylabel("Acceleration, $|fft(a)|$ [g]")
plt.xlabel("Frequency, $f$ [Hz]")
plt.show()
