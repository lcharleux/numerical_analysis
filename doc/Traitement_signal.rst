Traitement de signal
_________________________

Cette partie du cours aborde les notions basiques sur:

* Ce qu'est un signal.
* Les conséquences de son enregistrement dans un format numérique.
* L'analyse fréquentielle de son contenu.

Les points abordés ici sont détaillés plus finement dans le cours: :download:`Traitement_Signal_slides.pdf <Traitement_signal/Slides/Traitement_Signal_slides.pdf>` 

Signal
---------

Un signal undimensionnel peut être vu comme une fonction mathématique du type:

.. math::

   x: \; t \mapsto x(t)

Le signal sera périodique si il existe une période :math:`T` telle que:

.. math::

   \forall t, \; x(t + T) = x(t)

On définit alors sa fréquence :math:`f = 1/T`. Dans le cas général, un signal quelconque pourra toujours être vu comme une somme de plusieurs signaux (ou composantes) périodiques. 

Observation du signal
----------------------

Pour des raisons pratiques, il est impossible d'observer un signal pour toutes les valeur de :math:`t`. On observe donc uniquement le signal entre :math:`t_0` et :math:`t_1`. On définit alors la durée d'observation :math:`D = t_1 -t_0`. 



Echantillonnage
---------------

Principe
***********

Pour enregistre un signal dans un format numérique, on mesure ses valeurs sur une grille de points :math:`[t_i]` avec :math:`i \in [0, N-1]`, c'est `l'échantillonnage <http://fr.wikipedia.org/wiki/%C3%89chantillonnage_%28signal%29>`_. On enregistre donc :math:`N` valeurs. Une grande quantité d'information est donc perdue par ce procédé. On définit aussi la fréquence d'échantillonnage:

.. math::

   f_e = \frac{N-1}{D}

Dans l'exemple ci-dessous, les pastilles rouges représentent les points pour lesquelles les valeurs du signal réel sont enregistrées. On remarque les pastilles rouges décrivent bien la forme du signal réel, l'échantillonnage est donc réussi.

.. plot:: Traitement_signal/Example_code/sampling_ex0.py
    :include-source: 

Théorème de Shannon-Nyquist
***************************

Le  `théorème de Shannon Nyquist <http://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_d%27%C3%A9chantillonnage_de_Nyquist-Shannon>`_ indique que la fréquence :math:`f` du signal (ou celles de ses composantes) doit vérifier:

.. math::

   f < \frac{f_e}{2}

Le cas extr^eme où :math:`f = f_e/2` est représenté ci-dessous.

.. plot:: Traitement_signal/Example_code/sampling_shannon.py
    :include-source: 

Repliement de spectre
**********************

La figure ci-dessus laisse penser que si la fréquence du signal ne respecte pas le théorème de Shannon-Nyquist, alors le signal est perdu lors de l'échantillonnage. En réalité, le signal apparait comme ayant une fréquence différente comme le montre la figure ci-dessous.

.. plot:: Traitement_signal/Example_code/sampling_aliasing.py
    :include-source:  

Pour échantillonner un signal, il est donc essentiel de retirer préalablement les composantes de fréquence :math:`f \geq f_e/2` à l'aide d'un filtre anti repliement.

Analyse Spectrale
-----------------------

Principe  
***********

L' `analyse spectrale <http://fr.wikipedia.org/wiki/Analyse_spectrale>`_ d'un signal consiste à construire son spectre, c'est-à-dire sa décomposition sous forme d'une somme fonctions périodiques. Plusieurs outils existent selon le type de signal étudié. Dans la pratique, nous allons travaillons toujours avec des signaux apériodiques échantillonnés, l'outil de base de base pour construire le spectre est la `Transformé de Fourier Discrète (DFT) <http://fr.wikipedia.org/wiki/Transformation_de_Fourier_discr%C3%A8te>`_ ou son implémentation rapide, la `FFT <http://fr.wikipedia.org/wiki/Transformation_de_Fourier_rapide>`_ . En python, le moyen le plus simple pour accéder aux algorithmes de FFT est `scipy <https://scipy-lectures.github.io/intro/scipy.html#fast-fourier-transforms-scipy-fftpack>`_ . L'algorithem FFT impose que le nombre d'échantillon :math:`N` soit une puissance de 2.

Dans la pratique la FFT d'un signal :math:`x` se présente de la manière suivante:

>>> from scipy import fftpack
>>>  X = fftpack.fft(x)

Le vecteur :math:`X` est composé de :math:`N` coefficients complexes. La première moitié des coefficients du vecteur :math:`X` correspondent aux fréquences positives et la seconde aux fréquences négatives.

>>> Xpos = X[0:N/2] # Coefficients correspondant aux frequences positives
>>> Xneg = X[N/2:N] # Coefficients correspondant aux frequences negatives

Dans notre cas, le signal :math:`x` étant réel, les coefficients correspondant aux fréquences négatives sont les conjugués des coefficients correspondant aux fréquences positives, ils n'apportent donc pas d'information utile. 

Le vecteur fréquence :math:`f` correspondant au vecteur :math:`X` comporte :math:`N` coefficients se répartissant entre :math:`-f_e/2` et :math:`f_e/2`. Dans la pratique, il n'est pas intéressant de tracer les fréquences négatives, nous pouvons donc tracer un signal et son spectre de la manière suivante:

.. plot:: Traitement_signal/Example_code/FFT_ex0.py
    :include-source:  


Interprétation
****************

* Effet de la fréquence:

.. plot:: Traitement_signal/Example_code/exemple_FFT_frequence.py
     

Travaux dirigés
_________________

Ce sujet est une introduction aux questions abordées dans ce cours. On vous demande d'écrire un (ou plusieurs) scripts qui pour effectuer les tâches suivantes:

#. Signal sinusoidal

  #. Générer un signal sinusoidal de la forme :math:`x(t) = a  \sin (2 \pi f t + \phi)`.
  #. Construire une grille d'échantillonnage :math:`t` pour laquelle on peut contrôler la fréquence d'échantillonnage :math:`f_e` et la durée d'observation :math:`D`.
  #. Tracer le signal échantillonné.
  #. Que se passe-t-il quand on augmente la fréquence du signal :math:`f` en laissant :math:`f_e` constante.
  #. Calculer la transfromée de Fourier par FFT :math:`X` des coefficients :math:`x`.
  #. Calculer les fréquences positives.
  #. Tracer le spectre du signal.
  #. Expliquer l'influence de :math:`a` , :math:`f` et :math:`\phi` sur le spectre.

#. Autres signaux
  
  #. Réutilisez le code produit dans les questions précédentes et appliquez le à un signal carré.
  #. Même démarche pour un signal constant.
  #. Même démarche pour une gaussienne.
  






