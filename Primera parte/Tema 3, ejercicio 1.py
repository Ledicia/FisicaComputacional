# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 12:34:26 2018

@author: Ledicia Diaz
"""
import numpy as np
import scipy.misc as scm
import scipy.special as scs

# Derivar en el punto x0
x0 = 1.2; d = 1; h = 1
b=np.array([-2,-1,0,1,2], float)

# Función para derivar
def f(x):
    f = x**3 - 3*x**2 - x + 3
    return f
"""
N=18
print'======================================================'
for i in range (N):
    ec10=(f(x0+h)-f(x0-h))/(2*h)
    ec16=(-f(x0+2*h)+8*f(x0+h)-8*f(x0-h)+f(x0-2*h))/(12*h)
    print '%20.17f %20.17f %20.17f' %(h,ec10,ec16)
    h/=10.
print '====================================================='
"""

n=len(b)
A=np.zeros((n, n))  # Matriz de ceros cuadrada

for i in range(n):
    A[i] = b**i
print(A)

B = np.zeros((n, 1))  # Matriz de ceros columna
B[d] = scm.factorial(d)
print(B)
AB=np.concatenate((A,B),axis=1)
print(AB)
F,C=np.shape(AB)
print(F,C)

for i in range(F-1):
    for j in range (i+1,F):
        g = AB[j,i]/AB[i,i]
        AB[j,:] = AB[j,:] - g*AB[i,:]
print(AB)

x=np.zeros(F, float)
for i in range (F-1,-1,-1):
    x[i] = (AB[i, F] - np.sum(AB[i, 0:F]*x))/AB[i, i]
print(x)

for i in range(len(x)):
    print('x%.0f= %f' %(i+1, x[i]))

# Derivadas:
der = np.sum((x * f(x0 + b*h))) / h**d
print('Derivada:', der)


