#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sea
import variable_finder
from variable_finder import Variable_Finder

def graphs(file_location):
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    import seaborn as sea
    import variable_finder
    from variable_finder import Variable_Finder

    ## Asking user to input where file location is saved
    
    ## Read the csv file to create a DataFrame
    master_data = pd.read_csv(f'{file_location}/Master Data.csv')

    ## Ask the user to select the X and Y variable of interest

    while True:
        plot_type = input('Do you want to plot a one variable (1) or two variable (2) graph? ')
        if plot_type == "1":
            var_choice = Variable_Finder("", master_data)          
            X = var_choice.variable_finder()         
            break
        elif plot_type == "2":
            var_choice = Variable_Finder("x", master_data)          
            X = var_choice.variable_finder()  
            var_choice = Variable_Finder("y", master_data)          
            Y = var_choice.variable_finder()  
            break
        else:
            print("Invalid input")
            continue

    if int(plot_type) == 2:

        class Data_Visualization():

            def __init__(self, X, Y):
                self.X = X
                self.Y = Y

            def scatterplots(self):
                """
                Function to create a scatter plot for the variables of interest.
                The function should be called on the X and Y variables previously defined by the user.
                The function then creates the figure and axis on which to plot the scatter graph.
                The user is asked to input the title for the figure and the x- and y-axis labels.
                The function then outputs the defined scatter plot.
                """
                fig, ax = plt.subplots(figsize = [10, 5]) #Create the figue, set the axes and figure size.
                title = input('Enter figure title: ') #Ask user to input title for figure
                xlabel = input('Enter label for x axis: ') #Ask user to input x-axis label
                ylabel = input('Enter label for y axis: ') #Ask user to input y-axis label
                ax.scatter(self.X, self.Y, color = 'b', marker = 'o', alpha=0.3) #Plot the scatter graph
                plt.title(title) #Plot the given title
                plt.xlabel(xlabel)#Plot the given x-axis label
                plt.ylabel(ylabel) #Plot the given y-axis label
                plt.show()

            def linegraph(self):
                """
                Function to produce line graph for given input values. 
                x_variables should be a 1-D or multi-D array. 
                y_variable should be a 1-D array.
                The function creates a single figure and axis. 
                The function asks the user how many x-variables are being looked at; if only 1 then the 1-D arrays of 
                x_variables and y_variable are plotted on a single line graph. If more than 1 then the function iterates
                through the arrays of x_variables, plotting each against the y_variable array.
                The user is asked to input the label for each x_variable, the y_variable, the x- and y-axis labels 
                and the title.
                When called, the function returns a single linegraph plot.
                """
                fig, ax = plt.subplots(figsize = (15,5))
                number_x_vars = input('How many x variables are you looking at? Enter integer only: ')
                xlabel = input('Enter label for x axis: ') #Ask user to input x-axis label
                ylabel = input('Enter label for y axis: ') #Ask user to input y-axis label
                title = input('Enter figure title: ') #Ask user to input title for figure
                if number_x_vars == '1':
                    plt.plot(self.X, self.Y, alpha=0.3)
                    plt.title(title)
                else:
                    for i in self.X:
                        label = input('Enter label for line for x variable in list position {index(i)} : ')
                        plt.plot(i, self.Y, label=label, alpha=0.3)
                        ax.set(title=title) #Plot the given title
                        plt.legend()
                plt.xlabel(xlabel)#Plot the given x-axis label
                plt.ylabel(ylabel) #Plot the given y-axis label
                plt.show()

            def bargraph(self):
                """
                Function to produce bar graph for given input values.
                the x_variables will be plotted against the y-variable,
                x-variables are typically non-numerical variables such as area name, etc.
                the y-variable which should be a numerical variable so our bar graph
                represents bars as high or low as its count.
                """
                fig, ax = plt.subplots(figsize=(15, 5))

                xlabel = input('Enter label for x axis: ')  # Ask user to input x-axis label
                ylabel = input('Enter label for y axis: ')  # Ask user to input y-axis label
                title = input('Enter figure title: ')  # Ask user to input title for figure

                x_bar_y = pd.concat([self.X, self.Y], axis=1)
                x_bar_y.plot(kind="bar", color='b', label="auto", ax=ax)
                ax.set(title=title, xlabel=xlabel, ylabel=ylabel)
                plt.show()

    # How to call the functions above:
    # bargraph function: Data_Visualization.bargraph(X,Y)
    # linegraph function: Data_Visualization.linegraph(X,Y)
    # scatterplots function: Data_Visualization.scatterplots(X,Y)

    elif int(plot_type) == 1:

        class Histo_Boxplot():

            def __init__(self, X):
                self.X = X

            def histogram(self):
                plt.hist(self.X, bins=30)
                title = input('Enter figure title: ') #Ask user to input title for figure
                plt.title(title) #Plot the given title   
                plt.show()

            def boxplot(self):
                plt.boxplot(self.X)
                title = input('Enter figure title: ') #Ask user to input title for figure
                xlabel = input('Enter label for x axis: ') #Ask user to input x-axis label
                ylabel = input('Enter label for y axis: ') #Ask user to input y-axis label
                plt.title(title) #Plot the given title   
                plt.xlabel(xlabel)#Plot the given x-axis label
                plt.ylabel(ylabel) #Plot the given y-axis label
                plt.show()
