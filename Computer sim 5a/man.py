# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 10:48:43 2022

@author: damsk
"""
import numpy as np
filein = open("Mars.txt", "r")
        
temp1 = filein.read().splitlines()

tokens1 = temp1[2].split(",")
a = np.array((int(tokens1[0]), int(tokens1[1])))

tokens2 = temp1[3].split(",")
b = np.array((int(tokens2[0]), int(tokens2[1])))

tokens3 = temp1[4].split(",")
c = np.array((int(tokens3[0]), int(tokens3[1])))

print(tokens1)
print(temp1)