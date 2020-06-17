# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 13:01:27 2018

@author: HP
"""

import numpy as np
import matplotlib.pyplot as plt

delta_t=0.1
t=0
x=1
y=1
w0=1

for i in range(100):
    k1x=delta_t*y #primera pendiente 
    k1y=delta_t*(-w0**2*x)
    k2x=delta_t*(y+k1y/2) #método runge-kutta orden 2
    k2y=delta_t*(-w0**2*(x+k1x/2))
    t=t+delta_t
    y=y+k2y
    x=x+k2x
    plt.plot(x,y,'*')
    plt.xlabel('x')
    plt.ylabel('y')
    