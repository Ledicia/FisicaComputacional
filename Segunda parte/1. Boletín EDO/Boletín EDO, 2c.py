# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 13:20:32 2018

@author: Ledicia Díaz
"""
import numpy as np
import matplotlib.pyplot as plt

delta_t=0.01
x=1
y=1
b=1
w0=1
w=1
F=1
t=1

for i in range (1000):
    k1x=delta_t*y #primera pendiente 
    k1y=delta_t*(-w0**2*x-b*y+F*np.cos(w*t))
    k2x=delta_t*(y+k1y/2) #método runge-kutta orden 2
    k2y=delta_t*(-w0**2*(x+k1x/2)-b*(y+k1y/2)+F*np.cos(w*(t+delta_t/2)))
    k3x=delta_t*(y+k2y/2)
    k3y=delta_t*(-w0**2*(x+k2x/2)-b*(y+k2y/2)+F*np.cos(w*(t+delta_t/2)))
    k4x=delta_t*(y+k3y)
    k4y=delta_t*(-w0**2*(x+k3x)-b*(y+k3y)+F*np.cos(w*(t+delta_t)))
    t=t+delta_t
    y=y+k1y/6+k2y/3+k3y/3+k4y/6
    x=x+k1x/6+k2x/3+k3x/3+k4x/6
    plt.plot(x,y,'*')
    plt.xlabel('x')
    plt.ylabel('y')
    
'''
Comprobar el efecto de ∆t sobre la solución obtenida (analizar la estabilidad
del método en función del paso de integración). Analizar el caso resonante.

Para un delta_t=0.1 y F=b=0 obtenemos el mismo diagrama de fases que el 
obtenido en el ejercicio 1c.
Si ponemos w=w0=2 obtenemos un ciclo límite nuevamente, tal y como pasaba con
el método Runge-kutta de 2º orden.
Si ahora establecemos w=2 y w0=F=b=1, la solución en el espacio de fases  no
se corta.
===========================================================================
Para todos los métodos:
En el caso resonante de w=w0 tenemos que la solución converge a una elipse
cuya forma dependerá de los valores de F y b. Si domina la fuerza F, la elipse
crece; por el contrario, si domina el coeficiente de amortiguamiento b, la
elipse decrece.
La solución x(t) oscilará con una fase transitoria adicional creciendo o 
decreciendo hasta que se estabilice.
Para el caso b=0 la energía del sistema crece indefinidamente, debido a que 
no existe fuerza de rozamiento. En cambio, si F=0, tendremos una espiral que 
decae hasta el cero.
La estabilidad de las soluciones depende mucho de los valores de b, F, w y w0.
El método Runge-kutta de 4º orden es estable para valores mayores de w0.
'''
