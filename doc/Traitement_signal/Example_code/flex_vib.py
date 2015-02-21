import matplotlib.pyplot as plt
import numpy as np

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
  
data = read_file("../Samples/poutre_Al_flexion.txt")
time, force, accel = data[0], data[1], data[2]
fig = plt.figure(0)  
plt.clf()
ax = fig.add_subplot(2,1,1)
plt.plot(time, force)
plt.grid()
plt.ylabel("Force, $f$ [N]")
ax = fig.add_subplot(2,1,2)
plt.plot(time, accel)
plt.grid()
plt.ylabel("Acceleration, $a$ [g]")
plt.xlabel("Time, $t$ [s]")
plt.show()
