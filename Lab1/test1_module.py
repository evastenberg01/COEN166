#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 13:31:16 2022

@author: evastenberg
"""

import module # Get module as a whole
result = module.adder(module.a, module.b) # Go through the module name “module” to fetch
# its attributes “adder”, “a”, and “b”
print(result)