# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 12:37:26 2018

@author: Ledicia Diaz
"""

import numpy as np

A = np.array([[1, 2, -1], [2, 4, 5], [3, -1, -2]], float)
B = np.array([[2], [25], [-5]], float)
A = np.array([[1, 2, -3, 4], [3, 1, 0, -2], [0, 3, 1, 3], [-5, -2, 5, 2]], float)
B = np.array([[8], [-15], [22], [38]], float)
f, c = np.shape(A)
print('Matrices iniciales', A, B)
P = np.eye(f, c, dtype=float)  # Matriz con unos en la diagonal y ceros en el resto
print('Matriz P inicial', P)
L = np.full_like(P, 0)
print('Matriz L', L)

U = np.full_like(A, 0)
np.copyto(U, A)  # copia los elementos de la matriz A a la matriz U

# Funcion pivote
def pivote(AB, i):
    print('Matriz inicial \n', AB)
    h = np.argmax(np.abs(AB[i:, i])) + i
    # argmax: devuelve el índice del elemento mayor, por eso al final ponemos un +i que añade los elementosde arriba
    # Posicion del elemento mas grande de la columna i-esima
    # print('h', h)
    if i != h:
        b = np.copy(AB[i, :])             # Copia de la fila i-esima
        AB[i, :], AB[h, :] = AB[h, :], b  # Intercambiamos filas
        print('Matriz final \n', AB)
        print('intercambia filas %.f y %.f' % (i, h))
    return AB, h


# AB[j,:], AB[fila,:] = ABC[fila,:], ABC[j,:]
i = 0
for i in range(f - 1):
    U, m = pivote(U, i)
    print('intercambia filas %.f y %.f' % (i + 1, m + 1))
    print('matriz U', U)

    if m != i:
        aux = np.zeros(f)
        np.copyto(aux, P[m, :])
        np.copyto(P[m, :], P[i, :])
        np.copyto(P[i, :], aux)
        print('Matriz P', P)
        aux2 = np.zeros(f)
        np.copyto(aux2, L[m, :])
        np.copyto(L[m, :], L[i, :])
        np.copyto(L[i, :], aux2)

    for j in range(i + 1, f):
        L[j][i] = U[j, i] / U[i, i]
        U[j, :] = U[j, :] - (U[j, i] / U[i, i]) * U[i, :]

for i in range(f):
    L[i][i] = 1.
    print('por el elemento (%.f,%.f)' % (i + 1, i + 1))
    print('Matriz U', U)
    print('Matriz L', L)
    print('Matriz P', P)

Pb = np.dot(P, B)
print('Matriz  Pb', Pb)

y = np.zeros(f, float)
y = np.reshape(y, (f, 1), float)
y[0, 0] = Pb[0, 0] / L[0, 0]
i = 0
for i in range(i + 1, f):
    suma = 0
    for j in range(i):
        suma = suma + (y[j, 0] * L[i, j])
    y[i, 0] = (Pb[i, 0] - suma) / L[i, i]
print('vector columna y', y)

# Sistema regresivo para obtener la solucion
x = np.zeros(f)  # vector solucion
x[f - 1] = y[f - 1, 0] / U[f - 1, f - 1]
for i in range(f - 2, -1, -1):
    n = 0
    for j in range(f - 1, -1, -1):
        n = n + U[i, j] * x[j]
    x[i] = (y[i, 0] - n) / U[i, i]

print('Las soluciones son: ')
for i in range(len(x)):
    print('x%d=%.2f' % (i + 1, x[i]))

