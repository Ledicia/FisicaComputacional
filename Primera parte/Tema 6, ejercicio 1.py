# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 12:50:37 2018

@author: Ledicia Díaz
"""

import numpy as np

A=np.array([[3,-1,0],[-1,2,-1],[0,-1,3]])
D = np.full_like(A,0,float)
np.copyto(D,A)
V = np.identity(len(A), float)  # Matriz identidad
F,C=np.shape(A)

precision = 0.0000001
a=1; b=1    # Inicializacion de las variables para que empiece el bucle

# Calculo de autovalores (Diagonal de D) y autovectores (V)
while np.all(a<precision)==False and np.all(b<precision)==False:
    # Evalua si todos los elementos de la matriz a lo largo de un eje determinado son verdaderos
    # Se inicia el bucle si no es cierto que ni a ni b son menores que p
    elemento = 0
    for i in range (F):
        for j in range (C-1):
            if D[i,j] != D[i,i]:  # Elementos fuera de la diagonal
                if abs(D[i,j])>abs(elemento):
                    elemento = D[i,j]
                    p = i; q = j
    
    # Calculo variables
    theta = (D[q, q]-D[p, p])/(2*D[p, q])
    t = np.sign(theta)/(abs(theta) + np.sqrt(theta**2 + 1))
    c = 1/np.sqrt(t**2 + 1)
    s = c*t
    
    # Matriz R
    R = np.identity(len(A))
    R[p, p] = c; R[p, q] = s; R[q, p] = -s; R[q, q] = c
    Rt = np.transpose(R)
    D1 = np.dot(np.dot(Rt, D), R)  # np.dot multiplica matrices o hace el producto interno de vectores
    V1 = np.dot(V, R)
    a = abs(D1-D); b = abs(V1-V)   # Redefinir a y b para que el bucle pare cuando sean menores que la precisión

    # Copia valores de una matriz a otra
    np.copyto(D, D1); np.copyto(V, V1)


print('Precision: ', precision)
print('Autovalores: ', np.diag(D1))
print('Autovectores: ', V1)