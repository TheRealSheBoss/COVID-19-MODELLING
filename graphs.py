#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sea
import variable_finder
from variable_finder import Variable_Finder

def graph_selection(file_location):
    master_data = pd.read_csv(f'{file_location}/Master Data.csv')
    
    class Data_Viz():
        def __init__(self, x_data, y_data, x_variable_names, x_label, y_label, title):
            self.x_data = x_data
            self.y_data = y_data
            self.x_variable_names = x_variable_names
            self.x_label = x_label
            self.y_label = y_label
            self.title = title
            self.file_location = file_location
            
        def boxplot(self):
            plt.boxplot(self.x_data)
            plt.title(self.title) #Plot the given title   
            plt.xlabel(self.x_label)#Plot the given x-axis label
            plt.ylabel(self.y_label) #Plot the given y-axis label
            plt.show()
            while True:
                save_image = input("Do you want to save the image? (Y/N): ")
                if save_image == "Y":
                    plt.boxplot(self.x_data)
                    plt.title(self.title) #Plot the given title   
                    plt.xlabel(self.x_label)#Plot the given x-axis label
                    plt.ylabel(self.y_label) #Plot the given y-axis label
                    plt.savefig('boxplot.pdf', bbox_inches='tight')
                elif save_image == "N":
                    break
                else:
                    print("Invalid input")
                    continue
                break
            
        
        def multi_boxplot(self):
            plt.boxplot(self.x_data,labels=self.x_variable_names)
            plt.rcParams["figure.figsize"] = [7.50, 3.50]
            plt.rcParams["figure.autolayout"] = True 
            plt.xlabel(self.x_label, fontsize=12)
            plt.ylabel(self.y_label, fontsize=12) 
            plt.title(self.title, fontsize=18) 
            plt.show()
            while True:
                save_image = input("Do you want to save the image? (Y/N): ")
                if save_image == "Y":
                    plt.boxplot(self.x_data,labels=self.x_variable_names)
                    plt.rcParams["figure.figsize"] = [7.50, 3.50]
                    plt.rcParams["figure.autolayout"] = True 
                    plt.xlabel(self.x_label, fontsize=12)
                    plt.ylabel(self.y_label, fontsize=12) 
                    plt.title(self.title, fontsize=18)
                    plt.savefig('multi_boxplot.pdf', bbox_inches='tight')
                elif save_image == "N":
                    break
                else:
                    print("Invalid input")
                    continue
                break
            
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
            while True:
                save_image = input("Do you want to save the image? (Y/N): ")
                if save_image == "Y":
                    fig, ax = plt.subplots(figsize = [10, 5]) #Create the figue, set the axes and figure size.
                    ax.scatter(self.x_data, self.y_data, color = 'b', marker = 'o', alpha=0.3) #Plot the scatter graph
                    plt.title(self.title) #Plot the given title
                    plt.xlabel(self.x_label)#Plot the given x-axis label
                    plt.ylabel(self.y_label) #Plot the given y-axis label
                    plt.savefig('scatter_plot.pdf', bbox_inches='tight')
                elif save_image == "N":
                    break
                else:
                    print("Invalid input")
                    continue
                break
        
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
            while True:
                save_image = input("Do you want to save the image? (Y/N): ")
                if save_image == "Y":
                    fig, ax = plt.subplots(figsize = (15,5))
                    plt.plot(self.x_data, self.y_data, alpha=0.3)
                    plt.title(self.title)
                    plt.xlabel(self.x_label)#Plot the given x-axis label
                    plt.ylabel(self.y_label) #Plot the given y-axis label
                    plt.savefig('single_line_plot.pdf', bbox_inches='tight')
                elif save_image == "N":
                    break
                else:
                    print("Invalid input")
                    continue
                break
            
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
            while True:
                save_image = input("Do you want to save the image? (Y/N): ")
                if save_image == "Y":
                    fig, ax = plt.subplots(figsize = (15,5))
                    for i in range(len(self.x_data)):
                        label = self.x_variable_names[i]
                        plt.plot(self.y_data, self.x_data[i], label=label, alpha=0.3)
                        ax.set(title=self.title) #Plot the given title
                        plt.legend()
                    plt.xlabel(self.x_label)#Plot the given x-axis label
                    plt.ylabel(self.y_label) #Plot the given y-axis label
                    plt.savefig('multi_line_plot.pdf', bbox_inches='tight')
                elif save_image == "N":
                    break
                else:
                    print("Invalid input")
                    continue
                break
            
            
        def histogram(self):
            plt.hist(self.x_data, bins=30)
            plt.xlabel(self.x_label)
            plt.ylabel('Count')
            plt.title(self.title)    
            plt.show()
            while True:
                save_image = input("Do you want to save the image? (Y/N): ")
                if save_image == "Y":
                    plt.hist(self.x_data, bins=30)
                    plt.xlabel(self.x_label)
                    plt.ylabel('Count')
                    plt.title(self.title)
                    plt.savefig('histogram_plot.pdf', bbox_inches='tight')
                elif save_image == "N":
                    break
                else:
                    print("Invalid input")
                    continue
                break
            
        def bargraph(self):
            """
            Function to produce bar graph for given input values.
            the x_variables will be plotted against the y-variable,
            x-variables are typically non-numerical variables such as area name, etc.
            the y-variable which should be a numerical variable so our bar graph
            represents bars as high or low as its count.
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
                        graph_type = input("Would you like to plot a scatter (S) or a bar chart (B)?: ")
                        if graph_type == "S":
                            title = input("Enter title for scatter plot: ")
                            View_Charts = Data_Viz(x_variable, y_variable, x_label, x_label, y_label, title)
                            View_Charts.scatter()
                            break
                        elif graph_type == "B":
                            title = input("Enter title for bar plot: ")
                            View_Charts = Data_Viz(x_variable, y_variable, x_label, x_label, y_label, title)
                            View_Charts.bargraph()
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
                            View_Charts = Data_Viz(x_variable, y_variable, x_label, x_label, y_label, title, file_location)
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


        
        
        

        
        
    
    
    