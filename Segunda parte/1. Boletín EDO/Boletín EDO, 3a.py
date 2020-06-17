# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 13:38:06 2018

@author: Ledicia Díaz 
"""
import numpy as np
import matplotlib.pyplot as plt

delta_t=0.1
r=1
P=10
k=100
t=1

for i in range (1000):
    P2=P+delta_t*(r*P*(1-P/k))
    t=t+delta_t
    P=P2
    
    plt.plot(t,P,'*')
    plt.xlabel('t')
    plt.ylabel('x')
