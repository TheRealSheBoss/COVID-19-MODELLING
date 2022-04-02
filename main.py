#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 16:05:36 2022

@author: danieljoinson
"""

from graphs import graphs
from data_generation import data_generation
from info import info

data_generation()

function = ""


while function != "stop":
    print("Type G for graph function, I for variable information, type stop to quit the program")
    function = input("What do you want to do? ")
    print(f'Input was {function}')
    if function == "G":
        graphs()
        continue
    if function == "I":
        info()
        continue
        
else:
    print("Stopping")
    