# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 11:16:47 2018

@author: Ledicia Diaz
"""
import numpy as np

# Inicializacion de variables
a = 0.0; b = np.pi / 2.0
n = 1

# Funcion
def funcion(x):
    y = (x ** 2 + x + 1) * np.cos(x)
    return y
#
x = np.linspace(a, b, n + 1)
y = funcion(x)
h = (b - a)             # Subintervalo
fa = y[0]; fb = y[-1]   # Limites de integracion
T0 = h * (fa + fb) / 2  # Integral inicial

print("2n: 1")
print('h: ', h)
print('T:', T0, "\n")

T_old = 10000000  # Valor inicial grande para que no cumpla la condicion de precision
p = 1.0e-05       # Precision
j = 1
while abs(T0 - T_old) > p:
    T_old = T0  # Actualizamos el valor de T_old antes de actualizar T0
    j += 1
    n = 2 ** (j - 2)
    # x=np.linspace(a,b,2*(n+1)), esta linea no cambia nada, no es necesaria, porque la divison de los intervalos ya la hace h
    h = (b - a) / (2 ** (j - 1))
    suma = 0
    for k in range(1, n + 1):
        x2 = a + (2 * k - 1) * h
        y = funcion(x2)
        suma = suma + y
    T = T0 / 2. + h * suma  # y[0:-1] es un numero, solo, quiero hacer un suamtorio de todos lso elementos
    T0 = T
    print("2n: ", 2 * n)
    print('h: ', h)
    print('T:', T, "\n")

'''
Otra manera mas eficiente que aun no he probado
for j in xrange(1,n+1):
    x=np.linspace(a,b,n+1)/(2**(j-1))
    h=(b-a)/(2**(j-1))
    for k in range(n):
        x2=a+(2*k-1)*h
        y=funcion(x2)
    T[j]=T[j-1]/2. + h*np.sum(y[0:-1])
    print T    

while abs(integral-integral_old)>p:
    integral_old= integral
    n=n+100
    x=np.linspace(a,b,n+1)

    y=funcion(x)

    h=(b-a)/n

    fa=y[0]
    fb=y[-1]

    integral= h*(fa+fb)/2. + h*np.sum(y[1:-1])

print('I=%.12f'%(integral))
'''
