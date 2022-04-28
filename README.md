# EMAT10006COURSE (Daniel Joinson, Kate E, Tim A. , Adetutu S. )
This repository contains all the code we created for our program, including a video of our simulation.

**HOW TO RUN THE PROGRAM FROM YOUR TERMINAL**

    *Before running the program, download the folder containing the seperate CSV files to be combined and cleaned to create master data. Provided in the repository.

    *Clone the github repository:* 
git clone https://github.com/TheRealSheBoss/EMAT10006COURSE.git 


    *Enter the following into the terminal to run the program:*  
python ./covid_project.py 

 
    *Install relevant libraries using pip install* 
    *Installation and use of virtual is only neccessary for Mac users*
    
pip install virtualenv 


virtualenv venv 


source venv/bin/activate 


pip install pandas 


pip install matplotlib 


pip install numpy


pip install seaborn


pip install sklearn

 **DATA GENERATION**
 ===================
 **User input from covid_project.py: PATH of csv files'**
The data is pre-processed, cleaned and stored in the users desired path.
    *Generating Masterdata*
Once the program asks where have you saved the non-master data?, input the PATH for the folder in which the CSV files are contained into the command line of the console. 
For example, '/Users/adetutusadiq/Downloads'. 
data_generation.py will then automatically run. This module reads each of the csv files saved in the PATH given. Note, each file must be saved under the specific names and with the same number and names of parameter as the files provided here. The data_generation.py then reads the csv files and combines them into a master csv file. During this process, parameters are renamed, repeated columns are dropped, parameters with numerical data as string data type are converted to float, duplicates are dropped and rows with null values are dropped. The decision to drop null values was based on analysis of the data we obtained and provide for use in this program. The null values are sufficiently small for this action to be appropriate. data_generation.py then saves the processed 'Master Data'.csv file to the same PATH as given by the user.

 
    *Program functionality/tasks you can ask it to do:*  
The program will then give you the following options: 
Type G for graph function, I for variable information, R for machine learning regression modelling, E for eda(Exploratory Data Analysis), S for Simulation, or type stop to quit the program.
Note that this instruction is case sensitive. A while loop would run until the correct options are inputed.

**INFORMATION ON THE DATA SET**
===============================
**User input: 'I'**
Summary: 
1. Runs on output of data_generation.py 'Master Data'.csv
2. Returns information to the user in the console on variable names 
3. Returns information to the user in the console on the first 5 observations of a given variable
4. Returns information to the user in the console on the last 5 observations of a given variable
5. Returns information to the user in the console on the mean of a given variable

Detailed user instructon:

We recommend the user commences the program with this function. The user should input 'I' in the terminal when first running the program as this enables the user to gain an understanding of the variables in the data set and some initial descriptive statistics of the data. 

Inputting I runs the function info() from the module info.py. The user is then asked whether they want information on the variable names (user inputs 'N'), the first 5 observations of a particular variable (user in puts 'H', then the name of the variable of interest), the last 5 observations of a particular variable (user in puts 'T', then the name of the variable of interest), the mean of a variable of interest (user inputs 'M', then the name of the variable of interest). 

We recomment the user looks at the names of the variables before moving back to the main module, this way exact variable names can easily be copied into the command line of the terminal throughout the rest of the program. 
Once each command has been carried out, the user is asked whether they want to remain in info and input another command (user input: 'Y') or return to covid_project.py (user input: 'N').

**EXPLORATORY DATA ANALYSIS**
============================
**User input from covid_project.py: 'E'**
Summary:
1. Runs on output of data_generation.py 'Master Data'.csv
2. There are six potential functions, each would independently generate a graph or chart when called
3. A data profile of the dataset could be generated: (a profile is a set of statistics that describe how often and how long parts of a program are executed)
4. There are no comparisons contained in this class.

Detailed user instruction: 

We recommend the user performs exploratory data analysis after info, by inputting 'E' in the terminal command line. This calls the eda_selection() function from ExploratoryDataAnalysis.py and automatically displays and saves histograms of all variables, boxplots of all variables and a correlation matrix of all variables. 

The pdf and png files will be saved to the same PATH the programm is being run from. The histograms and boxplots are not meant for use in a formal report or paper and are intended to give the user an indication of the distribution of each variable. Once the graphs have been displayed and saved to PDF, the user is returned to the covid_project.py interface.

**GRAPHS**
==========
**User input from covid_project.py: 'G'**
Summary:
1. Allows user to input varibales of interest 
4. Returns predefined plots dependent on the variebles input by the user.

Detailed user instruction:

The user is then recommended to investigate indiviual or groups of varibles after running info and exploratory data analysis. 

Once the user inputs 'G' from covid_project.py, the graph_selction function is run from the module graphs.py. The user is then asked how many X variables they want to visualise, the user should input the appropriate integer in the terminal command line. Based on the integer entered by the user, the user is then asked to input the exact name of the variable in the 'Master Data'.csv and input their own preferred label name for the X variables of interest, again input via the terminal command line. (Note, the program will only accept X variables of the exact name saved in the csv file; use info.py by inputting 'I' from the main interface to get the exact variable names). The user is then asked whether they want to investigate a Y-variable (user input: 'Y' or 'N'). If 'Y' the user is asked to input the name of the variable of interest and input their preferred label for the variable. Depending on the number of X- and Y- variables being investigated, graph_selection() will either request the user select between one of two graph plotting options by inputting the first letter of the type of plot into the terminal command line, or if only one plotting option is available graph_selection will continue with that plot. A summary of the graph options available is presented below: 

