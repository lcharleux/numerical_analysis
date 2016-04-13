
Optimization: Practical work
============================

This tutorial aims at working on the optimization of truss type
mechanical structures. Therefore, you will use the following library
called `truss <http://truss.readthedocs.org/en/latest/index.html>`__.

Questions:

1. Firsty, install the package and try it,
2. The following structure (see below) aims at carrying a load
   :math:`F = 10` kN. All beams are made of steel with the following
   properties:

-  Young's modulus :math:`E = 210` GPa,
-  Density :math:`\rho = 7800` kg/m\ :math:`^3`,
-  Cross section :math:`S = 1` cm\ :math:`^2`,
-  Yield stress :math:`\sigma_{y} = 400` MPa.

3. Verify that the yield stress is not exceeded anywhere, do you think
   this structure has an optimimum weight ?
4. Modify all the sections at the same time in order to minimize weight
   while keeping acceptable stress level,
5. Modify the position along the :math:`\vec y` axis of the points
   :math:`D`, :math:`F` and :math:`H` in order to optimize the stiffness
   *vs.* mass ratio of the structure. Do not further modify the sections
   determined in question 4. Comment the solution.
6. Same question with displacements also along :math:`\vec x` of
   :math:`C`, :math:`D`, :math:`E` and :math:`F`. Is it better ?
7. You are now asked to optimize the cross section along with the
   position of :math:`C`, :math:`D`, :math:`E` and :math:`F` in order to
   reach the yield stress in each individual beam.
8. You are now asked to perform topological optimization by
   removing/merging well chosen beams and nodes.

