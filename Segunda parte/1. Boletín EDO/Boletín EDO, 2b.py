# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 13:05:25 2018

@author: Ledicia Díaz
"""
import numpy as np
import matplotlib.pyplot as plt

delta_t=0.1
x=1
y=1
b=1
w0=2
w=2
F=1
t=1

for i in range (1000):
    k1x=delta_t*y #primera pendiente 
    k1y=delta_t*(-w0**2*x-b*y+F*np.cos(w*t))
    k2x=delta_t*(y+k1y/2) #método runge-kutta orden 2
    k2y=delta_t*(-w0**2*(x+k1x/2)-b*(y+k1y/2)+F*np.cos(w*(t+delta_t/2)))
    t=t+delta_t
    y=y+k2y
    x=x+k2x
    plt.plot(x,y,'*')
    plt.xlabel('x')
    plt.ylabel('y')
    
'''
Comprobar el efecto de ∆t sobre la solución obtenida (analizar la estabilidad
del método en función del paso de integración). Analizar el caso resonante.

Para un delta_t=0.1 y F=b=0 obtenemos el mismo diagrama de fases que en el
ejercicio 1b. Esto nos sirve a modo de comprobación.
Si ponemos w=w0 vemos que la solución se corta en un punto para delta_t=0.1
y N=1000 (tiempo de integración).
Para delta_t=0.1, y N=1000, cuando w=w0=2 la solución en el espacio de fases
ahora es un ciclo límite, es decir, ya no se corta el diagrama de fases,
por lo que este método es más estable que el de Euler.
Si ahora establecemos w=2 y w0=F=b=1, la solución en el espacio de fases ya no
se corta, cosa que si que ocurría utilizando el método de euler.

'''