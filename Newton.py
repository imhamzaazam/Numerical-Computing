# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 01:21:12 2019

@author: Hamza
"""

# -*- coding: utf-8 -*-


import sympy as sp
x = sp.Symbol('x')
#print(sp.diff(x**3 - x - 1, x))

from scipy.misc import derivative
def f(x):
    return x**3 - x - 1
def df(x):
    return sp.diff(f(x), x)
rootA = 0.0
rootB = 0.0
i=0
maxIteration = 10
for i in range(-4, 5):
    #print("i: ",i, f(i))
    if(rootA!=0 and rootB!=0):
        break
    if(f(i))<0:
        rootA = i 
    if(f(i))>0:
        rootB = i
    
i=0
print("Root lies b/w: ",rootA, "&", rootB)
#print("RootB: ",rootB)
ans = []
xVal = (rootA + rootB) /2
ans.append(xVal)
print("i      Xi\t Xi+1=Xi-f(Xi)/f'(Xi)")
while(i<10):
    xVal = round(xVal - (f(xVal)/df(x).subs(x,xVal)), 4)
    #print("I: ", i,"xval", xVal)
    
    print(i,"    ",ans[i],"\t",xVal)
    ans.append(xVal)
    
    i+=1 
#print(ans)


