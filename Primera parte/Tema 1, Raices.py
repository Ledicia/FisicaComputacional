# -*- coding: utf-8 -*-
"""
Created on Thu Feb 01 13:44:17 2018

@author: Ledicia Diaz
"""
import numpy as np

def fun(x):
        f = x**2-3*x+np.exp(x)-2
        return f

def fun2(x):
    f = (37.72 * x ** 2 - 15.8 * x + 1.738) / (x ** 3 - 0.11 * x ** 2) - 16
    return f

def biseccion(a, b):
    while np.abs(b-a)>1e-6:
        c=(a+b)/2.
        if np.sign(fun(a))!=np.sign(fun(c)):
            b=c
        else:
            a=c
    return c

N=20
x=np.linspace(-2, 4, N+1)

y=fun(x)

print(x)
print(y)

for i in range(x.size-1):
    if np.sign(y[i])!=np.sign(y[i+1]):
        print(x[i], x[i+1])
        sol=biseccion(x[i], x[i+1])
        print(sol)
        
        

    

        
        
        
        
        