"""
Hamza Azam
"""
import math
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal as D

a = 3.0
b = 4.0
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
print(f"{'i':<8} {'a':>2} {'b':>7} {'f(a)':>12} {'f(b)':>10} {'c':>8} {'f(c)':>13} {'Error':>10}")
def func(x):
    return ((math.exp(-x))*(((3.2*(math.sin(x))) - (0.5 * (math.cos(x))))))

#print(round(func(3), 4))
while(i<maxIteration and not(round(func(midPt), 4) == ans)):
    #if((func(a)>0 and func(b)<0) or (func(b)>0 and func(a)<0)):
     #   print("Root does not exists!")
        #break
    #else:
    fA = (round(func(a), 5))
    fB = (round(func(b), 5))
    midPt = (a+b)/2
    #print(midPt)
    arrMid.append(midPt)
    fC = (round(func(midPt), 4))
    arrFC.append(fC)
    print(
        f"{i+1:<2} {a:>10} {b:>10} {fA:>10} {fB:>10} {midPt:>10} {fC:>10} "
    )
    if(fC * fB<0):
        a=midPt
    elif(fA*fC<0):
        b=midPt
    #print(fC)
    
    i+=1 
#print(arrFC)
#print(arrMid)
        
