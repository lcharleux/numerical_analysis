def lire_fichier(nom_fichier):
  '''
  Lit le fichier dont le nom est fourni, y cherche 2 colonnes et convertit le tout en nombres.
  '''
  fichier = open(nom_fichier, 'r') # Ouverture du fichier. Le second argument specifie le mode d'ouverture: 'r' pour read, 'w' pour write, etc...
  lignes = fichier.readlines() # On demande de lire toutes les lignes une par une et de stocker le resultat dans une liste
  col_0, col_1 = [], [] # On cree 2 listes vides pour recevoir le contenu des colonnes
  for ligne in lignes: # On cree une boucle FOR dont le nombre d'iterations est adapte au nombre de lignes.
    mots = ligne.split() # On casse chaque ligne sur les espaces et tabulations pour obtenir des mots
    col_0.append(float(mots[0])) # On convertit les mots en nombre avec la commande float et on les ajoute a la fin des listes col_0 et col_1
    col_1.append(float(mots[1]))
  return col_0, col_1
    
nom_fichier = 'data.txt'
temps, amplitude = lire_fichier(nom_fichier) # Et voila...
    
    
