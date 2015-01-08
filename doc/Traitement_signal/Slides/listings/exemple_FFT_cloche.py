# listings/exemple_FFT_cloche.py
from scipy.fftpack import fft
from numpy import array, arange, hanning
from matplotlib import pyplot as plt
import pickle
nom = '../figures/FFT_cloche-log.pdf'
fichier = open('cloche.pckl','r') # Ouverture du fichier
cloche = pickle.load(fichier) # Chargement des donnees
fichier.close() # Fermeture du fichier
xn = cloche['x'][::32] # Redimensionnement des donnees
fe = float(cloche['fe']) # Definition de la frequence d'echantillonage
tn = arange(len(xn))/float(fe) 
N = len(tn)
D = N/fe
plt.figure(0,figsize=(12,8))
plt.clf()
fk = arange(N)/D # Discretisation des frequences
Xk = abs(fft(xn))*2./N
Xkh = abs(fft(xn*hanning(N)))*2./N
plt.plot(fk[0:N/2],Xk[0:N/2],'-', label='Signal brut')
plt.plot(fk[0:N/2],Xkh[0:N/2],'-', label='Fenetrage Hann')
plt.xlabel(r'$f_k$', fontsize=20)
plt.ylabel(r'$\frac{2}{N}|X_k|$', fontsize=20)
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.legend(loc='upper left')
plt.savefig(nom)

