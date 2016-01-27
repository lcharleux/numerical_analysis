import numpy as np   
from matplotlib import pyplot as plt 
from scipy import ndimage
x = np.linspace(0., 1., 500)
y_perf = np.sin(2. * np . pi * x) 
noise = np.random.normal(loc = 0.,scale = .1,  size = len(x))
y = y_perf + noise
yg = ndimage.gaussian_filter(y, 10.)
ym =  ndimage.uniform_filter(y, 20)

fig = plt.figure()
ax = fig.add_subplot(2, 1, 1)
plt.plot(x, y_perf, "r-", label = "Signal", linewidth = 2.)
plt.plot(x, noise, "b-", label = "Noise")
plt.plot(x, y, "k.", label = "Signal + noise")
plt.grid()
plt.legend()
ax = fig.add_subplot(2, 1, 2)
plt.plot(x, y, "k.", label = "Signal + noise")
plt.plot(x, yg, "g-", label = "Gausian_filter(signal + noise)", linewidth = 2.)
plt.plot(x, ym, "m-", label = "Uniform_filter(signal + noise)", linewidth = 2.)
plt.grid()
plt.legend()
plt.show()
