# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 11:55:45 2018

@author: Ledicia Díaz
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
    k3x=delta_t*(y+k2y/2)
    k3y=delta_t*(-w0**2*(x+k2x/2))
    k4x=delta_t*(y+k3y)
    k4y=delta_t*(-w0**2*(x+k3x))
    t=t+delta_t
    y=y+k1y/6+k2y/3+k3y/3+k4y/6
    x=x+k1x/6+k2x/3+k3x/3+k4x/6
    plt.plot(x,y,'*')
    plt.xlabel('x')
    plt.ylabel('y')
    
'''
Efecto de ∆t sobre la solución (analizar la estabilidad del método en función
del paso de integración)
 
Para este método una delta_t=0.1 obtenemos ya una curva cerrada de forma 
ovalada. Si aumentamos N=10000 la solución sigue convergiendo.

Analizados los tres métodos vemos que el más preciso es el Runge-kutta de 
4º orden, ya que no necesita un delta_t tan pequeño para que la solución
converja. Esto nos permite reducir también el tiempo de interación N, siendo 
un programa más rápido y con mejores resultados.
'''