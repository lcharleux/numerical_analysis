Python
____________________________

Python présente plusieurs avantage à l'origine de son choix pour ce cours:

* C'est un langage généraliste présent dans de nombreuses domaines: calcul scientifique, web, bases de données, jeu vidéo, graphisme, etc. C'est un outil polyvalent qu'un ingénieur peut utiliser pour toutes les tâches numériques dont il a besoin.
* Il est présent sur la majorité des plateformes: Windows, Mac OS, Linux, Unix, Android
* C'est un langage libre et gratuit avec un grande communauté d'utilisateurs. Tous vos programmes sont donc échangeables sans contraintes. Vos questions trouveront toujours des réponses sur internet. Enfin, très peu de bugs sont présents dans Python.

Installation
=============================

A Polytech' Annecy-Chambéry, Python est présent sur toutes les machines et toutes les plateformes:

* Sous Windows (XP/7): vous le trouverez dans le dossier **R:\\Python26** dans sa version 2.6.
* Sous Fédora/Linux: il est installé de base et est accessible dans un terminal (Konsole par exemple) *via* la commande **python**.

Sur les autres machines, voir la section dédiée sur le site `python.org/download <http://www.python.org/download/>`_.


Introduction
==============================

Execution
++++++++++++++++

Python s'utilise comme une "grosse" calculatrice, les commandes peuvent y être tapées une par une dans un terminal:

>>> print 'Hello World !'
Hello World !
>>> a = 5.
>>> b = 7.
>>> a + b
12.0

Ou grâce à un fichier texte, de préférence terminé par **.py**, comme le fichier :download:`script.py <Python/Example_code/script.py>` contenant:

.. literalinclude:: Python/Example_code/script.py

Pour executer un script Python, deux options sont possibles:

* L'exécuter directement dans un terminal avec la commande **python script.py**.
* Lancer Python puis les utiliser la commande Python:

>>> execfile('script.py')

La première méthode est adaptée à un programme fonctionnant déja correctement alors que la seconde est plus adaptée à la période d'écriture du programme car elle permet d'accéder après coup aux variables générées par le programme.

.. note:: Ces considérations sur le mode d'exécution des programme est essentiellement importante sous Linux.

Bases
+++++++++++++++++++

Cette partie fournit quelques informations basiques sur Python, pour aller plus loin, se référer à la très complete documentation officielle `http://docs.python.org/2/tutorial/ <http://docs.python.org/2/tutorial/>`_.

Nombres 
-------

>>> a = 3.      # On définit un flottant (64 bits par défaut) 
>>> b = 7       # On définit un entier (32 bits par défaut)
>>> type(a)     # On demande le type de a
<type 'float'>
>>> type(b)     # On demande le type de b
<type 'int'>
>>> a + b       # On additionne a et b, on remarque que le résultat est un flottant.
10.0
>>> c = a + b   # On assigne à c la valeur a + b

Chaînes de caractères
----------------------

>>> mon_texte = 'salade verte' # Une chaîne de caractères
>>> mon_texte[0] # Premier caractère
's'
>>> mon_texte[1] # Second caractère
'a'
>>> mon_texte[-1] # Dernier caractère
'e'
>>> motif = 'Les {0} sont {1}' # Une comportant des balises de formatage
>>> motif.format('lapins', 'rouges') # Formatage de la chaine
'Les lapins sont rouges'
>>> motif.format('tortues', 5)
'Les tortues sont 5'


Listes et dictionnaires
-------------------------

>>> ma_liste = [] # On crée une liste vide 
>>> ma_liste.append(45) # On ajoute 45 à la fin de la liste.
>>> mon_texte = 'Les lapins ont des grandes oreilles' # On définit une chaine de caractères nommé mon_texte
>>> ma_liste.append(mon_texte) # On ajoute mon_texte à la fin de ma_liste.
>>> ma_liste    # On demande à voir le contenu de ma_liste
[45, 'Les lapins ont des grandes oreilles']
>>> ma_liste[0] # On demande le premier élément de la liste (Python compte à partir de 0)
45
>>> ma_liste[1]
'Les lapins ont des grandes oreilles'
>>> ma_liste[0] = a + b # On écrase le premier élément de ma_liste avec a + b
>>> ma_liste
[10.0, 'Les lapins ont des grandes oreilles']
>>> mon_dict = {} # On définit un dictionnaire
>>> mon_dict['lapin'] = 'rabbit' # On associe à la clé 'lapin' la valeur 'rabbit'
>>> mon_dict[1] = 'one' # On associe à la clé 1 la valeur 'one'
>>> mon_dict 
{1: 'one', 'lapin': 'rabbit'}
>>> mon_dict[1]
'one'
>>> mon_dict.keys() # Liste des clés
[1, 'lapin']
>>> mon_dict.values() # Liste des valeurs
['one', 'rabbit']

Boucles
-------

On crée un fichier :download:`boucles.py <Python/Example_code/boucles.py>`:

.. literalinclude:: Python/Example_code/boucles.py

Fonctions
----------

On crée un fichier :download:`fonctions.py <Python/Example_code/fonctions.py>`:

.. literalinclude:: Python/Example_code/fonctions.py

