# listings/exemple_DFT.py
from signal_sinusoidal import * 
from signal_carre import *
from trace_complexes import *
from numpy import arange, floor
from cmath import exp
signal = signal_sinusoidal #signal = signal_carre
beaucoup, rien = 1000, 1.e-10
f = 3.3 # Frequence du signal
D = 4. # Duree d'observation
t_min = 0. # Debut du calcul du signal
t_max = t_min+D # Fin du calcul du signal
fe = 16. # Frequence d'echantillonage
N = int(floor(D*fe)) # Nombre de points d'evaluation
tn = arange(N)/(D*fe)*(t_max-t_min)+t_min # Discretisation du temps
xn = [signal(tt,T=1./f, k=4.) for tt in tn] # Discretisation du signal
Xk = [] # DFT de xn
for k in range(N): # Boucle sur k
  Xk.append(0.)
  for n in range(N): # Boucle sur n
    Xk[-1] = Xk[-1] + xn[n]*exp(-2j*pi*n*k/N) # Calcul de Xk
  if abs(Xk[-1].real) < rien : Xk[-1] = Xk[-1] - Xk[-1].real
  if abs(Xk[-1].imag) < rien : Xk[-1] = Xk[-1] - 1j*Xk[-1].imag 
  Xk[-1] = Xk[-1]*2/N 
fk = arange(N)/D # Discretisation des frequences
tit='$DFT(\sin(2\pi nf/f_e))*2/N$: N={0}, f={1}, D={2}'.format(N,f,D)
trace_complexes(fk[:N/2],Xk[:N/2],'../figures/DFT_sinus.pdf',title=tit)