# =============================================================================
#                 number_x_vars = input('How many x variables are you looking at? Enter integer only: ')
#                 xlabel = input('Enter label for x axis: ') #Ask user to input x-axis label
#                 ylabel = input('Enter label for y axis: ') #Ask user to input y-axis label
#                 title = input('Enter figure title: ') #Ask user to input title for figure
#                 if number_x_vars == '1':
#                     plt.boxplot(self.X)
#                     plt.title(title)
#                 else:
#                     box_plot_data=[]
#                     labels = []
#                     for i in self.X:
#                         label = input('Enter label for line for x variable in list position {index(i)} : ')
#                         labels.append(label)
#                         box_plot_data.append(i)
#                     plt.boxplot(box_plot_data,labels=labels)
#                     ax.set(title=title) #Plot the given title
#                     plt.legend()    
#                 plt.xlabel(xlabel)#Plot the given x-axis label
#                 plt.ylabel(ylabel) #Plot the given y-axis label
#                 plt.title(title) #Plot the given title 
#                 plt.show()
# =============================================================================
                


    """
    def Boxplot():
        # For Covid-19 dataset BoxPlots can be created to compare infections/deaths/keyworkers/deprivation rate
        # by vaccination dose
        # % matplotlib inline (uncomment if using Jupyter NB)
        plt.figure(figsize=(25, 15))
        variables = input(f'Enter columns as specified in dataset: ')
        # separate columns with commas and place in quotation marks
        master_data_use = pd.DataFrame(columns=[variables])
        for all, column in enumerate(master_data_use.columns):
            plt.subplot(4, 6, all + 1)
            sea.boxplot(data=master_data_use[column])
            plt.title(column)
        plt.savefig(input('Enter figure title: '.png))
        plt.tight_layout()
        plt.show()
    Boxplot()
    """

    if int(plot_type) == 1:
         View_charts = Histo_Boxplot(X)
         while True:
             histo_or_boxplot = input('Do you want to plot a histogram (H) or boxplot (B)? ')
             if histo_or_boxplot == 'H':
                 View_charts.histogram()
                 break
             elif histo_or_boxplot == 'B':    
                 View_charts.boxplot()
                 break
             else:
                 print("Invalid input")
                 continue
    elif int(plot_type) == 2:
         View_Charts = Data_Visualization(X,Y)
         while True:
             bar_line_scatter = input('Do you want to plot a bar chart (B) or scatterplot (S)? ')
             if bar_line_scatter == 'B':
                 View_Charts.bargraph()
                 break
             elif bar_line_scatter == 'S':
                 View_Charts.scatterplots()
                 break
             else:
                 print("invalid input")
                 continue

def graph_selection(file_location):
    master_data = pd.read_csv(f'{file_location}/Master Data.csv')
    while True:
        no_x_vars = input('How many X variables do you want to visualise (must be integer greater than zero?): ')
        try:
            no_x_vars = int(no_x_vars)
        except ValueError:
            print("Invalid input")
        if no_x_vars == 1:
            var_choice = Variable_Finder("", master_data)          
            x_variable = var_choice.variable_finder() 
            x_label = input("Input x variable label: ")
            while True:
                no_y_vars = input('Do you want to look at a Y variable? (Y / N): ')
                if no_y_vars == 'Y':
                    var_choice = Variable_Finder("", master_data)
                    y_variable = var_choice.variable_finder()
                    y_label = input("Input y variable label: ")
                    while True: 
                        graph_type = input("Would you like to plot a scatter (S), line (L) or bar (B) graph?: ")
                        if graph_type == "S":
                            title = input("Enter title for scatter plot: ")
                            View_Charts = Data_Viz(x_variable, y_variable, x_label, x_label, y_label, title)
                            View_Charts.scatter()
                            break
                        elif graph_type == "L":
                            title = input("Enter title for line plot: ")
                            View_Charts = Data_Viz(x_variable, y_variable, x_label, x_label, y_label, title)
                            View_Charts.single_line()
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
                            y_label = x_label
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
               var_choice = Variable_Finder("", master_data)          
               x_variable = var_choice.variable_finder() 
               x_variables.append(x_variable.to_numpy())
               x_label = input("Input x variable label: ")
               x_variable_names.append(x_label)
            #x_variables = np.vstack(x_variables)
            print(x_variables)
            print(x_variable_names)
            x_label = input("Enter x-axis label: ")
            while True:
                no_y_vars = input('Do you want to look at a Y variable? (Y / N): ')
                if no_y_vars == 'Y':
                    var_choice = Variable_Finder("", master_data)
                    y_variable = var_choice.variable_finder()
                    y_label = input("Input y variable label: ")
                    title = input("Enter title for line plot: ")
                    #x_variable_names = np.vstack(x_variable_names)
                    View_Charts = Data_Viz(x_variables, y_variable, x_variable_names, x_label, y_label, title)
                    View_Charts.multi_line()
                    break
                    
                elif no_y_vars == 'N':
                    y_variable = None
                    title = input("Enter title for boxplot: ")
                    y_label = input("Enter y-axis label: ")
                    View_Charts = Data_Viz(x_variables, y_variable, x_variable_names, x_label, y_label, title)
                    View_Charts.multi_boxplot()
                    break
                else:
                    print("Invalid input")
                    continue
        else:
            print("Invalid input")
            continue
        break

