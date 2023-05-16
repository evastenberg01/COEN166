#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 13:10:31 2022

@author: evastenberg
"""
##xercise 6
x='spam'
while x:
        print(x,end='')
        x=x[1:]

a=0; b=10
while a<b:
    print(a,end='')
    a+=1
    
x=10
while x:
    x=x-1
    if x%2 !=0: continue
    print(x,end='')
    
thislist = ["spam", "eggs", "ham"]
for x in thislist:
    print(x,end='')
    
sum = 0
for x in [1,2,3,4]:
    sum = sum+x
print(sum)

prod = 1
for item in [1,2,3,4]: prod*=item
print(prod)
