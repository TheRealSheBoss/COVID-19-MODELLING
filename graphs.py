#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sea

## Asking user to input where file location is saved
master_data_input = input("Please enter dataset path in csv: ")
## Read the csv file to create a DataFrame
master_data = pd.read_csv(master_data_input)


## Ask the user to select the X and Y variable of interest

plot_type = input("Do you want to plot a one variable (1) or two variable (2) graph? ")
if int(plot_type) == 1:
    X_var = input("Which x variable do you want to look at (enter exact from Parameter names): ")
    X = master_data[X_var]
elif int(plot_type) == 2:
    X_var = input("Which x variable do you want to look at (enter exact from Parameter names): ")
    Y_var = input("Which y variable do you want to look at (enter exact from Parameter names): ")
    X = master_data[X_var]
    Y = master_data[Y_var]

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
        title = input("Enter figure title: ") #Ask user to input title for figure
        xlabel = input("Enter label for x axis: ") #Ask user to input x-axis label
        ylabel = input("Enter label for y axis: ") #Ask user to input y-axis label
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
        number_x_vars = input("How many x variables are you looking at? Enter integer only: ")
        xlabel = input("Enter label for x axis: ") #Ask user to input x-axis label
        ylabel = input("Enter label for y axis: ") #Ask user to input y-axis label
        title = input("Enter figure title: ") #Ask user to input title for figure
        if number_x_vars == '1':
            plt.plot(self.X, self.Y, alpha=0.3)
            plt.title(title)
        else:
            for i in self.X:
                label = input("Enter label for line for x variable in list position {index(i)} : ")
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

        xlabel = input("Enter label for x axis: ")  # Ask user to input x-axis label
        ylabel = input("Enter label for y axis: ")  # Ask user to input y-axis label
        title = input("Enter figure title: ")  # Ask user to input title for figure

        x_bar_y = pd.concat([self.X, self.Y], axis=1)
        x_bar_y.plot(kind="bar", color='b', label="auto", ax=ax)
        ax.set(title=title, xlabel=xlabel, ylabel=ylabel)
        plt.show()

View_Charts = Data_Visualization(X,Y)


# How to call the functions above:
# bargraph function: Data_Visualization.bargraph(X,Y)
# linegraph function: Data_Visualization.linegraph(X,Y)
# scatterplots function: Data_Visualization.scatterplots(X,Y)

class Histo_Boxplot():
    
    def __init__(self, X):
        self.X = X

    def histogram(self):
        plt.hist(self.X, bins=30)
        title = input("Enter figure title: ") #Ask user to input title for figure
        plt.title(title) #Plot the given title   
        plt.show()
    
    def boxplot(self):
        plt.boxplot(self.X)
        title = input("Enter figure title: ") #Ask user to input title for figure
        xlabel = input("Enter label for x axis: ") #Ask user to input x-axis label
        ylabel = input("Enter label for y axis: ") #Ask user to input y-axis label
        plt.title(title) #Plot the given title   
        plt.xlabel(xlabel)#Plot the given x-axis label
        plt.ylabel(ylabel) #Plot the given y-axis label
        plt.show()
        
View_charts = Histo_Boxplot(X)

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
    histo_or_boxplot = input("Do you want to plot a histogram (H) or boxplot (B)? ")
    if histo_or_boxplot == "H":
        View_charts.histogram()
    elif histo_or_boxplot == "B":    
        View_charts.boxplot()
elif int(plot_type) == 2:
    bar_line_scatter = input("Do you want to plot a bar chart (B), linegraph (L) or scatterplot (S)? ")
    if bar_line_scatter == "B":
        View_Charts.bargraph()
    elif bar_line_scatter == "L":
        View_Charts.linegraph()
    elif bar_line_scatter == "S":
        View_Charts.scatterplots()



