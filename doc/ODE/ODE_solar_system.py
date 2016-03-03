# -*- coding: utf-8 -*-
"""
A Solar System class
"""

import numpy as np
import matplotlib.pyplot as plt
# from scipy.integrate import odeint # You may need this

def Euler(func, y0, t):
  dt = t[1] - t[0]
  nt = len(t)
  Y  = np.zeros([nt, len(y0)])
  Y[0] = y0
  for i in xrange(nt-1):
    Y[i+1] = Y[i] + func(Y[i], t[i]) * dt
  return Y


class System(object):
  def __init__(self, m, p, v, nk = 50000, G = 6.67e-11):
    """
    2D solar system
    
    * m: mass vector
    * p: position vector    
    * v: velocity vector
    * G: gravity constant
    * nk: number of points in the trail 
    """
    n = len(p)
    self._n = n
    self.Y = np.zeros([nk, 4 * n])
    self.Y.fill(np.NAN)
    self.Y[-1, :2 * n] = np.array(p).flatten()
    self.Y[-1, 2 * n:] = np.array(v).flatten()
    self.m  = np.array(m)
    self.nk = nk
    self.G  = G
  
  def derivative(self, y, t):
    """
    Acceleration of each mass
    """      
    m, G = self.m, self.G
    n = len(m)
    p = y[:2 * n ].reshape(n ,2)
    v = y[ 2 * n:].reshape(n ,2)
    a = np.zeros_like(p) # vecteur plein de zeros dans le mm format que p
    n = len(m) # nombre de masses
    for i in xrange(n): # On s'intéresse à la masse i
      for j in xrange(n): # Les masses j agissent dessus   
        if i != j: # i ne doit pas agir sur i !
           PiPj = p[j] - p[i]
           rij = (PiPj**2).sum()**.5
           if rij != 0. :           
             a[i] += G * m[j] * PiPj / rij**3
    y2 = y.copy()
    y2[:2*n ] = v.flatten()
    y2[ 2*n:] = a.flatten()
    return y2       
    
  
  def solve(self, dt, nt, solver = Euler):
    """
    ODE solving
    """
    time = np.linspace(0., dt, nt + 1)
    Ys = solver( self.derivative, self.Y[-1], time)
    nk = self.nk
    Y = self.Y
    Y[:nk - nt] = Y[nt:]
    Y[-nt-1:] = Ys 
    self.Y    = Y
  
  def position(self):
    """
    Position of each mass
    """
    n = self._n
    p = self.Y[-1,:2 * n].reshape(n, 2)
    return p[:,0], p[:,1]
   
  def speed(self):
    """
    Speed of each mass
    """
    n = self._n
    v = self.Y[-1,2 * n:].reshape(n, 2)
    return v[:,0], v[:,1]
    
  def Ec(self):
    """
    Kinetic energy of each mass
    """
    vx , vy = self.speed()
    m = self.m
    Ec = .5 * m * (vx**2 + vy**2)
    return Ec
  
  def Ep(self):
    """
    Potential energy of each mass
    """
    m, G = self.m, self.G
    n = len(m)
    y = self.Y[-1]
    p = y[:2 * n ].reshape(n ,2)
    Ep = np.zeros_like(m) # vecteur plein de zeros dans le mm format que p
    n = len(m) # nombre de masses
    for i in xrange(n): # On s'intéresse à la masse i
      for j in xrange(n): # Les masses j agissent dessus   
        if i != j: # i ne doit pas agir sur i !
           PiPj = p[j] - p[i]
           rij = (PiPj**2).sum()**.5
           if rij != 0. :           
             Ep[i] -= G * m[j] * m[i] / rij   
    return Ep
  
  def Em(self):
    """
    Mechanical energy of each mass
    """
    return self.Ep() + self.Ec()
    
  
  def trail(self, i):
    n = self._n
    Y = self.Y
    return Y[:, 2*i], Y[:, 2*i +1 ]
    

