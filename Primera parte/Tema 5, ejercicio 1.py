# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 12:44:09 2018

@author: Ledicia Diaz
"""

import random as rd
import numpy as np

def f(x):
    y = (1 - x ** 2) ** (1.5)
    return y

suma1 = 0; suma2 = 0
a=0; b=1
N = 100
V = (b-a)  # Intervalo

# Genera una semilla a partir del uno, por lo que genera siempre los mismos números aleatorios
rd.seed(1)
for i in range(N):
    x = rd.uniform(a, b)
    y = f(x)
    suma1 = suma1 + y
    suma2 = suma2 + y**2
    print(x)
  
f2_media = (suma2/N)
f_media = (suma1/N)
f_media2 = (suma1/N)**2
  
I = f_media*V
print('Integral=', I)
error = np.sqrt((f2_media-f_media2)/N)*V
print('Error=', error)


