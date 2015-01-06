Images Numériques
___________________


Les images numériques sont des images décrites dans un format numérique. On peut les utiliser pour interpréter quantitativement certaines phénomènes qu'elles mettent en évidence. Cette partie dresse un rapide tableau des différentes approches basiques qui permettent d'effectuer ces tâches. 


Formation
+++++++++++++++++++

Une image est issue de la mesure d'un phénomène physique particulier par un dispositif adapté. On trouve ainsi des images de différentes natures:

* Lumière visible: `photographie <http://fr.wikipedia.org/wiki/Photographie>`_ , `microscopie optique <http://fr.wikipedia.org/wiki/Microscope_optique>`_.

* Lumière infrarouge: `thermographie <http://fr.wikipedia.org/wiki/Thermographie>`_.

* Electrons: `microscopie électronique <http://fr.wikipedia.org/wiki/Microscope_%C3%A9lectronique>`_.

* Topologie: `microscopie à force atomique <http://fr.wikipedia.org/wiki/Microscope_%C3%A0_force_atomique>`_.

* Et de nombreux autres...


Structure
++++++++++++++++++

Deux grandes familles d'images numériques existent:

* `Images vectorielles <http://fr.wikipedia.org/wiki/Image_vectorielle>`_ : elles constituées de figures géométriques (droites, polygones, ...). Elles sont idéales pour représenter des schémas et des courbes. 

* `Images matricielles <http://fr.wikipedia.org/wiki/Image_matricielle>`_ : elles sont constituées d'une matrice de **pixels**. Chaque pixel d'une même image porte le même type d'informations. Ces informations sont scindées en **canaux** chacun contenant un nombre qui peut être entier (généralement 8 bits) ou des flotant dans le cas d'images scientifiques. Il est important de noter que la couleur d'un pixel tel qu'il apparait quand on représente une image n'est pas associé de manière unique à l'information contenue dans le pixel. Par exemple, dans une photographie, on cherche à ce que la représentation du pixel soit fidèle à la vision humaine et donc on va donc la décomposer en 3 canaux (rouge, vert, bleu par exemple) avec eventuellement un quatrième canal destiné à coder la transparence. On parle alors d'image polychrome. A l'opposé dans une image à vocation scientifique, on cherchera généralement à quantifier un phénomème scientifique par un seul canal, si possible sous forme flotante. On parle alors d'image monochrome. 

On prend un exemple de photographie: :download:`laping.jpg <Traitement_images/Example_code/lapin.jpg>`

.. plot:: Traitement_images/Example_code/lapin.py
    :include-source: 

On s'intéresse maintenant uniquement à des images monochromes formées de nombres flotants. Ainsi si on dispose d'une photographie, on peut isoler un canal ou construire une combinaison quelquconque de canaux comme suit.

.. plot:: Traitement_images/Example_code/lapin_monochrome.py
    :include-source: 

Une image se résumera donc à une matrice :math:`Z_{ij}` où :math:`i` et :math:`j` sont les indices des pixels. Dans certains cas, on pourra ajouter des informations comme les coordonnées :math:`X_{ij}` et :math:`Y_{ij}` des pixels. Toutes ces matrices sont décrites dans le format Python ``numpy.array`` avec des pixels sous forme ``numpy.float64``.


Operations
+++++++++++

Histogramme
~~~~~~~~~~~~~~~~~~~~~~

A titre d'exemple, on travaille sur une image d'altitude de l'Europe (source: `European Environment Agency <http://www.eea.europa.eu/data-and-maps/data/digital-elevation-model-of-europe>`_ ) dans laquelle :math:`1 \; pixel = 1 \; km \times \; 1 \; km`.

.. plot:: Traitement_images/Example_code/europe.py
    :include-source: 

On peut alors se demander quelle surface du territoire européen est située dans telle bande d'altitudes de :math:`100m` de largeur..

.. plot:: Traitement_images/Example_code/europe_hist.py
    :include-source: 




Seuillage
~~~~~~~~~~~~~~~~~~~~~~

L'histogramme montre clairement que la majorité du territoire est située à :math:`Z \leq 100m`. En fait, les zones marines sont à une altitude :math:`Z = 0m` et contribuent grandement à cette grande surface. Le seuillage consiste à transformer une image monochrome en **image binaire** en appliquant un test booléen à chaque pixel. Une image binaire est ainsi formée de 0 et de 1 ou de **Vrai** et **Faux**. Dans le cas présent, on peut alors chercher à isoler la mer de la terre en effectuant un seuillage :math:`Z >0m` :

.. plot:: Traitement_images/Example_code/europe_seuillage.py
    :include-source: 


Erosion / Dilatation
~~~~~~~~~~~~~~~~~~~~~~

On souhaite mesurer la surface continentale Européenne à l'aide du seuillage effectué précédement. On remarque de nombreuses iles sont assimilés au continent, on souhaite les éliminer. Pour éliminer cet artefact, les outils issus de la `morphologie mathématique <http://fr.wikipedia.org/wiki/Morphologie_math%C3%A9matique>`_ tels que l'érosion et la dilatation sont particulièrement adaptés:


.. plot:: Traitement_images/Example_code/erosion_dilatation.py
    :include-source: 

On applique l'érosion-dilatation à la carte de l'Europe:

.. plot:: Traitement_images/Example_code/europe_ED.py
    :include-source: 

Comptage
~~~~~~~~~~~~~~~~~~~~~~

Si on cherche maintenant a extraire les différents zones distinctes (iles et continents), il faut trouver tous les pixels appartenant à la terre :math:`Z = 1` qui sont voisins. Le comptage de zones dans une image binaire peut se faire par des `algorithmes dédiés <http://en.wikipedia.org/wiki/Connected-component_labeling>`_ . Voici un exemple:

.. plot:: Traitement_images/Example_code/europe_comptage.py
    :include-source: 
    
Recherche de contours
~~~~~~~~~~~~~~~~~~~~~~

Si on cherche maintenant à trouver les cotes européennes, il faut rechercher les contours terres. Pour ce faire le laplacien donne de bons résultats:

.. plot:: Traitement_images/Example_code/europe_contours.py
    :include-source: 
    
Les performances de la détection sont meilleures avec un filtre dédié comme le `filtre de Canny <http://fr.wikipedia.org/wiki/Filtre_de_Canny>`_ .


