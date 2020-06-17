# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 13:21:32 2018

@author: Ledicia Diaz
"""
import numpy as np

# Funcion a integrar
def funcion(x):
    y = (x ** 2 + x + 1) * np.cos(x)
    return y

# Inicializacion variables
a = 0.0; b = np.pi / 2.0  # Valores
n = 5                     # Intervalo
x = np.linspace(a, b, n + 1)  # Vector entre los valores a y b cuyo intervalo con n+1 valores entre a y b
y = funcion(x)
R = []                    # Lista para guardar los valores anterior y recien integrado
h = (b - a)               # Sub-intervalo
fa = y[0]                 # Limite de la integral
fb = y[-1]                # Limite de la integral
T0 = h * (fa + fb) * 0.5  # Integral inicial
R.append([T0])
T1 = []
T1.append(T0)

# Variables del bucle que se encargan de integrar
p = 1.000000e-8       # Precision
R1 = 1000; R2 = 2000  # Inicializar las variables a numeros altos para que inicialmente no cumplan la precision
j = 1
while abs(R1 - R2) > p:
    j += 1             # Aumento del valor de j para recalcular n
    n = 2 ** (j - 2)   # Intervalo
    #x = np.linspace(a, b, 2 * (n + 1))  # esta linea no cambia nada, no es necesaria, porque la divison de los intervalos ya la hace h
    h = (b - a) / (2 ** (j - 1))  # Longitud de los sub-intervalos en funcion de j
    # Suma a lo largo de los intervalos
    suma = 0
    for k in range(1, n + 1):
        x2 = a + (2 * k - 1) * h  # Nuevo x para cada subintervalo (x2 esta entre a y b)
        y = funcion(x2)           # Valor de la funcion para el x de ese intervalo
        suma = suma + y           # Suma sobre todos los intervalos
    T = T0 / 2. + h * suma
    T0 = T
    T1.append(T)
    j -= 1         # Disminuimos el valor de j
    R.append([T])  # Añadimos el nuevo calculo a la lista
    for k in range(1, j + 1):
        R[j].append(R[j][k - 1] + (R[j][k - 1] - R[j - 1][k - 1]) / (4 ** k - 1))
    # Se actualizan los valores de R1 y R2 y se vuelve a empezar en el bucle while mientras que se cumpla la condicion
    R1 = R[j - 1][j - 1];  R2 = R[j][j]
    j += 1
print('el procedimiento para obtener la matriz es: ', R)
print('la integral es: ', R[j - 1][j - 1])

'''
# Otra manera mas eficiente que aun no he probado
for j in range(len(R)):
    for k in range(1,j+1):#esto es para crear una matriz triangular
        R[j][k] = R[j][k-1] + (R[j][k-1] - R[j-1][k-1]) / (4**k- 1)
n+=1  

print ('R:',R)
print ('valor de la integral: ', R[-1])

def romberg(f, a, b, eps = 1E-8):
    """Approximate the definite integral of f from a to b by Romberg's method.
    eps is the desired accuracy."""
    R = [[0.5 * (b - a) * (f(a) + f(b))]]  # R[0][0]
    print_row(R[0])
    n = 1
    while True:
        h = float(b-a)/2**n
        R.append((n+1)*[None])  # Add an empty row.
        R[n][0] = 0.5*R[n-1][0] + h*sum(f(a+(2*k-1)*h) for k in range(1, 2**(n-1)+1)) # for proper limits
        for m in range(1, n+1):
            R[n][m] = R[n][m-1] + (R[n][m-1] - R[n-1][m-1]) / (4**m - 1)
        print_row(R[n])
        if abs(R[n][n-1] - R[n][n]) < eps:
            return R[n][n]
        n += 1        
'''

