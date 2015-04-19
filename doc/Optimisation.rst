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









