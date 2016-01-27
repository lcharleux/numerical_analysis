# listings/exemple3.py
# On charge la fonction sinusoidale
from signal_sinusoidal import * 
# On charge la fonction trace_signal
from trace_signal import * 
from numpy import arange
s = signal_sinusoidal 
T0,T1 = 1.,.5 # Periodes du signal
t_min = 0. # Debut du calcul du signal
t_max = 2. # Fin du calcul du signal
np = 1000 # Nombre de points calcules
# On definit l'interval de temps a tracer
t = arange(np)/float(np)*(t_max-t_min)+t_min 
fichier = '../figures/bisinus.pdf' 
x = [s(tt,T=T0)+s(tt,T=T1) for tt in t]
trace_signal(t,x,fichier)
