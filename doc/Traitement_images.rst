Images Numériques
___________________


Les images numériques sont des images décrites dans un format numérique. On peut les utiliser pour interpréter quantitativement certaines grandeurs. Cette partie dresse un rapide tableau des différentes approches basiques qui permettent d'effectuer ces tâches et donne des pistes pour aller plus loin sur chaque thème abordé.

Les points abordés ici sont détaillés plus finement dans le cours: :download:`Traitement_Signal_slides.pdf <Traitement_images/Slides/Traitement_Images_slides.pdf>` 

Formation
----------------

Selon le dispositif qui l'a produite, le sens physique des informations contenues dans une image est différent. Voici quelques exemples d'images classées par type d'informations:

* Lumière visible: `photographie <http://fr.wikipedia.org/wiki/Photographie>`_ , `microscopie optique <http://fr.wikipedia.org/wiki/Microscope_optique>`_.

* Lumière infrarouge: `thermographie <http://fr.wikipedia.org/wiki/Thermographie>`_.

* Electrons: `microscopie électronique <http://fr.wikipedia.org/wiki/Microscope_%C3%A9lectronique>`_.

* Topologie: `microscopie à force atomique <http://fr.wikipedia.org/wiki/Microscope_%C3%A0_force_atomique>`_.

* Et de nombreux autres...


Structure
---------------

Deux grandes familles d'images numériques existent:

* `Images vectorielles <http://fr.wikipedia.org/wiki/Image_vectorielle>`_ : elles constituées de figures géométriques (droites, polygones, ...). Elles sont idéales pour représenter des schémas et des courbes. 

* `Images matricielles <http://fr.wikipedia.org/wiki/Image_matricielle>`_ : elles sont constituées d'une matrice de **pixels**. Chaque pixel d'une même image porte le même type d'informations. Ces informations sont scindées en **canaux** chacun contenant un nombre qui peut être entier (généralement 8 bits) ou des flottant dans le cas d'images scientifiques. Il est important de noter que la couleur d'un pixel tel qu'il apparait quand on représente une image n'est pas associé de manière unique à l'information contenue dans le pixel. Par exemple, dans une photographie, on cherche à ce que la représentation du pixel soit fidèle à la vision humaine et donc on va donc la décomposer en 3 canaux (rouge, vert, bleu par exemple) avec eventuellement un quatrième canal destiné à coder la transparence. On parle alors d'image polychrome. A l'opposé dans une image à vocation scientifique, on cherchera généralement à quantifier un phénomème scientifique par un seul canal, si possible sous forme flottante. On parle alors d'image monochrome. 

On prend un exemple de photographie: :download:`grenouille.jpg <Traitement_images/data/grenouille.jpg>`

.. plot:: Traitement_images/Example_code/grenouille.py
    :include-source: 

On s'intéresse maintenant uniquement à des images monochromes formées de nombres flottants. Ainsi si on dispose d'une photographie, on peut isoler un canal ou construire une combinaison quelquconque de canaux comme suit.

.. plot:: Traitement_images/Example_code/grenouille_canaux.py
    :include-source: 

Une image se résumera donc à une matrice :math:`Z_{ij}` où :math:`i` et :math:`j` sont les indices des pixels. Dans certains cas, on pourra ajouter des informations comme les coordonnées :math:`X_{ij}` et :math:`Y_{ij}` des pixels. Toutes ces matrices sont décrites dans le format Python ``numpy.array`` avec des pixels sous forme ``numpy.float64``.


Operations
-----------------

Dans cette partie, nous utiliserons aussi une image générée pour l'occasion:

.. plot:: Traitement_images/Example_code/generate_image.py
     
Vous pouvez télécharger l'image ici: :download:`image.jpg <Traitement_images/Slides/figures/image.jpg>` 

Lecture
********

.. plot:: Traitement_images/Example_code/grenouille.py
    :include-source:

Sauvegarde
************

.. plot:: Traitement_images/Example_code/grenouille_save.py
    :include-source:


Rognage
**********

.. plot:: Traitement_images/Example_code/grenouille_crop.py
    :include-source:

Rotations
************

.. plot:: Traitement_images/Example_code/grenouille_rotate.py
    :include-source:

Histogramme
**************

