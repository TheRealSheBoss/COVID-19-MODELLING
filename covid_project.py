#!/usr/bin/env python

from graphs import graph_selection
from data_generation import data_generation
from info import info
from Regression_models import regression
from simulation import Main_function
from ExploratoryDataAnalysis import eda_selection
from ExploratoryDataAnalysis import ExploreMasterData

"""
This program prompts the user to input the location they saved the relevant files - and then the data_generation program 
is used to generate the master data. After this, a while loop is used to generate an interface where the user choices which
function of the program to use. This loop breaks only if the user inputs stop. 

Each file which the user can select to use contains a function which file_location is passed to. This means that these files 
can have access to master_data, without the user having to input the file location repeatedly.
"""

file_location = input("Where have you saved the non-master data? ")

data_generation(file_location)

function = ''


while function != "stop":
    print("\n\n This is case-sensitive! \n\n Type G for graph function \n\n I for variable information \n\n R for machine learning regression modelling"
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

