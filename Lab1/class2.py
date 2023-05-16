#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 14:59:45 2022

@author: evastenberg
"""

class PersonClass: # define a class object
 def basicinfo(self, name, age):
     self.name=name
     self.age=age
 def display(self):
     print(self.name, '\n', self.age, '\n')
class StudentClass(PersonClass): # inherits basicinfo and display
 def moreinfo(self, university, major): # create moreinfo
     print(self.name + ' is a ' + major + ' student ' + 'from ' + university)
student=StudentClass() # make one instance
student.basicinfo('Cathy', 20)
student.display()
student.moreinfo('Santa Clara University', 'CSE')