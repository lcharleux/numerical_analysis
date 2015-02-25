import pickle
import numpy as np
data = pickle.load(open("cloche.pckl"))
fe = data["fe"]
x = data["x"]
N = len(x)
t = np.linspace(0., (N-1)/fe, N)
f = open("cloche.txt", "w")
f.write("Time[s]\t Acceleration[g]\n")
for i in xrange(N):
  f.write("{0}\t{1}".format(t[i], x[i]))
  if i != (N-1): f.write("\n")

