# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 12:42:33 2018

@author: Ledicia Díaz
"""
import numpy as np
import matplotlib.pyplot as plt

delta_t=0.01
t=0
x=1
y=1
w0=1
b=0
w=1
F=0
x0=1
y0=1
for i in range(1000):
    x=x0+delta_t*y0
    y=y0+delta_t*(-b*y0-w0**2*x0+F*np.cos(w*t))
    t=delta_t+t
    x0=x
    y0=y
    
    plt.plot(x,y,"+")