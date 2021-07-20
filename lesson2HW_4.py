#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 14:29:36 2021

@author:  蔡侑廷
"""


math = input('Please enter math grade ')
math = int(math)
eng = input('Please enter english grade ')
eng = int(eng)


if math >= 90 and eng >= 90:
    print('Prize')

elif math < 60 and eng < 60:
    print('Suprise! You win a punishment! YAY!')

elif math < 60 or eng <60:
    print('Try again next time')

else:
    print('No prize')
