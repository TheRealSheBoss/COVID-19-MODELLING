
import pandas as pd

"""
Variable finder is a class which confirms that a variable that the user inserted exists in the dataset. 
If the variable does not exist, a while True loop repeats and the user is prompted to enter a variable name again. 
The class also takes an input of the variable type that the user must input. For example, if the variable is the X 
variable of a graph, the class will ask the user “Which X variable do you want to look at?”. 

It was chosen to make variable finder a class because the user is regularly asked to input a variable name, 
and using a class reduces the amount of repeated code, and allows its use across different files. 

Try and except is used to prevent KeyError from crashes the program, when a name not in the dataset is inputted.
"""

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
