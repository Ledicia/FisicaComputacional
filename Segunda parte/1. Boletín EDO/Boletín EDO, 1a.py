# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 19:24:48 2018

@author: Ledicia Díaz
"""

import numpy as np
import matplotlib.pyplot as plt

delta_t=0.1
t=0
y=1
x=1
w0=1
N=100
x0=1
y0=2
#a)Método de Euler:

for i in range(N):
    x=x0+delta_t*y0
    y=y0+delta_t*(-w0**2*x0)
    t=delta_t+t
    x0=x
    y0=y
    plt.plot(x,y,"+")
    
   
'''
Efecto de ∆t sobre la solución (analizar la estabilidad del método en función
del paso de integración)
 
Para este método, delta_t=0.1 es demasiado grande, por lo que tendríamos una
espiral en el espacio de fases. Como la ecuación es la de un oscilador
armónico, lo que tendría que aparecer sería una curva cerrada. Sabemos que 
la solución diverge porque el valor de x crece con N.

Si ahora ponemos delta_t=0.01 obtenemos una elipse, por tanto una curva cerrada,
con la anomalía que parece que la línea no cierra completamente el óvalo,
sino que se superpone. Si aumentamos N vemos que la soluación diverge ya que 
las llíneas se van superponiendo aumentando x progresivamente.

Reduciendo delta_t=0.001, y aumentando N, pues sino simplemente aparece un
trozo del diagrama de fases, podemos ver que la estabilidad mejora, pues
ahora obtenemos una elipse cerrada.
'''
