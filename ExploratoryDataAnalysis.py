#Basic Data Exploration without comparisons
# !pip install pandas-profiling if not on system
import matplotlib.pyplot as plt
import seaborn as sea
import pandas as pd

"""
This module contains the function, eda_selection(file_location), which is called 
from covid_project.py to inform the module which PATH to find and read the data 
from (master_data). This function is automatically called from covid_project 
when 'E' is input by the user from the main user interface (covid_project).

eda_selection(file_location) then calls functions from the class ExploreMasterData
to plot the histograms, boxplots and heatmap for all variables in the master_data set.

The subplots of each graph type produced for each variable are saved in one PDF
and one PNG file. 

The class ExploreMasterData can be called from any module to provide exploratory 
data analysis on any data set of interest. The layout of each set of subplots has 
been designed for use with the COVID data to be run with this program.

"""


def eda_selection(file_location):
    """eda_selection uses file_location to read the COVID data set and assigns 
    the DataFrame to variable master_data. 
    Then the variables Region Name and Local Authority are removed as they aren't
    appropriate to view in these plots. 
    The function then calls histplot_master_data(), boxplot_master_data() and
    heatmap_master_data() from the class ExploratoryDataAnalysis to provide 
    subplots for each variable in the dataset. """
    # !pip install pandas-profiling if not on system
    import matplotlib
    #matplotlib.use('TkAgg') # comment out if using Jupyter Notebook
    import matplotlib.pyplot as plt
    import seaborn as sea
    sea.set(font_scale=0.6)
    import pandas as pd
    master_data = pd.read_csv(f'{file_location}/Master Data.csv')
    #%matplotlib inline  #(comment out if not using Jupyter NB)
    master_data_copy = master_data.copy()
    master_data_copy = master_data_copy.drop(columns=['Region name', 'Local Authority'])
    View_charts2 = ExploreMasterData(master_data_copy)
    View_charts2.histplot_master_data()
    View_charts2.boxplot_master_data()
    
    View_charts = ExploreMasterData(master_data)
    View_charts.heatmap_master_data()

class ExploreMasterData:
    """ 
    Class takes input of a DataFrame for the variables of interest and produces 
    subplots of variaous graph types to provide the user with an overview of 
    the distributions of each of the variables.
    """
    def __init__(self, x):
        self.x = x

    def histplot_master_data(self):
        """" Produces histograms for each of the variables in the dataset self.x 
        as subplots and saves the output as png and pdf."""
        for all, column in enumerate(self.x.columns):
            plt.subplot(5, 4, all + 1)
            sea.histplot(data=self.x[column], palette='husl')
            plt.xticks(rotation=30,fontsize=5)
            plt.yticks(rotation=30,fontsize=5)
            plt.title(column)
            plt.xlabel(None)
            plt.ylabel('Count',fontsize=6)
            plt.tick_params(axis='both', which='both',length=0.1, pad=2)
            plt.margins(0.2)
        plt.subplots_adjust(left=0.125,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.8, 
                    hspace=0.9)
        plt.suptitle('Histograms of all variables', fontsize=12)
        plt.savefig('Histograms of all variables.png', format='png', dpi=800)
        plt.savefig('Histograms of all variables.pdf')
        plt.tight_layout()
        plt.show()

    def lineplot_master_data(self):
        """" Produces lineplots for each of the variables in the dataset self.x 
        as subplots and saves the output as png and pdf."""
        for all, column in enumerate(self.x.columns):
            plt.subplot(4, 6, all + 1)
            sea.lineplot(data=self.x[column])
            plt.xticks(rotation=30,fontsize=5)
            plt.yticks(rotation=30,fontsize=5)
            plt.title(column)
            plt.xlabel(None)
            plt.ylabel('Count',fontsize=6)
            plt.tick_params(axis='both', which='both',length=0.1, pad=2)
            plt.margins(0.2)
        plt.subplots_adjust(left=0.125,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.8, 
                    hspace=0.9)

        plt.savefig('Lineplots of all variables.png', format='png', dpi=800)
        plt.savefig('Lineplots of all variables.pdf')
        plt.tight_layout()
        plt.show()

    def scatterplot_master_data(self):
        """" Produces scatterplots for each of the variables in the dataset self.x 
        as subplots and saves the output as png and pdf."""
        for all, column in enumerate(self.x.columns):
            plt.subplot(4, 6, all + 1)
            sea.scatterplot(data=self.x[column])
            plt.xticks(rotation=30,fontsize=5)
            plt.yticks(rotation=30,fontsize=5)
            plt.title(column)
            plt.xlabel(None)
            plt.ylabel('Count',fontsize=6)
            plt.tick_params(axis='both', which='both',length=0.1, pad=2)
            plt.margins(0.2)
        plt.subplots_adjust(left=0.125,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.8, 
                    hspace=0.9)

        plt.savefig('Scatterplots of all variables.png', format='png', dpi=800)
        plt.savefig('Scatterplots of all variables.pdf')
        plt.tight_layout()
        plt.show()

    def heatmap_master_data(self):
        """" Produces a heatmap showing correlation between each of the variables 
        in the dataset self.x and saves the output as png and pdf."""
        correlation = self.x.corr()
        fig, ax = plt.subplots(figsize=(10, 10))
        sea.heatmap(data=correlation, annot=False, cmap="seismic", center=0, linewidths=0.9)
        plt.xlabel(None)
        plt.tick_params(axis='both', which='both',length=0.1, pad=2, labelsize=7)
        plt.margins(0.2)
        plt.title('Correlation matrix of all variables', fontsize=25)
        plt.savefig('Correlations.png', format='png', dpi=800)
        plt.savefig('Correlations.pdf')
        plt.show()

    def boxplot_master_data(self):
        """" Produces boxplotss for each of the variables in the dataset self.x 
        as subplots and saves the output as png and pdf."""
        for all, column in enumerate(self.x.columns):
            plt.subplot(5, 4, all + 1)
            plt.xticks(rotation=30, fontsize=5)
            plt.yticks(rotation=30,fontsize=5)
            box_plt = sea.boxplot(data=self.x[column], linewidth = 0.8, width = 0.6, showfliers = False)
            plt.title(column)
            plt.xlabel(None)
            plt.tick_params(axis='both', which='both',length=0.1, pad=2)
            plt.margins(0.2)
            box_plt.set(xticks = [])
        plt.subplots_adjust(left=0.125,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.6, 
                    hspace=0.6)
        plt.suptitle('Boxplots of all variables', fontsize=12)
        plt.savefig('Boxplot of all variables.png', dpi=800)
        plt.savefig('Boxplots of all variables.pdf')
        plt.tight_layout()
        plt.show()

    




