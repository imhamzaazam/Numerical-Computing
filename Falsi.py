# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 00:26:58 2019

@author: Hamza
"""

import math
import numpy as np
import matplotlib.pyplot as plt

a = 3.000
b = 4.000
midPt=0 #C
ans = 0.001 
maxIteration = 10
i=0
decimalPlaces = 4
fA= 0
fB= 0
fC= 0
arrFC = []
arrMid = []
error = []
iter = []
def func(x):
    return ((math.exp(-x))*(((3.2*(math.sin(x))) - (0.5 * (math.cos(x))))))
print(f"{'i':<8} {'a':>2} {'b':>7} {'f(a)':>12} {'f(b)':>10} {'c':>8} {'f(c)':>13} {'Error':>10}")
#print(round(func(3), 4))
while(i<maxIteration and not(round(func(midPt), 4) == ans)):
    #if((func(a)>0 and func(b)<0) or (func(b)>0 and func(a)<0)):
     #   print("Root does not exists!")
        #break
    #else:
    iter.append(i)
    fA = (round(func(a), 5))
    fB = (round(func(b), 5))
    #midPt = (a+b)/2
    midPt = (a*func(b) - b*func(a)) / (func(b) - func(a))  
    #print(midPt)
    arrMid.append(midPt)
    midPt = round(midPt, 4)
    fC = (round(func(midPt), 4))
    arrFC.append(fC)
    if(i==0):
        error.append(fC)
    else:
        error.append(arrFC[i]-arrFC[i-1])
    
    b = round(b,4)
    print(
        f"{i+1:<2} {a:>10} {b:>10} {fA:>10} {fB:>10} {midPt:>10} {fC:>10} {round(error[i], 4):>10}"
    )
    if(fC * fB<0):
        a=midPt
    elif(fA*fC<0):
        b=midPt
    
    
  
    i+=1 
    

#print(arrMid)
#print(error)
#print(arrFC)

