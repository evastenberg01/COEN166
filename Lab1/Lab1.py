#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 12:28:02 2022

@author: evastenberg
"""

#Exercise 1
a=123+222
print(a)

b=1.5*4
print(b)

c=2**10 # 2 to the power of 10
print(c)

import math
print(math.pi)

print(math.sqrt(36))

import random
a=random.random()
print('a=',a)

b=random.choice([1,2,3,4])
print('b=',b)

#Exercise 2
S='Spam'
len(S)
S[0] 
S[1]
S[-1]
S[-2]
S[len(S)-1]
S[1:3]
S='z'+S[1:]
S