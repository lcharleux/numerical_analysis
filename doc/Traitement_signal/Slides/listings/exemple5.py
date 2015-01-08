# listings/exemple5.py
# On charge la fonction sinusoidale
from signal_sinusoidal import * 
# On charge la fonction trace_signal
from echantilloneur import * 
from numpy import arange, floor
signal = signal_sinusoidal 
f = 1. # Frequence du signal
fe = 1.2*f # Frequence d'echantillonage
D = 10./f # Duree d'observation
t_min = 0. # Debut du calcul du signal
t_max = t_min+D # Fin du calcul du signal
N = int(floor(D*fe))
beaucoup = 1000
# On definit l'echantillonage
tn = arange(N)/float(N)*(t_max-t_min)+t_min
t = arange(beaucoup)/float(beaucoup)*(t_max-t_min)+t_min
fichier = '../figures/echant_sin_6.pdf' 
x = [signal(tt,T=1./f) for tt in t]
title = '$f={0}$, $f_e/f={1}$, $D/T={2}$'.format(f,fe/f,D*f)
echantilloneur(t,tn,signal,fichier,title=title)
