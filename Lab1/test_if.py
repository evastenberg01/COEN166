#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 13:05:57 2022

@author: evastenberg
"""
#Exercise 5: if Tests and Syntax rules
x =1
if x:
    y= 2
if y>0:
     print('block2')
     print('block1')
     print('block0')
choice = 'ham'
if choice == 'spam': # the equivalent if statement
     print(1.25)
elif choice == 'ham':
    print(1.99)
elif choice == 'eggs':
    print(0.99)
elif choice == 'bacon':
    print(1.10)
else:
    print('Bad choice')