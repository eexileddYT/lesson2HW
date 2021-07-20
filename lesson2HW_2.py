#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 19:45:09 2021

@author: 蔡侑廷
"""
   
    
score = int(input('Please enter a grade 0-100 '))


if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print ('C')
elif score >= 60:
    print('D')
elif score == 0:
    print('what are you doing in class?')
else:
    print ('E')
    

