# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 20:23:46 2023

@author: gio
"""

import numpy as np
import matplotlib.pyplot as plt

####################

def parallelo(x,y):
    return x * y/(x + y)


def calcola(R1,R2,Vdd):
    
    Vg = Vdd * parallelo(R1,R2) / R1
    Rs = (Vg - 5) * 666.66667
    #Ai = (parallelo(R1,R2) / (333.33334 + parallelo(Rs,1000))) * (Rs / (Rs + 1000))
    #Av = (parallelo(Rs,1000) / (333.33334 + parallelo(Rs,1000))) * (parallelo(R1,R2) / (2500 + parallelo(R1,R2)))
    
    #dimostrazione equivalenza della seconda formula di Ai: 
    Ai =  ( ((Rs*3/2000)+5)*R1 / (Vdd*(333.33334 + parallelo(Rs,1000) ))) * (Rs / (Rs + 1000))
    
    #dimostrazione equivalenza della seconda formula di Av: 
    Av = (parallelo(Rs,1000) / (333.33334 + parallelo(Rs,1000))) * (((Rs*3/2000)+5)*R1) / ( (((Rs*3/2000)+5)*R1) + 2500*Vdd)
    
    
    '''
    print("R1: " + str(R1))
    print("R2: " + str(R2))
    print("Vdd: " + str(Vdd))
    
    print("----")
    
    print("Vg: " + str(Vg))
    print("Rs: " + str(Rs))
    print("Ai: " + str(Ai))
    print("Av: " + str(Av))
    '''
    
    return(Vg,Rs,Ai,Av)
    

####################

dataAv = []
dataAi = []
dataRs = []
dataVg = []
dataR = []

for x in range(15, 20):
    a,b,c,d = calcola(300000,300000,x)
    
    dataR = np.append(dataR,x)
    dataAv = np.append(dataAv,d)
    dataAi = np.append(dataAi,c)
    dataRs = np.append(dataRs,b)
    dataVg = np.append(dataVg,a)


textLegend = 'R1=R2=300k'
xText = 'R'
markerUserd = '*'


plt.subplot(2,2,1)
plt.plot(dataR,dataAv, marker=markerUserd, color = 'r', label = textLegend)
plt.xlabel(xText)
plt.ylabel('Av')
plt.grid(True, color='gray', linestyle='--')
#plt.text(0.05, 0.95, 'Vdd=15', transform=plt.gca().transAxes, va='top', ha='left')
plt.legend(loc='upper left')



plt.subplot(2,2,2)
plt.plot(dataR,dataAi, marker=markerUserd, color = 'orange', label = textLegend)
plt.xlabel(xText)
plt.ylabel('Ai')
plt.grid(True, color='gray', linestyle='--')
#plt.text(0.05, 0.95, 'Vdd=15', transform=plt.gca().transAxes, va='top', ha='left')
plt.legend(loc='upper left')



plt.subplot(2,2,3)
plt.plot(dataR,dataRs, marker=markerUserd, color='g', label = textLegend)
plt.xlabel(xText)
plt.ylabel('Rs')
plt.grid(True, color='gray', linestyle='--')
#plt.text(0.05, 0.95, 'Vdd=15', transform=plt.gca().transAxes, va='top', ha='left')
plt.legend(loc='upper left')



plt.subplot(2,2,4)
plt.plot(dataR,dataVg, marker=markerUserd, color = 'b', label = textLegend)
plt.xlabel(xText)
plt.ylabel('Vg')
plt.grid(True, color='gray', linestyle='--')
#plt.text(0.05, 0.95, 'Vdd=15', transform=plt.gca().transAxes, va='top', ha='left')
plt.legend(loc='upper left')



plt.show()

####################

#calcola(200000,800000,15)