>>> execfile('fonctions.py')
>>> ma_fonction(3)
9.0
>>> ma_fonction(5.)
25.0
>>> ma_fonction(5., k = 5)
125.0
>>> help(ma_fonction)


Classes
-------

On crée un fichier :download:`classes.py <Python/Example_code/classes.py>` dans lequel on définit une classe de vecteurs qui permet de faire très facilement les opérations usuelles sur les vecteurs:

.. literalinclude:: Python/Example_code/classes.py


>>> execfile('classes.py')
>>> v = vecteur(1, 0, 0)
>>> v
<vecteur: (1.0, 0.0, 0.0)>
>>> v + 4
<vecteur: (5.0, 4.0, 4.0)>
>>> w = vecteur(0, 1, 0)
>>> v + w
<vecteur: (1.0, 1.0, 0.0)>
>>> v * w
<vecteur: (0.0, 0.0, 1.0)>
>>> v.scalaire(w)
0.0
>>> q = v + w
>>> q
<vecteur: (1.0, 1.0, 0.0)>
>>> q.norme()
1.4142135623730951
>>> k = vecteur(2, 5, 6)
>>> k.normaliser()
>>> k
<vecteur: (0.248069469178, 0.620173672946, 0.744208407535)>
>>> k.norme()
1.0

Fichiers
--------

On veut lire le fichier de données :download:`data.txt <Python/Example_code/data.txt>` qui comporte 2 colonnes et un nombre de lignes inconnues. La première colonne contient le temps et la seconde une amplitude qui évolue avec le temps. On peut construire une fonction dans le fichier `fichier.py <Python/Example_code/fichier.py>`_  qui permet de charger les donnnées contenues dans le fichier comme suit:


.. literalinclude:: Python/Example_code/fichier.py


Modules
+++++++++++++++++++++++

Les outils présents dans Python ont vocation à être très généralistes. De très nombreux outils orientés vers des applications particulières existes mais ils ne font pas directement partie du Python, ils sont alors disponibles sous forme de modules ou de packages. A titre d'exemple, si on cherche à utiliser des fonctions mathématiques de base dans Python, on remarque qu'elles n'existent pas:

>>> pi
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pi' is not defined
>>> sin(0.)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sin' is not defined

Cependant, elles sont disponibles dans le module math qui est toujours présent dans Python sans installation supplémentaire (math est un module *built-in*). On peut donc aller chercher ces outils de la manière suivante:

>>> from math import sin, pi
>>> pi
3.141592653589793
>>> sin(pi)
1.2246467991473532e-16
>>> import math
>>> math.pi
3.141592653589793
>>> math.sin
<built-in function sin>

Dans cette partie, on présent les modules indispensables à une bonne utilisation de Python dans une optique d'ingénieur.

Numpy
-----

`Numpy <http://scipy.org/Tentative_NumPy_Tutorial>`_ est un module de calcul matriciel, il rend Python comparable à *Matlab*. Il est téléchargeable depuis son site officiel et ou installable depuis les dépots de paquets sous Linux. Numpy est incontournable pour toutes les opérations qui peuvent être mises sous forme matricielle ou vectoriel pour lesquels il offre une facilité et une vitesse impossible autrement sous Python. L'essence de numpy est la classe ``array`` qui ressemble à une liste a un comportement très différent vis-à-vis des opérateurs mathématiques. De plus, elle est très adaptée au stockage massif de donnée de même type.


>>> ma_liste = [1., 3., 5., 10. ] # Une liste
>>> ma_liste + ma_liste
[1.0, 3.0, 5.0, 10.0, 1.0, 3.0, 5.0, 10.0] # Somme de liste = concaténation
>>> ma_liste*2
[1.0, 3.0, 5.0, 10.0, 1.0, 3.0, 5.0, 10.0] # Produit liste * entier: concaténation
>>> import numpy as np # On import numpy et on le renomme np par commodité.
>>> mon_array = np.array(ma_liste) # On crée un array à partir de la liste.
>>> mon_array
array([  1.,   3.,   5.,  10.])
>>> mon_array * 2 # array * entier = produit terme à terme
array([  2.,   6.,  10.,  20.])
>>> mon_array +5 # array + array = somme terme à terme
array([  6.,   8.,  10.,  15.])
>>> mon_array.sum() # Somme du array
19.0
>>> mon_array.mean() # Valeur moyenne
4.75
>>> mon_array.std() # Ecart type
3.344772040064913
>>> np.where(mon_array  > 3., 1., 0.) # Seuillage
array([ 0.,  0.,  1.,  1.])

Scipy
-----

`Scipy <http://www.scipy.org/Cookbook>`_ (pour Scientific Python) contient un grand nombre d'algorithme classiques en méthodes numériques implémentés en Python de manière performante. 

Matplotlib
-----------

`Matplotlib <http://matplotlib.org/>`_ est un module de graphisme qui produit des figures de grande qualité dans tous les formats utiles. Voici quelques exemples:

* Tracé d'une courbe :math:`y = \frac{\sin( 2 \pi x)}{x}`:

.. plot:: Python/Example_code/matplotlib_courbe.py
    :include-source: 
    
* Tracé d'un champ :math:`z = \sin (2 \pi x) \sin (2 \pi y) / \sqrt{x^2 + y^2}`:

.. plot:: Python/Example_code/matplotlib_champ.py
    :include-source:
