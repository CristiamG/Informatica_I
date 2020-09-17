# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 11:24:40 2020

@author: User
"""

numero = int (input ('Ingrese el valor del numero que quiere invertir: '))
invertido=(numero%1000-numero%100)//100+numero%100-numero%10+(numero%10)*100
print ('Valor invertido es: ', (invertido))

