# -*- coding: utf-8 -*-
"""
Created on Thu Mar 8 21:04:30 2018

@author: Ledicia Diaz
"""
import numpy as np
from sys import exit
import scipy.linalg as scl
import matplotlib.pyplot as plt


# Funciones
def poly_fit(datos, n, a0=True):
    '''
    Ajuste a un polinomio grado n: y=A0 + A1 x + A2 x^2 +...+ An x^n
    Argumentos de entrada:
        datos:
            tupla (x,y) para ajuste sin ponderar
            tupla (x,y,s) para ajuste ponderado
        n: grado del polinomio
        ao=True (con término independiente), a0=False (sin término independiente)
    Argumentos de salida:
        coeficientes polinomio en el orden An,...,A2,A1,A0
        tipo
    '''
    tipo = 'sin ponderar'
    nd = len(datos)
    if nd == 2:
        xe, ye = datos
    elif nd == 3:
        xe, ye, se = datos
        tipo = 'ponderado'
    else:
        exit('Número de datos incorrecto')

    # Numero puntos experimentales
    N = len(xe)
    # si es sin ponderar poner sigmas a 1.
    if nd == 2: se = np.ones(N)
    # construimos matrices auxiliares para el calculo de sumatorios
    a = np.zeros((n + 1, N), dtype=float)
    b = np.zeros((1, N), dtype=float)
    for i in range(n + 1):
        a[i, :] = xe ** i
    a = a / se
    for i in range(N):
        b[0][i] = ye[i]
    b = b / se
    # Matries de sumatorios
    A = np.dot(a, a.T)
    B = np.dot(a, b.T)
    # Anular el término A0 si es necesario
    if a0 == False:
        A[0, :] = 0.
        A[:, 0] = 0.
        A[0, 0] = 1.
        B[0, 0] = 0.
    # Calculo de la solución
    x = np.dot(scl.inv(A), B)
    # Calculo del polinomio con los coeficientes obtenidos
    po = np.reshape(x, (1, n + 1))
    po = po[0][::-1]
    pol = np.poly1d(po)
    # Calculo de valores teoricos variable y
    yc = pol(xe)
    # Calculo de ji cuadrado
    dif = (ye - yc) / se
    ji2 = np.sum(dif ** 2)
    # Calculo de la desviacion estandar
    Syx = (N * ji2 / ((N - n - 1) * np.sum(1. / se ** 2))) ** 0.5
    # Calculo de la media
    ym = (np.sum(ye / se ** 2)) / (np.sum(1. / se ** 2))
    # Calculo de St
    St = np.sum(((ye - ym) / se) ** 2)
    # Calculo de coeficiente de determinacion
    r2 = (St - ji2) / St
    # Calculo de errores de los coeficientes
    E = (np.diag(scl.inv(A))) ** 0.5  # ponderado
    if nd == 2:
        E = Syx * E                   # sin ponderar
    # Impresion de resultados
    print('===== Ajuste %s a un polinomio de grado %d =====' % (tipo, n))
    print('ji2=', ji2)
    print(u'desviación estándar=', Syx)
    print(u'coeficiente de regresión=', r2 ** 0.5)
    for i in range(n + 1):
        if i == 0 and a0 == False:
            print('A[{0:d}]= {1:f}'.format(i, x[i][0]))
        else:
            print('A[{0:d}]= {1:f} , sA[{0:d}]= {2:f}'.format(i, x[i][0], E[i]))
    return po, tipo


## Programa

# Datos ejemplo: polinomio grado 1
xe = np.array([3000 ** (-0.5), (3500) ** (-0.5), 4000 ** (-0.5), (4500) ** (-0.5), 5000 ** (-0.5)], dtype=float)
ye = np.array([52.6, 49.035, 45.73, 43.655, 41.52], dtype=float)
# se=np.array([0.1,0.01,0.01,0.01,0.01],dtype=float)
# 29.365,28.465,27.07,25.315,24.245

# Ajuste sin incertidumbres
coef, tipo = poly_fit((xe, ye), 1)
# Ajuste sin incertidumbres sin término Ao
# coef,tipo=poly_fit((xe,ye),2,a0=False)

# Ajuste con incertidumbres
# coef,tipo=poly_fit((xe,ye,se),1)
# Ajuste con incertidumbres sin término Ao
# coef,tipo=poly_fit((xe,ye,se),1,a0=False)

# Grafica
po = np.poly1d(coef)
x = np.linspace(0, 10, 10)
y = po(x)

plt.plot(x, y, 'r-')
plt.plot(xe, ye, 'or', markersize=5)

# Barra de errores si procede
if tipo == 'ponderado':
    plt.errorbar(xe, ye, yerr=se, linestyle="None")

plt.title(u'gráfica')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.show()
