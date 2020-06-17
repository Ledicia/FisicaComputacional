# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 18:11:28 2018

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
    x+=delta_t*(sigma*(y-x))
    y+=delta_t*(r*x-y-x*z)
    z+=delta_t*(x*y-b*z)
    ax.scatter(x,y,z,'*')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.title('Ejercicio 4, Euler')
plt.show()