class Data_Viz():
    def __init__(self, x_data, y_data, x_variable_names, x_label, y_label, title):
        self.x_data = x_data
        self.y_data = y_data
        self.x_variable_names = x_variable_names
        self.x_label = x_label
        self.y_label = y_label
        self.title = title
        
    def boxplot(self):
        plt.boxplot(self.x_data)
        plt.title(self.title) #Plot the given title   
        plt.xlabel(self.x_label)#Plot the given x-axis label
        plt.ylabel(self.y_label) #Plot the given y-axis label
        plt.show()
    
    def multi_boxplot(self):
        plt.boxplot(self.x_data,labels=self.x_variable_names)
        plt.rcParams["figure.figsize"] = [7.50, 3.50]
        plt.rcParams["figure.autolayout"] = True 
        plt.xlabel(self.x_label, fontsize=12)
        plt.ylabel(self.y_label, fontsize=12) 
        plt.title(self.title, fontsize=18) 
        plt.show()
        
    def scatter(self):
        """
        Function to create a scatter plot for the variables of interest.
        The function should be called on the X and Y variables previously defined by the user.
        The function then creates the figure and axis on which to plot the scatter graph.
        The user is asked to input the title for the figure and the x- and y-axis labels.
        The function then outputs the defined scatter plot.
        """
        fig, ax = plt.subplots(figsize = [10, 5]) #Create the figue, set the axes and figure size.
        ax.scatter(self.x_data, self.y_data, color = 'b', marker = 'o', alpha=0.3) #Plot the scatter graph
        plt.title(self.title) #Plot the given title
        plt.xlabel(self.x_label)#Plot the given x-axis label
        plt.ylabel(self.y_label) #Plot the given y-axis label
        plt.show()
    
    def single_line(self):
        """
        Function to produce line graph for given input values. 
        x_variable should be a 1-D array. 
        y_variable should be a 1-D array.
        The function creates a single figure and axis. 
        The 1-D arrays of x_variables and y_variable are plotted on a single line graph. 
        When called, the function returns a single linegraph plot.
        """
        fig, ax = plt.subplots(figsize = (15,5))
        plt.plot(self.x_data, self.y_data, alpha=0.3)
        plt.title(self.title)
        plt.xlabel(self.x_label)#Plot the given x-axis label
        plt.ylabel(self.y_label) #Plot the given y-axis label
        plt.show()
        
    def multi_line(self):
        """
        Function to produce line graph for given input values. 
        x_variables should be a 1-D or multi-D array. 
        y_variable should be a 1-D array.
        The function creates a single figure and axis. 
        The function asks the user how many x-variables are being looked at; if only 1 then the 1-D arrays of 
        x_variables and y_variable are plotted on a single line graph. If more than 1 then the function iterates
        through the arrays of x_variables, plotting each against the y_variable array.
        The user is asked to input the label for each x_variable, the y_variable, the x- and y-axis labels 
        and the title.
        When called, the function returns a single linegraph plot.
        """
        fig, ax = plt.subplots(figsize = (15,5))
        for i in range(len(self.x_data)):
            label = self.x_variable_names[i]
            plt.plot(self.y_data, self.x_data[i], label=label, alpha=0.3)
            ax.set(title=self.title) #Plot the given title
            plt.legend()
        plt.xlabel(self.x_label)#Plot the given x-axis label
        plt.ylabel(self.y_label) #Plot the given y-axis label
        plt.show()
        
        
    def histogram(self):
        plt.hist(self.x_data, bins=30)
        plt.xlabel(self.x_label)
        plt.ylabel('Count')
        plt.title(self.title)    
        plt.show()
        
    def bargraph(self):
        """
        Function to produce bar graph for given input values.
        the x_variables will be plotted against the y-variable,
        x-variables are typically non-numerical variables such as area name, etc.
        the y-variable which should be a numerical variable so our bar graph
        represents bars as high or low as its count.
        """
        fig, ax = plt.subplots(figsize=(15, 5))
        x_bar_y = pd.concat([self.x_data, self.y_data], axis=1)
        x_bar_y.plot(kind="bar", color='b', label="auto", ax=ax)
        ax.set(title=self.title, xlabel=self.x_label, ylabel=self.y_label)
        plt.show()    
        
        
        
        
        
        
        
        
        
        
        