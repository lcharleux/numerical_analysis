# Creation d'une classe de vecteurs

class vecteur:
  '''
  Classe vecteur: decrit le comportement d'un vecteur a 3 dimensions.
  '''
  def __init__(self, x = 0., y = 0., z = 0.): # Constructeur: c'est la fonction (ou methode) qui est lancee lors de la creation d'un exemplaire de la classe.
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)
    
  def norme(self): # Une methode qui renvoie la norme
    x, y, z = self.x, self.y, self.z
    return (x**2 + y**2 + z**2)**.5
  
  def __repr__(self): # On definit comment la classe apparait dans le terminal
    x, y, z = self.x, self.y, self.z
    return '<vecteur: ({0}, {1}, {2})>'.format(x, y, z)
  
  # Addition
  def __add__(self, other): # On definit le comportement de la classe vis-a-vis de l'addition
    x, y, z = self.x, self.y, self.z
    if type(other) in [float, int]: # Avec un nombre
      return vecteur(x + other, y + other, z + other)
    if isinstance(other, vecteur): # Avec un vecteur
      return vecteur(x + other.x, y + other.y, z + other.z)
  __radd__ = __add__ # On definit l'addition a gauche pour garantir la commutativite
  
  # Multiplication: 
  def __mul__(self, other): # On definit le comportement de la classe vis-a-vis de la multiplication
    x, y, z = self.x, self.y, self.z
    if type(other) in [float, int]: # Avec un nombre
      return vecteur(x * other, y * other, z * other)
    if isinstance(other, vecteur): # Avec un vecteur: produit vectoriel
      x2, y2, z2 = other.x, other.y, other.z
      xo = y * z2 - y2 * z
      yo = z * x2 - z2 * x
      zo = x * y2 - x2 * y 
      return vecteur(xo, yo, zo)
  __rmul__ = __mul__ # On definit le produit vectoriel a gauche
  
  def scalaire(self, other):
    '''
    Effectue le produit scalaire entre 2 vecteurs.
    ''' 
    x, y, z = self.x, self.y, self.z
    x2, y2, z2 = other.x, other.y, other.z
    return x * x2 + y * y2 + z * z2
  
  def normaliser(self):
    '''
    Normalise le vecteur.
    '''
    x, y, z = self.x, self.y, self.z
    n = self.norme()
    self.x, self.y, self.z = x / n, y / n , z / n
    
