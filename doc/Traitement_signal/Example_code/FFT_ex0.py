import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack

# Signal
T = 1.
def signal(t): return np.sin(2. * np.pi * t / T)
# Echantillonnage
D = 2. # Duree d'observation
fe = 10. # Frequence d'echantillonnage
N = int(D * fe) + 1 # Nombre de points enregistres
t = np.linspace(0., D, N) # Grille d'echantillonnage
x = signal(te)
# FFT
X = fftpack.fft(xe)
f = np.linspace(-fe/2., fe/2., N)
# Trace du signal et de son spectre
fig = plt.figure(0)
ax = fig.add_subplot(3,1,1)
plt.plot(t, x, 'r-')
plt.grid()
plt.xlabel("Temps $t$")
plt.ylabel("Amplitude $x(t)$")
ax = fig.add_subplot(3,1,2)
plt.plot(f, abs(X), 'b-')
plt.grid()
ax = fig.add_subplot(3,1,3)
plt.plot(f, np.degrees(np.angle(X)), 'b-')
plt.grid()
plt.xlabel("Fréquence $f$")
plt.ylabel("Amplitude $x(t)$")
plt.show()
