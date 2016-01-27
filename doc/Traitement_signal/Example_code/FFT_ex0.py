import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack

# Signal
T = 1.
def signal(t): return np.sin(2. * np.pi * t / T)
# Echantillonnage
D = 2. # Duree d'observation
fe = 100. # Frequence d'echantillonnage
N = int(D * fe) + 1 # Nombre de points enregistres
t = np.linspace(0., (N-1)/fe, N) # Grille d'echantillonnage
x = signal(t)
# FFT
X = fftpack.fft(x)
fpos = np.linspace(0., fe/2., N/2)
Xpos = X[0:N/2]
# Trace du signal et de son spectre
fig = plt.figure(0)
ax = fig.add_subplot(3,1,1)
plt.plot(t, x, 'r-')
plt.grid()
plt.xlabel("Temps $t$")
plt.ylabel("Amplitude $x(t)$")
ax = fig.add_subplot(3,1,2)
plt.plot(fpos, abs(Xpos), 'b*-')
plt.grid()
plt.ylabel("Amplitude $|X(f)|$")
ax = fig.add_subplot(3,1,3)
plt.plot(fpos, np.degrees(np.angle(Xpos)), 'b*-')
plt.grid()
plt.xlabel("Frequence $f$")
plt.ylabel("Amplitude $arg(X(f)) [^o]$")
plt.show()
