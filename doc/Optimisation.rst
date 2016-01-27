Optimisation
____________

Introduction
=============

L'optimisation consiste à minimiser une fonction coût :math:`f` typiquement de la forme:

.. math::

  f: X \mapsto e
  
 
Avec :math:`X \in R^n` et :math:`e \in R`. Le problème peut aussi comporter des contraintes sur :math:`X`. On peut mieux comprendre les applications au travers de quelques exemples. 

Treillis
++++++++

On s'intéresse à un treillis à 2 barres :math:`AB` et :math:`CB` articulées autour de 3 points :math:`A`, :math:`B` et :math:`C` de coordonnées respectives :math:`(x_A, y_A)`, :math:`(x_B, y_B)` et :math:`(x_C, y_C)`. On fait les hypothèses suivantes:

* Les points :math:`A` et :math:`C` sont fixes.
* Le point :math:`B` est mobile. On note :math:`B_0` sa position initiale et :math:`C_f` sa position finale.
* On néglige le poids des barres elles mêmes et on suspend une masse :math:`m` au point :math:`B`. On suppose que la gravité est selon :math:`-\vec y` et d'amplitude :math:`g`.
* Les barres se comportent comme des ressorts de raideur :math:`k` et dont la longueur au repos est celle spécifiée dans les conditions initiales.

On peut alors calculer l'énergie potentielle globale de pesanteur et de déformation:

.. math::

  E_p = \frac{k}{2} \left[  (AB_0 - AB)^2 + (CB_0 - CB)^2\right] + mgy_c

Le problème peut donc être vu comme la minimisation d'une fonction scalaire (*i. e.* :math:`E_p`) de la position du point :math:`B` dans le plan.

.. plot:: Optimisation/Example_code/treillis.py
    :include-source: 






Algorithmes
===========

Le choix d'algorithmes de résolution des problèmes d'optmisation est asssez vaste. Plusieurs critères de choix sont utilisés, dans la pratique les principaux seront:

* La présence ou non de contraintes.
* La présence de bruit sur la fonctionnelle.

Le site `scipy lectures <http://scipy-lectures.github.io/advanced/mathematical_optimization/>`_ fournit des explications pratiques pour effectuer ces choix. De plus, vous avez à tous ces algorithmes de manière identique au travers de  la fonction `minimize <http://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html#scipy.optimize.minimize>`_ .


Travaux Dirigés
=================

Dans le cadre du TD dédié à l'optimisation, vous allez travailler sur un problème très classique dans ce domaine, la régression.

1. Ecrivez une fonction mathématique :math:`g(x, a, b)` où :math:`x` est la variable et :math:`(a,b)` des paramètres de votre choix.
2. Evaluez cette fonction sur une grille de points :math:`X`, les valeurs associées seront notées :math:`Y = g(X, a_0, b_0)` 
3. Ecrivez une fonctionnelle :math:`f` qui décrit l'erreur aux moindre carrés entre les les points précalculés et :math:`Y` et la fonction :math:`g` évaluée sur :math:`X` pour un autre set de paramètres :math:`(a,b)` .
4. Retrouvez vos paramètres initiaux par optmimisation.
5. Ajoutez du bruit à :math:`Y` et recommencez.    

Travaux Pratiques
===================

Ce TP vous propose de travailler sur l'optimisation de structures mécaniques type treillis. Pour ce faire, vous allez utiliser le package `truss <http://truss.readthedocs.org/en/latest/index.html>`_ dédié à ces problèmes. 

1. Installez le package ``truss`` et prennez le en main.
2. La structure ci-dessous est une poutre qui supporte une charge de :math:`F = 10\; kN` en son milieu au niveau du point :math:`G`. Les poutres sont constituées d'un acier qui a les propriétés suivantes: 

  * Le module de Young du matériau utilisé est :math:`E = 210\; GPa`
  * La masse volumique du matériau utilisé est :math:`\rho = 7800\; kg/m^3`
  * La section des poutres est :math:`S = 1\; cm^2`
  * La limite d'élasticité pratique est :math:`R_{pe} = 400\; MPa`

.. image:: Optimisation/Example_code/treillis.png

3. Vérifiez que la limite d'élasticité n'est pas dépassée. La structure est elle optimale en terme de de poids ? Notez bien le poids de la structure.
4. Peut on jouer sur globalement sur la section des poutres pour alléger la structure. Si oui, mettez votre méthode en place et notez le poids obtenu.       
5. Modifiez la position selon :math:`\vec y` des points D, F et H pour optimiser la raideur massique de la structure sans modifier la section des poutres otenue en 4. Que pensez vous du résultat ?
6. Même question en modifiant aussi les positions horizontales des points C, D, E et F. Commentez le résultat.
7. On vous demande maintenant d'optimisez individuellement la section des poutres de la structure obtenue en 7 pour que la limite d'élasticité soit approcher au mieux dans chaque poutre. 
8. Recherchez des formes de structures plus optimisées en changeant le nombre de noeuds et leur positions.


    







