# listings/exemple1.py
# On charge la fonction signal_sinusoidal
from signal_sinusoidal import * 
# On charge la fonction trace_signal
from trace_signal import * 
from numpy import arange
signal = signal_sinusoidal # On definit le signal utilise
T = 1. # Periode du signal
t_min = 0. # Debut du calcul du signal
t_max = 2. # Fin du calcul du signal
np = 10000 # Nombre de points calcules
# On definit l'interval de temps a tracer
t = arange(np)/float(np)*(t_max-t_min)+t_min 
# Fichier dans lequel tracer
fichier = '../figures/sinusoide.pdf' 
x = [signal(tt,T=T) for tt in t]
trace_signal(t,x,fichier)


