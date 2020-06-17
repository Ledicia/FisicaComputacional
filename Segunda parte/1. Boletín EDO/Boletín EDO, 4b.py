# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 19:29:14 2018

@author: Ledicia Díaz
"""
import numpy as np
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
ax = fig.add_subplot(1,1,1,projection='3d') #para plotear en 3D

for i in range(1000):
    t+=delta_t
    k1x=delta_t*(sigma*(y-x))
    k1y=delta_t*(r*x-y-x*z)
    k1z=delta_t*(x*y-b*z)
    k2x=delta_t*(sigma*(y+k1y/2-(x+k1x/2)))
    k2y=delta_t*(r*(x+k1x/2)-(y+k1y/2)-(x+k1x/2)*(z+k1z/2))
    k2z=delta_t*((x+k1x/2)*(y+k1y/2)-b*(z+k1z/2))
    x+=k2x
    y+=k2y
    z+=k2z
    ax.scatter(x,y,z,'*')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.title('Ejercicio 4, Euler')
plt.show()
