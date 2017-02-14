
Ordinary Differential Equations : Pendulum
==========================================

.. figure:: https://upload.wikimedia.org/wikipedia/commons/f/fa/PenduloTmg.gif
   :alt: Simple pendulum

   pendulum

.. code:: python

    # Setup
    %matplotlib nbagg
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.integrate import odeint


Part 1: Theory
--------------

-  Find the ODE followed by :math:`\theta`.

.. math::


   \dot \theta = \ldots

Part 2: Reformulation
---------------------

-  Reformulate the equation in order to match the standard formulation:

.. math::


   X = \begin{bmatrix} \ldots \end{bmatrix}

.. math::


   \dot X = f(X, t) = \ldots

-  Write the function :math:`f` in Python

.. code:: python

    def f(X, t):
        """
        ...
        """
        return

Part 3: Numerical solution
--------------------------

Solve the problem with Euler, RK4 and ODEint integrators and compare the
results.


Part 4: Energies an errors
--------------------------

Calculate and plot the kinetic energy :math:`E_c`, the potential energy
:math:`E_p` and the total energy :math:`E_t = E_c + E_p` for all 3
cases, plot it and comment.

