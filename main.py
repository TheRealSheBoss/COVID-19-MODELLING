#!/usr/bin/env python

from graphs import graph_selection
from data_generation import data_generation
from info import info
from Regression_models import regression
from simulation import Main_function
from ExploratoryDataAnalysis import eda_selection
from ExploratoryDataAnalysis import ExploreMasterData

file_location = input("Where have you saved the non-master data? ")

data_generation(file_location)

function = ''


while function != "stop":
    print("This is case-sensitive! \n\n Type G for graph function \n\n I for variable information \n\n R for machine learning regression modelling"
          "\n\n E for eda \n\n or S for simulation "
          "or type stop to quit the program")
    function = input("What do you want to do? ")
    print(f'Input was {function}')
    if function == "G":
        graph_selection(file_location)
        continue
    if function == "I":
        info(file_location)
        continue
    if function == "R":
        regression(file_location)
        continue
    if function == "E":
        eda_selection(file_location)
        continue
    if function == "S":
        Main_function()
        continue
    if function == "stop":
        print("Stopping")
        break
    else:
        print("Invalid input")
        continue

