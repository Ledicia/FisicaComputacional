# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 12:44:37 2018

@author: Ledicia Diaz
"""
import numpy as np

# Funcion a integrar
def f(x):
    y = x**3 - 3*x**2 - x + 3
    return y

# Variables de integracion:
a = 0.; b = 1.35
fa=f(a); fb=f(b)  # Definimos los límites
n = 10            # Número de subintervalos
h = (b-a)/n       # Ancho de cada subintervalo

x = np.linspace(a,b,n+1)
y = f(x)

# Suma todos los elementos menos los extremos
integral = h*(fa + fb)/2. + h * np.sum(y[1:-1])

# # Otra manera de hacerlo menos eficiente:
# integral = h*(fa + fb)/2.
# for i in range(1,n):
#     integral = integral+h*f(x[i])

print('I=%.12f'%(integral))

p = 1e-10                # Precisión
integral_anterior = 10   # Se le asigna un valor para que empiece el bucle

# Calcula la nueva integral y después la compara abs(integral-integral_anterior)>p continuando el bucle si esto se cumple
while abs(integral-integral_anterior)>p:
    integral_anterior = integral
    # Se define un nuevo n ya que con el número de subintervalos dado inicialmente no se cumple la precisión requerida
    n = n+1
    x = np.linspace(a,b,n+1)
    y = f(x)
    h = (b-a)/n  # Nuevo ancho de los subintervalos
    fa = f(a)
    fb = f(b)
    integral = h*(fa+fb)/2.+ h*np.sum(y[1:-1])
    
print('Icorregida=%.12f'%(integral))
print(n)
