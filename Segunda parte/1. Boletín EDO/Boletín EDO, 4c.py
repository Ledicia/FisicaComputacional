# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 19:38:10 2018

@author: Ledicia Díaz
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


sigma=3
r=26.5
b=1
x=0
y=1
z=0
t=0
delta_t=0.01

fig=plt.figure()
ax = fig.add_subplot(111,projection='3d') #para plotear en 3D

for i in range(1000):
    t+=delta_t
    k1x=delta_t*(sigma*(y-x))
    k1y=delta_t*(r*x-y-x*z)
    k1z=delta_t*(x*y-b*z)
    k2x=delta_t*(sigma*(y+k1y/2-(x+k1x/2)))
    k2y=delta_t*(r*(x+k1x/2)-(y+k1y/2)-(x+k1x/2)*(z+k1z/2))
    k2z=delta_t*((x+k1x/2)*(y+k1y/2)-b*(z+k1z/2))
    k3x=delta_t*(sigma*(y+k2y/2-(x+k2x/2)))
    k3y=delta_t*(r*(x+k2x/2)-(y+k1y/2)-(x+k2x/2)*(z+k2z/2))
    k3z=delta_t*((x+k2x/2)*(y+k2y/2)-b*(z+k2z/2))
    k4x=delta_t*(sigma*(y+k3y)-(x+k3x))
    k4y=delta_t*(r*(x+k3x)-(y+k3y)-(x+k3x)*(z+k3z))
    k4z=delta_t*((x+k3x)*(y+k3y)-b*(z+k3z))
    x+=k2x
    y+=k2y
    z+=k2z
    ax.scatter(x,y,z)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.title('Ejercicio 4, Euler')
plt.show()
