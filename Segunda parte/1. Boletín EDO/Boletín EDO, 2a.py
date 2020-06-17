# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 12:42:33 2018

@author: Ledicia Díaz
"""
import numpy as np
import matplotlib.pyplot as plt

delta_t=0.1
t=0.
x=1.
y=1.
w0=2.
b=1.
w=2.
F=1.
x0=1.
y0=0.
for i in range(1000):
    x=x0+delta_t*y0
    y=y0+delta_t*(-b*y0-w0**2*x0+F*np.cos(w*t))
    t=delta_t+t
    x0=x
    y0=y
    
    plt.plot(x,y,"+")
    
    
'''
Comprobar el efecto de ∆t sobre la solución obtenida (analizar la estabilidad
del método en función del paso de integración). Analizar el caso resonante.

Para un delta_t=0.1 y F=b=0 obtenemos una espiral divergente en el espacio de
fases, tal cual la del ejercicio 1a, por lo que al ir reduciendo delta_t 
obtenemos el mismo diagrama de fases. 
La solución va a mejorar a medida que aumentamos el tiempo de integración, y 
reducimos delta_t.
Para el caso resonante con w=w0=2 y delta_t=0.1 la solución se corta
en el espacio de fases,lo cual es imposible; en cambio, para delta_t=0.01 
obtenemos un ciclo límite. 
Si w=2 y w0=F=b=1, obtenemos una solución en el espacio de fases que se corta. 
Esto es imposible.
'''