Un histogramme représente la répartition de la population de pixels en fonction de leur altitude. Une valeur haute dans l'histogramme indique donc qu'un grand nombre de pixels correspondent à l'altitude considérée.

.. plot:: Traitement_images/Example_code/image_hist.py
    :include-source: 




Seuillage
*************

L'histogramme montre deux pics (:math:`Z = 20` et :math:`Z = 230`) correspondant à deux populations de pixels. Le seuillage consiste à transformer une image monochrome en une **image binaire** en appliquant un test booléen à chaque pixel. Une image binaire, c'est-à-dire formée de 0 et de 1 ou de **Vrai** et **Faux** est ainsi créé. Dans le cas présent, on peut alors chercher séparer les deux populations en effectuant un seuillage :math:`Z > 120` :

.. plot:: Traitement_images/Example_code/image_seuillage.py
    :include-source: 


Erosion / Dilatation
********************

On souhaite mesurer éliminer le bruit révélé par le seuillage effectué précédement. Pour ce faire, les outils issus de la `morphologie mathématique <http://fr.wikipedia.org/wiki/Morphologie_math%C3%A9matique>`_ tels que l'érosion et la dilatation sont particulièrement adaptés:


.. plot:: Traitement_images/Example_code/image_erosion.py
    :include-source: 

Pour restaurer la surface des zones partiellement érodées, on applique une dilatation:

.. plot:: Traitement_images/Example_code/image_dilatation.py
    :include-source: 

Comptage
***********

Si on cherche maintenant a identifier individuellement les zones blanches mises en évidence lors du seuillage, il faut trouver tous les pixels appartenant à la terre :math:`Z = 1` qui sont voisins. Le comptage de zones dans une image binaire peut se faire par des `algorithmes dédiés <http://en.wikipedia.org/wiki/Connected-component_labeling>`_ . Voici un exemple:

.. plot:: Traitement_images/Example_code/image_comptage.py
    :include-source: 
    
Recherche de contours
**************************

Si on cherche maintenant à trouver les contours des zones blanches. On peut combiner les opérateurs de dérivation:

.. plot:: Traitement_images/Example_code/image_contours.py
    :include-source: 
    
Les performances de la détection sont meilleures avec un filtre dédié comme le `filtre de Canny <http://fr.wikipedia.org/wiki/Filtre_de_Canny>`_ .


Travaux Dirigés
-----------------
     
On vous propose de travailler sur l'image  `suivante: <http://www.onera.fr/sites/default/files/actualites/magazine/image_du_mois/sinb-microstruture-eutectique-2.jpg>`_  (`source <http://www.onera.fr/fr/imagedumois/dendrites>`_ ). On vous demande de faire un programme qui effectue les tâches suivantes:

1. Lire l'image et la convertire au format `numpy.array`. Bien que d'aspect grisatre, l'image est en couleur et comporte donc 3 canaux. Il convient donc de choisir le canal le plus avantageux.
2. Rogner séparer l'image en deux parties pour séparer le bandeau inférieur de l'image elle même.
3. Tracer l'histogramme de l'image et en déduire un moyen de séparer les deux phases.
4. Calculer la proportion de particules dans l'image.
5. Compter les particules.
6. Déterminer la taille moyenne des particules.

Travaux Pratiques
-----------------

On vous demande de travailler sur une grille d'altitude de l'Euroe (télécharger `europe.tif <http://www.eea.europa.eu/data-and-maps/figures/elevation-map-of-europe>`_). La grille comporte des pixels représentant 1 km de coté. On vous fournit une amorce de programme `ici <Traitement_images/Example_code/europe.py>`_ :

1. Qelle est la surface de terre présente sur la carte ?
2. Dans cette surface de terre, quelle est la proportion d'iles ?
3. Parmi les iles, quelles sont les 5 lus grandes dans l'ordre ?
4. Quelle ile a la plus grande altitude moyenne ?
5. Quelle proportion de surface de terre perdrait l'Europe si le niveau de la mer montait de 10 m. Même question pour 50 m.
6. Quelle ile a la plus grande longueur de côtes ramenée à sa surface ? Ce résultat est-il discutable ?
7. Quelle est l'ile la plus étendue d'est en ouest ?



