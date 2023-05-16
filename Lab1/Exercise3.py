#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 12:51:01 2022

@author: evastenberg
"""

L=[123, 'spam', 1.23] 
len(L)

L[0]

L[:-1]

L+[4,5,6]

L.insert(0,'apple')

L=[123,'spam',1.23]
L.insert(2,'apple')

L=[1.10,2,5,8]
L.sort()
L

L.reverse()
L

list(range(4))

list(range(-6,7,2))

[[x **2,x **3]for x in range(4)]
[[x,x/2,x*2] for x in range(-6,7,2) if x > 0]