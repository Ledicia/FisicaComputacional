# -*- coding: utf-8 -*-
"""
Created on Tue Mar 06 13:05:39 2018

@author: Ledicia Diaz
"""

import numpy as np
a = 0.; b = np.pi/2.
n = 1                 # Número de subintervalos
h = (b-a)             # Ancho de cada subintervalo

# Funcion a integrar
def f(x):
    y=(x**2+3*x+1-x)*np.cos(x)
    return y

x=np.linspace(a,b,n+1)
y=f(x)

# Definimos los límites
fa=f(a); fb=f(b)

T_1 = h * (fa + fb)/2
print('T:', T_1, "\n")

p = 1e-8            # Precisión
T_anterior = 10000  # Se le asigna un valor para que empiece el bucle
j=1

# Calcula la nueva integral y después la compara abs(T(1)-T(anterior)>p continuando el bucle si esto se cumple.
while abs(T_1-T_anterior)>p:
    T_anterior=T_1
    j+=1  # vamos sumando una unidad a la j anterior (como un bucle)
    n = 2**(j-2)
    h = (b-a)/(2**(j-1))
    suma = 0  # Inicializacion de la variable para que empiece el bucle
    
    for i in range(1,n+1):
         x_2 = a+(2*i-1)*h
         y = f(x_2)
         suma = suma+y  # Sumatorio de f(x_2)
         
    T = T_1/2.+ h*suma  # Suma todos los elementos (y[0:-1])
    T_1 = T
         
    print("2n:",  2*n)
    print('h:',h)
    print('T:', T, "\n")
