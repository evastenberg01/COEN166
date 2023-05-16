#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 14:50:10 2022

@author: evastenberg
"""

import unittest

class Testlab2(unittest.TestCase):
    def agent_function(self,location, status):
        self.assertEqual(["Clean","Dirty",0],[])
        self.assertEqual(["Clean","Clean",1],[])
        self.assertEqual(["Dirty","Dirty",1],[])
        
    def space_is_clean(self):
        self.assertTrue(["Clean","Clean"])
    
        
        
    