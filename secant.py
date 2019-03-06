# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 21:29:05 2019

@author: Hamza
"""

import math
current = -1.5
prev = -2
def f(x):
    return math.cos(x) + 2*math.sin(x) + x**2
i=0
iterations = 6
ans = []
xVal = 0
print("n      Xn\t  Xn+1")
while(i<iterations):
    xVal = current - (((current-prev)/(f(current)-f(prev)))*f(current))   
    prev = current
    current = xVal
    xVal = round(xVal, 4)
    #print(xVal)
    ans.append(xVal)
    current = round(current,4)
    prev = round(prev,4)
    print(i,"   ",prev,"\t",current)
    i+=1