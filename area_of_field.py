#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 19:58:57 2020

@author: geethikalakshmi
"""

length=float(input('enter the length of the field'))
width=float(input('enter the width of the field'))
area=length*width
sqrt_per_acre=43560
acre=area/sqrt_per_acre
print('area of field is:',acre,'acres')