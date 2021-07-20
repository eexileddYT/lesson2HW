#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 19:50:14 2021

@author: 蔡侑廷
"""

    
math = input('Please enter math grade ')
math = int(math)
eng = input('Please enter english grade ')
eng = int(eng)

if math >= 90 and eng >= 90: 
    print('YOU WIN A PRIZE ')
elif math == 100 or eng == 100:
    print('YOU WIN A PRIZE ')
else:
    print('oof no prize')
if math == 0 and eng == 0 :
    print('redo this year and win a blob of poop')
    