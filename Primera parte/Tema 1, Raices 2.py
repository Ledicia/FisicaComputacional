# -*- coding: utf-8 -*-
"""
Created on Thu Feb 01 13:44:17 2018

@author: Ledicia Diaz
"""
import numpy as np
import matplotlib.pylab as plt

def funcion(x):
    y=x**2-3*x+ np.exp(x)-2
    return y

xmin, xmax=-2.0, 4.0
ninter=20
x=np.linspace(xmin, xmax, ninter+1)
y=funcion(x)

n=0
for i in range(1, ninter+1):
    if np.sign(y[i-1])!=np.sign(y[i]):
        n+=1
        print('raiz %d:intervalo (%f,%8.2f)' %(n, x[i-1], x[i]))


# Plot
plt.plot(x,y)
plt.hlines(0,xmin,xmax)
plt.xlabel(r'$\vec(v)/m\cdot s^(-1)$')
plt.ylabel('y')
plt.title(r'$y=x^2-3x+ e^x-2$')  # Notacion LaTeX
plt.show()

