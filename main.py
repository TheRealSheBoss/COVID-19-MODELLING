#!/usr/bin/env python

from graphs import graph_selection
from data_generation import data_generation
from info import info
from Regression_models import regression
from ExploratoryDataAnalysis import eda
from simulation import Main_function
from ExploratoryDataAnalysis import EDA

file_location = input("Where have you saved the non-master data? ")

data_generation(file_location)

function = ''


while function != "stop":
    print("This is case-sensitive! \n\n Type G for graph function \n\n I for variable information \n\n R for machine learning regression modelling"
          "\n\n E for eda \n\n S for simulation, or T for graph test "
          "or type stop to quit the program")
    function = input("What do you want to do? ")
    print(f'Input was {function}')
    if function == "G":
        graphs(file_location)
        continue
    if function == "T":
        graph_selection(file_location)
        continue
    if function == "I":
        info(file_location)
        continue
    if function == "R":
        regression(file_location)
        continue
    if function == "E":
        print ("Type 'P' for profile, \n 'H' for histplot, \n'L' for lineplot, \n and 'S' for scatterplot"
               "\n Remember, code is case-sensitive")
        eda = str(input('Select an option: '))
        if eda == 'P':
            EDA.master_data_profile()
        if eda == 'H':
            EDA.histplot_master_data()
        if eda == 'L':
            EDA.lineplot_master_data()
        if eda == 'S':
            EDA.scatterplot_master_data()
        else:
            EDA.heatmap_master_data()
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

