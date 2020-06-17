# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 12:37:28 2018

@author: Ledicia Díaz, Control 1 (EDO)
"""
import numpy as np
import matplotlib.pyplot as plt

u=1; v=5; alpha=0.5; delta_t=0.01; t=0

for i in range(100):
    t=t+delta_t
    
    k1u=delta_t*(u*(1-v))
    k1v=delta_t*(alpha*v*(u-1))
    
    k2u=delta_t*((u+k1u/2)*(1-(v+k1v/2)))
    k2v=delta_t*(alpha*(v+k1v/2)*((u+k1u/2)-1))
    
    k3u=delta_t*((u+k2u/2)*(1-(v+k2v/2)))
    k3v=delta_t*(alpha*(v+k2v/2)*((u+k2u/2)-1))
    
    k4u=delta_t*((u+k3u)*(1-(v+k3v)))
    k4v=delta_t*(alpha*(v+k3v)*((u+k3u)-1))
    
    u2=u+k1u/6+k2u/3+k3u/3+k4u/6
    u=u2
    v2=v+k1v/6+k2v/3+k3v/3+k4v/6
    v=v2
    plt.plot(u,v,'*')
    plt.xlabel('u')
    plt.ylabel('v')