
import pandas as pd

class Variable_Finder():
    def __init__(self, var_type, master_data):
        self.var_type = var_type
        self.master_data = master_data
        
	
    def variable_finder(self):
        while True:
            var = input(f'Which {self.var_type} variable do you want to look at (enter exact from Parameter names): ')
       	    try:
                   variable = self.master_data[var]
                   return variable
                   break
            except KeyError:
           		   print("Variable not found")
           		   continue