#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 16:05:36 2022

@author: danieljoinson
"""

from graphs import graphs
from data_generation import data_generation
from info import info
from ai_models import model_choice

file_location = input("Where have you saved the non-master data? ")

data_generation(file_location)

function = ""


while function != "stop":
    print("Type G for graph function, I for variable information, A for AI modelling, type stop to quit the program")
    function = input("What do you want to do? ")
    print(f'Input was {function}')
    if function == "G":
        graphs(file_location)
        continue
    if function == "I":
        info()
        continue
    if function == "A":
        model_choice(file_location)
        continue
    if function == "stop":
        print("Stopping")
        break
    else:
        print("Invalid input")
        continue 
    
