# listings/exemple4.py
import pickle
from numpy import arange
from trace_signal import *
fichier = open('cloche.pckl','r') # Ouverture du fichier
cloche = pickle.load(fichier) # Chargement des donnees
fichier.close() # Fermeture du fichier
x = cloche['x'][::32] # Redimensionnement des donnees
fe = cloche['fe'] # Definition de la frequence d'echantillonage
t = arange(len(x))/float(fe) 
fichier = '../figures/cloche.pdf' 
trace_signal(t,x,fichier)

