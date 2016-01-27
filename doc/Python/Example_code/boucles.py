# Boucles en Python

# Boucle FOR
print 'Boucle FOR'
ma_liste = ['rouge', 'vert', 'noir', 56]

for truc in ma_liste:
  print truc # Bien remarquer le decalage de cette ligne (ou indentation) qui delimite le bloc de code qui appartient a la boucle. Dans Python, les blocs sont toujours definis par une indentation.
  
  
# Boucle IF
print 'Boucle IF'
nombre = raw_input(' 2 + 2 = ')
if nombre == 4:
  print 'Bon'
else:
  print 'Pas bon'
  
# Boucle WHILE
print 'boucle WHILE'
nombre = 3.
while nombre < 4.:
  nombre = raw_input('Donnez un nombre plus petit que 4: ')
  
  
