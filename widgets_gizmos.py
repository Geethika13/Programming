#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 20:09:00 2020

@author: geethikalakshmi
"""
#define the given conditions.
widgets= 75
gizmos=112
#input the values 
a=int(input('enter the number of widgets..:'))
b=int(input('enter the number of gizmos..:'))
#calculate the total weight
tot=a*widgets+b*gizmos
#display the total weights in grams
print('total weight of the items purchased is..:',tot,'gms')
