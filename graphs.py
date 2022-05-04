#!/usr/bin/env python
import matplotlib
#matplotlib.use('TkAgg') #comment out if using Jupyter notebook.
#%matplotlib inline  #(comment out if not using Jupyter NB)
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sea
import variable_finder
from variable_finder import Variable_Finder

"""
To allow the user to explore the data and specific variables of interest, the
function graph_selection() has been designed to be interactive via the terminal
when run from covid_project.py, this allows the user to input the variables of interest
which they wish to visualise and, based on the number of variables of interest,
the function returns options to the user as to which type of graph they wish to
plot. graph_selection() then calls the relevant function from the class 
Data_Viz() to return the plot of interest to the user. 

The class Data_Viz() has been designed in such a way that it can be used
in different combinations with functions across modules within this program, 
or indeed any other module of interest. 
For example, the multi_boxplot(), multi_line() and scatter() functions are     
also called into the Regression_models.py module within this program.

The class BarChart() is defined within the graph_selection() function as, given 
the nature of the data this program is intended to be used with, processing of 
some variables is required before a bargraph can be plot. Therefore, the 
bargraph() function is defined and called within the confines of 
graph_selection() and has not been designed for reuse in the class Data_Viz().
"""

def graph_selection(file_location):
    """
    Function returns interactive interface with the user via the terminal to
    allow the user to input variables of interest. Dependent on the number of 
    variables entered, the function calls the relevant graph funtion from 
    Data_Viz() or BarChart() which displays the resulting graph. 
    
    Graph plotting options:
        1 X variable, no Y variable: histogram or boxplot
        1 X variable, 1 Y variable: scatter plot or barchart
        >1 X variables, no Y variable: boxplot
        >1 X variables, 1 Y variable: line plot

    """
    import matplotlib
    #matplotlib.use('TkAgg') #comment out if using Jupyter notebook.
    #%matplotlib inline  #(comment out if not using Jupyter NB)
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    import seaborn as sea
    import variable_finder
    from variable_finder import Variable_Finder
    
    
    master_data = pd.read_csv(f'{file_location}/Master Data.csv')
    
                
    class BarChart():
        def __init__(self, x_data, y_data, x_variable_names, x_label, y_label, title):
            self.x_data = x_data
            self.y_data = y_data
            self.x_variable_names = x_variable_names
            self.x_label = x_label
            self.y_label = y_label
            self.title = title
        
        def bargraph(self):
            """
            If chosen X variable is Local Authority, user required to try 
            Region as an alternative, as Local Authority has too many x-ticks 
            to return a meaningful graph. 
            Creates quartiles of the X variable of interest, if numerical.
            Displays (and saves) a bargraph plot.
            """
            fig, ax = plt.subplots(figsize=(15, 5))
            
            if self.x_data.dtype == float:
                
                q = master_data.quantile([0.00, 0.25, 0.50, 0.75, 1.00])
                
                q1 = master_data[((master_data[self.x_data.name]>=q[self.x_data.name][0.00]) & (master_data[self.x_data.name]<q[self.x_data.name][0.25]))]
                q2 = master_data[((master_data[self.x_data.name]>=q[self.x_data.name][0.25]) & (master_data[self.x_data.name]<q[self.x_data.name][0.50]))]
                q3 = master_data[((master_data[self.x_data.name]>=q[self.x_data.name][0.50]) & (master_data[self.x_data.name]<q[self.x_data.name][0.75]))]
                q4 = master_data[((master_data[self.x_data.name]>=q[self.x_data.name][0.75]) & (master_data[self.x_data.name]<=q[self.x_data.name][1.00]))]
        
                X_bar = [f'{self.x_data.name} First Quartile', f'{self.x_data.name} Second Quartile', f'{self.x_data.name} Third Quartile', f'{self.x_data.name} Fourth Quartile']
        
                Y_bar = [q1[self.y_data.name].mean(), q2[self.y_data.name].mean(), q3[self.y_data.name].mean(), q4[self.y_data.name].mean()]
        
                plt.bar(X_bar,Y_bar, color='b', label ='auto')
                ax.set(title=self.title, xlabel=self.x_label, ylabel=self.y_label)
                plt.show()   
                while True:
                    save_image = input("Do you want to save the image? (Y/N): ")
                    if save_image == "Y":
                        fig, ax = plt.subplots(figsize=(15, 5))
                        plt.bar(X_bar,Y_bar, color='b', label ='auto')
                        ax.set(title=self.title, xlabel=self.x_label, ylabel=self.y_label)
                        plt.savefig('bargraph_plot.png', bbox_inches='tight')
                        plt.savefig('bargraph_plot.pdf', bbox_inches='tight')
                    elif save_image == "N":
                        break
                    else:
                        print("Invalid input")
                        continue
                    break
                
            elif self.x_data.name == "Local Authority":
                print("Too many X data points to plot effectively, try plotting region name instead")
                    
            elif self.x_data.name == "Region name":
                    
                master_data_copy = master_data.copy()
    
                master_data_copy.replace('East Midlands', 'EM', inplace = True)
                
                master_data_copy.replace('South East', 'SE', inplace = True)
                
                master_data_copy.replace('North East', 'NE', inplace = True)
                
                master_data_copy.replace('North West', 'NW', inplace = True)
                
                master_data_copy.replace('South West', 'SW', inplace = True)
                
                master_data_copy.replace('Yorkshire and The Humber', 'YH', inplace = True)
                
                master_data_copy.replace('West Midlands', 'WM', inplace = True)
                
                X_bar = master_data_copy[self.x_data.name]
    
                Y_mean = master_data_copy.groupby(X_bar).mean()
                
                Y_bar = Y_mean[self.y_data.name]
                
                plt.bar(Y_bar.index,Y_bar, color='b', label ='auto')
                ax.set(title=self.title, xlabel=self.x_label, ylabel=self.y_label)
                plt.show()   
                while True:
                    save_image = input("Do you want to save the image? (Y/N): ")
                    if save_image == "Y":
                        fig, ax = plt.subplots(figsize=(15, 5))
                        plt.bar(Y_bar.index,Y_bar, color='b', label ='auto')
                        ax.set(title=self.title, xlabel=self.x_label, ylabel=self.y_label)
                        plt.savefig('bargraph_plot.png',format='png', dpi=800, bbox_inches='tight')
                        plt.savefig('bargraph_plot.pdf', bbox_inches='tight')    
                    elif save_image == "N":
                        break
                    else:
                        print("Invalid input")
                        continue
                    break
    
    while True:
        try:
            no_x_vars = input('How many X variables do you want to visualise (must be integer greater than zero?): ')
            no_x_vars = int(no_x_vars)
            if no_x_vars < 1:
                print("Must be at least 1 X variable")
                continue
        except ValueError:
            print("Invalid input")
            continue
        if no_x_vars == 1:
            var_choice = Variable_Finder("x", master_data)          
            x_variable = var_choice.variable_finder() 
            x_label = input("Input x variable label: ")
            while True:
                no_y_vars = input('Do you want to look at a Y variable? (Y / N): ')
                if no_y_vars == 'Y':
                    var_choice = Variable_Finder("y", master_data)
                    y_variable = var_choice.variable_finder()
                    y_label = input("Input y variable label: ")
                    while True: 
                        graph_type = input("Would you like to plot a scatter (S) or a bar chart (B)?: ")
                        if graph_type == "S":
                            title = input("Enter title for scatter plot: ")
                            View_Charts = Data_Viz(x_variable, y_variable, x_label, x_label, y_label, title)
                            View_Charts.scatter()
                            break
                        elif graph_type == "B":
                            title = input("Enter title for bar plot: ")
                            View_Bar = BarChart(x_variable, y_variable, x_label, x_label, y_label, title)
                            View_Bar.bargraph()
                            break
                        else:
                            print("Invalid input")
                            continue
                elif no_y_vars == 'N':
                    y_variable = None
                    while True: 
                        graph_type = input("Would you like to plot a histogram (H) or boxplot (B): ")
                        if graph_type == "H":
                            title = input("Enter title for histogram plot: ")
                            y_label = 'Count'
                            View_Charts = Data_Viz(x_variable, y_variable, x_label, x_label, y_label, title)
                            View_Charts.histogram()
                            break
                        elif graph_type == "B":
                            title = input("Enter title for boxplot: ")
                            y_label = input("Enter label for y-axis: ")
                            View_Charts = Data_Viz(x_variable, y_variable, x_label, x_label, y_label, title)
                            View_Charts.boxplot()
                            break
                        else:
                            print("Invalid input")
                            continue
                else:
                    print("Invalid input")
                    continue
                break
        elif int(no_x_vars) > 1:
            x_variables = []
            x_variable_names = []
            for i in range(int(no_x_vars)):
               var_choice = Variable_Finder("x", master_data)          
               x_variable = var_choice.variable_finder() 
               x_variables.append(x_variable.to_numpy())
               x_label = input("Input x variable label: ")
               x_variable_names.append(x_label)
            x_label = input("Enter x-axis label: ")
            y_variable = None
            title = input("Enter title for boxplot: ")
            y_label = input("Enter y-axis label: ")
            View_Charts = Data_Viz(x_variables, y_variable, x_variable_names, x_label, y_label, title)
            View_Charts.multi_boxplot()
            
        else:
            print("Invalid input")
            continue
        break



