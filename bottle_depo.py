#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 20:08:27 2020

@author: geethikalakshmi
"""
less_depo=0.10
more_depo=0.25

less=float(input('how many 1 litre containers do you have?'))
more=float(input('how many more than 1 ltre containers do you have?'))
refund=less*less_depo+more*more_depo
print('total refund is $.2f.'% refund)
