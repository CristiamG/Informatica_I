# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 17:06:47 2020

@author: User
"""

a = int (input ('Ingrese el valor de año: '))
if ((a%4==0) and (a%100!=0)) or a%400==0:
    print ('el año es bisiesto')
else:
    print ('el año no es bisiesto').
