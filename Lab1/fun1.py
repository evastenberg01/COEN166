#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 13:25:31 2022

@author: evastenberg
"""

#Exercise 7

def times(x,y): # create a function
 return x*y # Body executed when called
a = times(2,4)
b = times('Ok', 4) # Functions are “typeless”
print(a,'\n', b)
print(a,b)