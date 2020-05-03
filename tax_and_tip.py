#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 20:35:15 2020

@author: geethikalakshmi
"""
#dfining the values of taxes and tips 
tax_rate=0.18
tip_rate=0.10
#input the values
cost=float(input('enter the cost of the meal:'))
#calculating the tax,tip and cost
tax=cost*tax_rate
tip=cost*tip_rate
total=cost+tax+tip
#displaying the result
print('the tax is %.2f and the tip is %.2f making the total %.2f:'%\
      (cost,tax,tip,total))
