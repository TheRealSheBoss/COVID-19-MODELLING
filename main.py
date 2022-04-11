#!/usr/bin/env python

from graphs import graphs
from data_generation import data_generation
from info import info
from ai_models import model_choice
from ExploratoryDataAnalysis import eda

file_location = input("Where have you saved the non-master data? ")

data_generation(file_location)

function = ""


while function != "stop":
    print("Type G for graph function, I for variable information, A for AI modelling, E for eda or type stop to quit the program")
    function = input("What do you want to do? ")
    print(f'Input was {function}')
    if function == "G":
        graphs(file_location)
        continue
    if function == "I":
        info(file_location)
        continue
    if function == "A":
        model_choice(file_location)
        continue
    if function == "E":
        eda(file_location)
        continue
    if function == "stop":
        print("Stopping")
        break
    else:
        print("Invalid input")
        continue
    
