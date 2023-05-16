#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 14:57:06 2022

@author: evastenberg
"""

class PersonClass: # define a class object
 def basicinfo(self, name, age): # Define class's methods
     self.name=name # self is the instance
     self.age=age
 def display(self):
     print(self.name, '\n', self.age, '\n')
person=PersonClass() # make one instance of the class
person.basicinfo("John", 20) # Call methods: self is person
person.display()
person.name="Mary"
person.age=30
person.display()
person.school="Engineering"
person.display()
print(person.school)