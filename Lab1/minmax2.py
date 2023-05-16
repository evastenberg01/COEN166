#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 14:51:04 2022

@author: evastenberg
"""

def minmax(fun,array):
    result = array[0]
    for arg in array[1:]:
        if fun(arg, result):
            result = arg
            return result
def lessthan(x,y): return x<y
def grtrthan(x,y): return x>y
if __name__ == '__main__':
    print(minmax(lessthan, [4,2,1,5,6,3])) # self-test code
    print(minmax(grtrthan, [4,2,1,5,6,3]))