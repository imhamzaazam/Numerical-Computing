# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 00:15:02 2019

@author: Hamza
"""
import math 
import numpy as np
import sympy
import matplotlib.pyplot as plt

iterations = 0
converge = False
diverge = 0
ans = 0
print(f"{'i':<5} {'x':>4} {'g(x)':>7} ")

def func(x):
    return ((math.exp(-x)))

#ans = func(0) #x=0
ansArr = []
ansArr.append(ans)
while(iterations<15 or  converge):
    #print(iterations)
    if(ans == round(func(ans), 4)):
        converge=True    
    print(
            f"{iterations+1:<5} {ans:>6}  {round(func(ans), 4)}"
    )
    ans=round(func(ans), 4)
    ansArr.append(ans)
    
    iterations += 1
#print(ansArr)
