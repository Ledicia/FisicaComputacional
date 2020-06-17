# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 13:38:08 2018

@author: Ledicia Diaz
"""
import numpy as np
import random as rd

# Centro de masas de un objeto:
# Hipotesis: Cuerpo homogeneo -> la densidad no importa
rd.seed(1)
R = 2.
a = 6.  # eje y
b = 8.  # eje x

# Funciones de calculo del centro de masas
def dm(x, y):
    if ((x - b + R) ** 2 + y ** 2) > R ** 2:
        z = 1.
    elif ((x - b + R) ** 2 + y ** 2) <= R ** 2:
        z = 0.
    return z

# Calculo de la componente x
def xdm(x, y):
    if ((x - b + R) ** 2 + y ** 2) > R ** 2:
        z = x
    elif ((x - b + R) ** 2 + y ** 2) <= R ** 2:
        z = 0.
    return z

# Calculo de la componente y
def ydm(x, y):
    if ((x - b + R) ** 2 + y ** 2) > R ** 2:
        z = y
    elif ((x - b + R) ** 2 + y ** 2) <= R ** 2:
        z = 0.
    return z

# Inicializacion de las variables necesarias para el calculo
N = 10
for j in range(7):
    N = N * 10
    suma = 0.; suma2 = 0.
    sumax = 0.; sumax2 = 0.
    sumay = 0.; sumay2 = 0.
    error = 0.
    for i in range(N):
        xi = rd.uniform(0., b)  # para definir el semicirculo
        yi = rd.uniform(0., a)
        dm1 = dm(xi, yi);             suma = suma + dm1
        dmcuad = (dm(xi, yi)) ** 2;   suma2 = suma2 + dmcuad
        xdm1 = xdm(xi, yi);           sumax = sumax + xdm1
        xdmcuad = (xdm(xi, yi)) ** 2; sumax2 = sumax2 + xdmcuad
        ydm1 = ydm(xi, yi);           sumay = sumay + ydm1
        ydmcuad = (ydm(xi, yi)) ** 2; sumay2 = sumay2 + ydmcuad

    # Calculos para la integral de dm
    fcuad = (suma2 / N)
    f = (suma / N)
    f2 = (suma / N) ** 2
    error = (a * b) * (np.sqrt((fcuad - f2) / N))
    Idm = (a * b) * f
    # Calculos para la integral de xdm
    fxcuad = (sumax2 / N)
    fx = (sumax / N)
    fx2 = (sumax / N) ** 2
    errorx = (a * b) * (np.sqrt((fxcuad - fx2) / N))
    Ixdm = (a * b) * fx
    # Calculos para la integral de ydm
    fycuad = (sumay2 / N)
    fy = (sumay / N)
    fy2 = (sumay / N) ** 2
    errory = (a * b) * (np.sqrt((fycuad - fy2) / N))
    Iydm = (a * b) * fy
    # Calculo de xG e yG: errores calculados mediante propagacion
    xG = Ixdm / Idm
    errorxG = np.sqrt((errorx / Idm) ** 2 + ((Ixdm * error) / (Idm ** 2)) ** 2)
    yG = Iydm / Idm
    erroryG = np.sqrt((errory / Idm) ** 2 + ((Iydm * error) / (Idm ** 2)) ** 2)
    print('N: %10d, xG: %.10f, error: %8.2e,yG: %.10f, error: %8.2e' % (N, xG, errorxG, yG, erroryG))
