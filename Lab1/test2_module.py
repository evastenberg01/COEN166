#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 13:32:29 2022

@author: evastenberg
"""

c = 5
d = 10
from module import adder # Copy out an attribute
result = adder(c, d) # No need go through the module name “module” to fetch
# its attribute “adder”
print(result)
from module import a, b, multiplier # Copy out multiple attributes
result = multiplier(a, b)
print(result)