*1 X-variable, no Y-variable: histogram or boxplot*
*1 X-variable, 1 Y-variable: scatter plot or barchart*
*>1 X-variables, no Y-variable: boxplot*
*>1 X-variables, 1 Y-variable: line plot*
   
The selected graph is then displayed as a GUI to the user. Once the user closes the GUI, the program then asks whether the user wishes to save the plot as a PDF and PNG (user input: 'Y'/'N'). If 'Y' the plot is saved as a PDF to the same PATH the program is being run from. Then the user is returned to the main interface (covid_project.py). If 'N' the user is redirected to the main interface. 

**REGRESSION MODELS**
==========
**User input: 'R'**
Summary: 
1. User selects response variable of interest 
2. The X and Y data is then split into training and test sets 
3. Linear regression: returns the training and test mean squared error and R squared scores in the console. Displays and saves a scatter plot of the predicted test vs. true response values. 
4. Polynomial regression: returns plot of the training and validation mean squared error scores across X degrees.
5. Decision tree regression: returns the training and test mean squared error and R squared scores in the console. Displays and saves a table of the MSE and R2 scores. 
6. Comapre all models: returns a multi-variable boxplot of the cross validation scores across each of the three regression models. Returns the MSE and R squared scores in the console. 

Detailed user instruction:

Having investigated the variables of interest, the user is then recommended to investigate the regression models by entering 'R' from the main interface (covid_project.py). 

The user should input which variable they wish to investigate as the response variable. This should be the exact parameter name listed in the master data set and the program will request you input the variable name again if the input name does not match one in the data set. 

The user should then input the test size they wish to retain from the X and Y data to test the trained model on (recommended to be 0.2). 

The user should then input the random state they wish to use to split the training and test data (recommended 0).

The program automatically splits the resulting X and Y data into training and test sets with the test size and random state specified by the user. 

The user should then input which regression model they wish to run; linear regression model (user input: 'L'), Polynomial regression (user input: 'P'), Decision Tree Regression (user input: 'D'), compare all (user input: 'C') or return to the main interface (user input: 'main').

If 'L', Linear regression, the program returns the training and test mean squared error and R squared scores in the console. Displays and saves a scatter plot of the predicted test vs. true response values. 

If 'P', Polynomial regression, the program returns plot of the training and validation mean squared error scores across X degrees.

If 'D', Decision tree regression, the program returns the training and test mean squared error and R squared scores in the console. Displays and saves a table of the MSE and R2 scores. 

If 'C', Comapre all models, the program returns a multi-variable boxplot of the cross validation scores across each of the three regression models. Returns the MSE and R squared scores in the console. 

The user can then select whether to remain in regression models (user input: 'Y') to investigate a different model or to return to the main console page ('N') to choose another function in the program. 


**SIMULATION: THE PROGRESSIVE ACCEPTANCE OF VACCINATIONS DURING THE COVID-19 CRISES IN THE UK:**
================================================================================================
**User input: 'S'**
*The simulation code is contained in simulation.py*
The codes for the simulation have been tested using PyCharm and the video was downloaded(SIMULATION.mp4). 
Ensure you have the required encoder to view and download the created simulation.
The ffmpeg encoder is one of the most popular. Else, please run the code on PyCharm so as to get the exact same results that we did.
1. A class containing several reusable functions was created
2. Population was set to 10,000 and it could be extrapolated to fit a larger population (The population density in the raw dataset was extremely heavy and led to RunTime errors and poor indexing, hence the choice for an arbitrary figure)
3. Parameters representing infected persons, as well as the first, second and third dose of the vaccine were set
4. The first_wave() function is responsible for depicting how the infections spread through iterations, after it had been initialized to zero. It initializes our plot with the set population of 10,000. 
The **GOLDEN SPIRAL METHOD** discussed on stackoverflow: https://stackoverflow.com/questions/9600801/evenly-distributing-n-points-on-a-sphere was the principle behind the sections witnessed in the polar plot. 
It generates a 2D-spiral algorithm.
6. The Vaccine_share() function would calculate the number of newly infected people while vaccinations are out, a serial interval of 7days was used, however, this value can be changed/adjusted. 
7. The Doses() function calculates the doses given during each wave of the infection.
8. The updates() function would update the color of plot points when infections occur, whether or not they have been vaccinated
9. The update_annotation() function would make changes to the annotations created at the beginning on the polar plot, so that each data would change and reflect on the plot. Formatted strings were used to make changes.
10.The animate() function would show the plot while the program is running.
11.The generator function acts as short cut to build iterations as frames for the plot. It is totally dependent on the number of vaccinated persons being less than infectious persons.
12.The class was assigned to a variabe covid, after the COVID_19 parameter had been passed, the animate function was called. And the simulation appeared









