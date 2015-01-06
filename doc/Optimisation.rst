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


Regressions
++++++++++++

Ici on cherche à représenter un groupe de points par une fonction dont certains paramètres sont ajustables. 

.. plot:: Optimisation/Example_code/regression.py
    :include-source: 



Algorithmes
===========

De nombreux algorithmes sont dédiés à l'optimisation. Le choix d'un de ces algorithmes se fait en fonction du problème. Voici les deux qu'il est essentiel de connaître:

* `Nelder-Mead <http://fr.wikipedia.org/wiki/M%C3%A9thode_de_Nelder-Mead>`_ (NM): algorithme ancien mais généraliste. Dans scipy, voir: `scipy.optimize.fmin` (`doc <http://docs.scipy.org/doc/scipy-0.7.x/reference/generated/scipy.optimize.fmin.html>`_ )
* `Levenberg-Marquardt <http://fr.wikipedia.org/wiki/Algorithme_de_Levenberg-Marquardt>`_ (LM): algorithme de référence pour la minimisation aux moins carrés. Dans scipy, voir: `scipy.optimize.leastsq` (`doc <http://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.leastsq.html>`_ )






