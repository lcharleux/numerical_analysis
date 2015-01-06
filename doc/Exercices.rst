Exercices
___________________


TD 1 et 2
++++++++++


L'image suivante (:download:`superalliage.jpg <Traitement_images/Example_code/superalliage.jpg>`) représente met en évidence la microstructure d'un superalliage à base nickel (source: `Onera <http://www.onera.fr/images-science/materiaux-structures/superalliage-monocristallin-nickel.php>`_ ). On y met en évidence deux phases:

* Une matrice dite phase :math:`\gamma`: la plus sombre
* Des particules dites phase :math:`\gamma ^\prime` : plus claires.

.. image:: Traitement_images/Example_code/superalliage.jpg

On vous demande de faire un programme écrit en Python qui effectue les tâches suivantes:

1. Lire l'image et la convertire au format `numpy.array`. Bien que d'aspect grisatre, l'image est en couleur et comporte donc 3 canaux. Il convient donc de choisir le canal le plus avantageux.
2. Tracer l'histogramme de l'image et en déduire un moyen de séparer les deux phases.
3. Seuiller l'image de sorte à séparer les deux phases. On pourra remarquer que le microscope utilisé pour produire l'image induit un `vignetage <http://fr.wikipedia.org/wiki/Vignettage>`_ marqué qui fausse le seuillage. On pourra réflechir à des moyens de corriger cet artefact.
4. Calculer la proportion de chaque phase dans l'image.
5. Compter les particules de phase :math:`\gamma ^\prime`.
6. Déterminer la taille moyenne des particules.

TP
+++

On cherche à trouver la trajectoire la plus rapide entre deux points :math:`A` et :math:`B`. Ce problème peut être abordé par le biais des outils d'optimisation. On vous fournit une amorce de programme qui propose la solution basique de la ligne droite. On vous demande de construire un programme qui permet de trouver un trajet plus rapide. Votre programme sera votre compte rendu, prennez donc soin d'y mettre vos noms et de le commenter au maximum. Votre note dépend du bon fonctionnement de votre programme et la clarte de son écriture et des figures qu'il produit. Vous pouvez biensur vous inspirer des exemples présents dans le cours.

.. plot:: Optimisation/Example_code/chemin.py
    :include-source: 


