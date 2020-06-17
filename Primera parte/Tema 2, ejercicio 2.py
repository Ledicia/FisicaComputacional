# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 12:56:02 2018

@author: Ledicia Diaz
"""
import numpy as np

A=np.array([[2,-1,1],[-1,1,2],[1,2,-1]],dtype=float)
B=np.array([[3],[7],[2]],float)

A=np.array([[1,2,-3,4],[3,1,0,-2],[0,3,1,3],[-5,-2,5,2]],float)
B=np.array([[8],[-15],[22],[38]],float)

A=np.array([[1,2,-1],[2,4,5],[3,-1,-2]],float)
B=np.array([[2],[25],[-5]],float)

AB=np.concatenate((A,B), axis=1) #Pega las matrices, axis=1 es columna 0 es por fila

print('A', A, 'B', B, 'AB', AB)
F, C = np.shape(AB)
print(F, C)

def pivote(AB, i):
        print('Matriz inicial \n', AB)
        h=np.argmax(np.abs(AB[i:,i])) + i
        # argmax: devuelve el índice del elemento mayor, por eso al final ponemos un +i que añade los elementosde arriba
        # Posicion del elemento mas grande de la columna i-esima
        print('h', h)
        if i != h:
            b = np.copy(AB[i, :])          # Copia de la fila i-esima
            AB[i, :], AB[h, :] = AB[h, :], b #Intercambiamos filas
            print('Matriz final \n', AB)
            print('intercambia filas %.f y %.f' % (i,h))
        return AB


for i in range (F-1):
    AB=pivote(AB, i)
    for j in range (i+1,F):
        f=AB[j,i]/AB[i,i]
        AB[j]=AB[j]-f*AB[i]
print(AB)
 

x = np.zeros(F, float)  # Creacion de un vector de zeros para guardar las soluciones
for i in range (F-1,-1,-1):  # Bucle que va al reves, sacamos las soluciones
    x[i] = (AB[i, F] - np.sum(AB[i, 0:F] * x)) / AB[i, i]
print(x)

for i in range (len(x)):         
    print('x%.0f= %f' %(i+1, x[i]))
