#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 20:08:27 2020

@author: geethikalakshmi
"""
#defining the refund values per container
less_depo=0.10
more_depo=0.25
#input the values by the user 
less=float(input('how many 1 litre containers do you have?'))
more=float(input('how many more than 1 ltre containers do you have?'))
#displaying total refund value with two decimal places
refund=less*less_depo+more*more_depo
print('total refund is $.2f.'% refund)