class Data_Viz():
    """
    The Data_Viz class defines reusable functions to produce boxplots, 
    multi-variable boxplots, scatter plots, single- and multi-line plots, and
    histograms. 
    The class takes as input:
        x_data = a list, array or multiple array of data for the X variables 
                of interest.
        y_data = a list or array of data for the Y variable of interest.
        x_variable_names = a list of strings with the name for each X variable, 
                in the same order as the X variable data provided in x_data.
        x_label = a string, providing the label for the x-axis
        y_label = a string, providing the label for the y-axis
        title = a string, providing the title for the plot
    
    The class should be called with all arguments listed above. If an argument 
    isn't relevant for the plot the user wishes to make None should be entered 
    instead.  
    
    Example
    =======
    Create a multi-boxplot graph comparing the mean squared errors of three 
    regression models.
    
    mean_squared_errors = [[3.11, 4.23, 8.96], [5.77, 9.11, 7.33], 
                           [12.35, 10.67, 15.22]]
    X_variables = ['Decision tree regression', 'Linear regression', 
                   'Polynomial regression']
    XLabel = 'Regression models'
    YLabel = 'Mean Squared Error'
    Title = 'Comparison of regression models'
    Charts = Data_Viz(mean_squared_errors, X_variables, None, XLabel, YLabel, 
                      Title)
    Charts.multi_boxplot()
    
    Output: GUI display of the graph. User asked to input Y/N as to whether 
    they want to save the plot as a PDF. If 'Y', plot saved as PDF to the PATH
    the program is being run from.
    """
    
    
    def __init__(self, x_data, y_data, x_variable_names, x_label, y_label, title):
        self.x_data = x_data
        self.y_data = y_data
        self.x_variable_names = x_variable_names
        self.x_label = x_label
        self.y_label = y_label
        self.title = title
        
            
    def boxplot(self):
        """Displays (and saves) a single variable boxplot."""
        plt.clf()
        box_plt = plt.boxplot(self.x_data)
        plt.xticks([])
        plt.title(self.title, pad=18.0) #Plot the given title   
        plt.xlabel(self.x_label)#Plot the given x-axis label
        plt.ylabel(self.y_label) #Plot the given y-axis label
        plt.show()
        while True:
            save_image = input("Do you want to save the image? (Y/N): ")
            if save_image == "Y":
                plt.boxplot(self.x_data)
                plt.xticks([])
                plt.title(self.title, pad=18.0) #Plot the given title   
                plt.xlabel(self.x_label)#Plot the given x-axis label
                plt.ylabel(self.y_label) #Plot the given y-axis label
                plt.savefig('boxplot.pdf', format='png', dpi=800, bbox_inches='tight')
                plt.savefig('boxplot.png', bbox_inches='tight')
            elif save_image == "N":
                break
            else:
                print("Invalid input")
                continue
            break
        
        
    def multi_boxplot(self):
        """Displays (and saves) a multi-variable boxplot."""
        plt.clf()
        plt.boxplot(self.x_data,labels=self.x_variable_names)
        plt.rcParams["figure.figsize"] = [7.50, 3.50]
        plt.rcParams["figure.autolayout"] = True 
        plt.xlabel(self.x_label, fontsize=12)
        plt.ylabel(self.y_label, fontsize=12) 
        plt.title(self.title, fontsize=18, pad=18.0) 
        plt.show()
        while True:
            save_image = input("Do you want to save the image? (Y/N): ")
            if save_image == "Y":
                plt.boxplot(self.x_data,labels=self.x_variable_names)
                plt.rcParams["figure.figsize"] = [7.50, 3.50]
                plt.rcParams["figure.autolayout"] = True 
                plt.xlabel(self.x_label, fontsize=12)
                plt.ylabel(self.y_label, fontsize=12) 
                plt.title(self.title, fontsize=18, pad=18.0)
                plt.savefig('multi_boxplot.pdf', format='png', dpi=800, bbox_inches='tight')
                plt.savefig('multi_boxplot.png', bbox_inches='tight')
            elif save_image == "N":
                break
            else:
                print("Invalid input")
                continue
            break
            
    def scatter(self):
        """Displays (and saves) a scatter plot."""
        plt.clf()
        fig, ax = plt.subplots(figsize = [10, 5]) #Create the figue, set the axes and figure size.
        ax.scatter(self.x_data, self.y_data, color = 'b', marker = 'o', alpha=0.3) #Plot the scatter graph
        plt.title(self.title, pad=18.0) #Plot the given title
        plt.xlabel(self.x_label)#Plot the given x-axis label
        plt.ylabel(self.y_label) #Plot the given y-axis label
        plt.show()
        while True:
            save_image = input("Do you want to save the image? (Y/N): ")
            if save_image == "Y":
                fig, ax = plt.subplots(figsize = [10, 5]) #Create the figue, set the axes and figure size.
                ax.scatter(self.x_data, self.y_data, color = 'b', marker = 'o', alpha=0.3) #Plot the scatter graph
                plt.title(self.title, pad=18.0) #Plot the given title
                plt.xlabel(self.x_label)#Plot the given x-axis label
                plt.ylabel(self.y_label) #Plot the given y-axis label
                plt.savefig('scatter_plot.pdf', bbox_inches='tight')
                plt.savefig('scatter_plot.png', format='png', dpi=800, bbox_inches='tight')
            elif save_image == "N":
                break
            else:
                print("Invalid input")
                continue
            break
        
    def single_line(self):
        """Displays (and saves) a single x variable linegraph plot."""
        plt.clf()
        fig, ax = plt.subplots(figsize = (15,5))
        plt.plot(self.x_data, self.y_data, alpha=0.3)
        plt.title(self.title, pad=18.0)
        plt.xlabel(self.x_label)#Plot the given x-axis label
        plt.ylabel(self.y_label) #Plot the given y-axis label
        plt.show()
        while True:
            save_image = input("Do you want to save the image? (Y/N): ")
            if save_image == "Y":
                fig, ax = plt.subplots(figsize = (15,5))
                plt.plot(self.x_data, self.y_data, alpha=0.3)
                plt.title(self.title, pad=18.0)
                plt.xlabel(self.x_label)#Plot the given x-axis label
                plt.ylabel(self.y_label) #Plot the given y-axis label
                plt.savefig('single_line_plot.pdf', bbox_inches='tight')
                plt.savefig('single_line_plot.png', format='png', dpi=800, bbox_inches='tight')
            elif save_image == "N":
                break
            else:
                print("Invalid input")
                continue
            break
            
    def multi_line(self):
        """Displays (and saves) a multi-x variable linegraph plot.""" 
        from matplotlib.ticker import MaxNLocator
        plt.clf()
        fig, ax = plt.subplots(figsize = (15,5))
        for i in range(len(self.x_data)):
            label = self.x_variable_names[i]
            plt.plot(self.y_data, self.x_data[i], label=label, alpha=0.3)
            ax.set(title=self.title) 
            plt.legend()
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label) 
        plt.show()
        while True:
            save_image = input("Do you want to save the image? (Y/N): ")
            if save_image == "Y":
                fig, ax = plt.subplots(figsize = (15,5))
                for i in range(len(self.x_data)):
                    label = self.x_variable_names[i]
                    plt.plot(self.y_data, self.x_data[i], label=label, alpha=0.3)
                    ax.set(title=self.title) 
                    plt.legend()
                plt.xlabel(self.x_label)
                plt.ylabel(self.y_label) 
                plt.savefig('multi_line_plot.pdf', bbox_inches='tight')
                plt.savefig('multi_line_plot.png', format='png', dpi=800, bbox_inches='tight')
            elif save_image == "N":
                break
            else:
                print("Invalid input")
                continue
            break
            
            
    def histogram(self):
        """Displays (and saves) a histogram plot."""
        plt.clf()
        plt.hist(self.x_data, bins=30)
        plt.xlabel(self.x_label)
        plt.ylabel('Count')
        plt.title(self.title, pad=18.0)    
        plt.show()
        while True:
            save_image = input("Do you want to save the image? (Y/N): ")
            if save_image == "Y":
                plt.hist(self.x_data, bins=30)
                plt.xlabel(self.x_label)
                plt.ylabel('Count')
                plt.title(self.title, pad=18.0)
                plt.savefig('histogram_plot.pdf', bbox_inches='tight')
                plt.savefig('histogram_plot.png', format='png', dpi=800, bbox_inches='tight')
            elif save_image == "N":
                break
            else:
                print("Invalid input")
                continue
            break
            
