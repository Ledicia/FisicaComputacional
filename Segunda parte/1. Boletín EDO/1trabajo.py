#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 12:43:12 2018

@author: a.hermida
"""

import matplotlib.pyplot as plt
import numpy as np


'''
#============Euler=====================

t=0
x=1
Dt=0.1
N=100
for i in range(N):
    x2=x+Dt*np.sin(x)
    t=t+Dt
    x=x2
    plt.plot(t,x,"-")
'''


#=========== Runge-Kutta   2º orden===============

t=0
x=1
Dt=0.1
N=10000

for i in range(N):
    t=t+Dt
    k1=Dt*np.sin(x)
    k2=Dt*np.sin(x+k1/2)
    k3=Dt*np.sin(x+k2/2)
    k4=Dt*np.sin(x+k3)
    x2=x+k1/6.+k2/3.+k3/3.+k4/6    
    x=x2
    plt.plot(t,x,"+")  
    

    