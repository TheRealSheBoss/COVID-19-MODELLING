#!/usr/bin/env python

'''

AI REGRESSION MODELLING: 

Our dataset contains numeric variables relevant to the Covid pandemic across all regions in the UK. 
This data includes information about deaths, population vaccinated 1st, 2nd and 3rd doses, and many more data points.
Our team decided to apply AI/Machine Learnining regression algorithms to give us an understanding of the data. 

Thus, in this code, we have a main function called regresssion(). To split our data into test and training data, we use the traintestsplit function. 
Depending on the type of regression algorithms the user wants to fit to the data, we created subfunctions for Linear Regression, Polynomial Regression, and Decision Tree Regression.
Lastly, we have a function to compare all these models to see which ones performed best. 

PERFORMANCE METRICS: 

The performance metrics used are the Mean Squared Error(MSE) and R-squared. 
A model with a lower MSE is a better performning data and the closer R-squared value is to 1, the better the model's fit to the data. 
Hence, better performing. However, to prevent our model from over-fitting to the data and ensure model generalizability to new unseen data, we 
had to optimize for parameters, especially in our polynomial model. 

A polynomial degree value more than 5 is likely to produce overfitting or crash the program, so in order to prevent this, we introduced a While loop to 
operate the code only if the conditional that poly_degree_test has to be less than or equal to 5 is met. 


THIS SCRIPT CAN BE USED TO: 

    1. Fit 3 AI regression models imported from the scikit-learn library to the data. 
    2. Evaluate each model's performance(fit to data) using metrics such as Mean Squared Error(MSE) and R-squared. Produce line graphs, scatters plots and box plots
    that give us a visual representation of performance of each model.
    3. Use the CompareAllModels function to compare the performance of each model to each other using box plot files as the visualization method.
    
TO RUN THIS SPECIFIC SCRIPT, 
    1. clone the github repository : https://github.com/TheRealSheBoss/EMAT10006COURSE.git 
    2. run ./main,py from your terminal
    3. Install libraries and environments listed in ReadMe file, Generate Masterdata. 
    4. Enter A, for AI modelling, follow prompts for specific models you wish to run or to compare all models. 


'''

def regression(file_location):
    
    
    import matplotlib.pyplot as plt
    import pandas as pd
    from sklearn.metrics import mean_squared_error, r2_score  #from sklearn.metrics import mean_squared_error, r2_score
    from sklearn import linear_model  #from sklearn import linear_model
    from sklearn.preprocessing import PolynomialFeatures
    from sklearn.model_selection import KFold
    from sklearn.tree import DecisionTreeRegressor
    from scipy.stats import ttest_rel
    from sklearn.model_selection import train_test_split
    import numpy as np
    import variable_finder as VF
    import graphs as Gph
    
    master_data = pd.read_csv(f'{file_location}/Master Data.csv')

    def traintestsplit(X_data, Y_data):
    
        size_test = input("What test size do you want? ")
    
        state_random = input("What random state do you want? ")
        
        Xtr, Xtest, Ytr, Ytest = train_test_split(X_data, Y_data, test_size = float(size_test), random_state = int(state_random))
        
        return Xtr, Xtest, Ytr, Ytest 
    
        #from sklearn.model_selection import train_testT_split
        #size_test = input("What test size do you want? ")
        #state_random = input("What random state do you want? ")
        #Xtr, Xtest, Ytr, Ytest = train_test_split(X, Y, test_size = float(size_test), random_state = int(state_random))

        
    def linear(Xtr, Xtest, Ytr, Ytest):
        regr = linear_model.LinearRegression()
        regr_model = regr.fit(Xtr, Ytr)
    
        print(f'Coefficent is {regr.coef_}')
    
        print(f'Intercept is {regr.intercept_}')
        
        ypred_test = regr_model.predict(Xtest)
        print(f'Testing MSE is {mean_squared_error(ypred_test, Ytest)}')
        print(f'Testing R2 score is {r2_score(ypred_test, Ytest)}')
        
        ypred_train = regr_model.predict(Xtr)
        print(f'Training MSE is {mean_squared_error(ypred_train, Ytr)}')
        print(f'Training R2 score is {r2_score(ypred_train, Ytr)}')
        
        plt.scatter(ypred_test, Ytest,color='black')
        plt.show()
        

    def Polynomial(Xtr, Xtest, Ytr, Ytest): 
        
        
        poly_degree_test = int(input("Please enter an integer as the maximum number of polynomial degree values you wish to test in this model : "))
        
        MSE_test_data = []
        MSE_train_data = []
        
        for i in range(poly_degree_test):
            poly = PolynomialFeatures(degree=i+1)
            
            Xtr_new = poly.fit_transform(Xtr)
            Xtest_new = poly.fit_transform(Xtest)
            
            regr = linear_model.LinearRegression()
            regr.fit(Xtr_new, Ytr) #fit transformed data and target to regression model 
            
            pred_tr = regr.predict(Xtr_new) #performing predictions on transformed data 
            pred_tst = regr.predict(Xtest_new)
            
            MSE_train_data.append(mean_squared_error(Ytr, pred_tr))
            MSE_test_data.append(mean_squared_error(Ytest, pred_tst))
        
        plt.plot(range(1, poly_degree_test+1), MSE_train_data, label='Training Data')
        plt.plot(range(1, poly_degree_test+1), MSE_test_data, label='Test Data')
        plt.ylabel('MSE')
        plt.xlabel('Degree')
        plt.legend()
        plt.show()

# =============================================================================
#         AllXVars = np.vstack((MSE_train_data, MSE_test_data))
#         print(len(AllXVars))
#         y_var = list(range(1, poly_degree_test+1))
#         labels = ['Training', 'Validation']
#         xlabel = 'Degree'
#         ylabel = 'MSE'
#         title = 'Parameter optimisation and cross validation for Polynomial Regression'
#         Plots = Gph.Data_Viz(AllXVars, y_var, labels, xlabel, ylabel, title)
#         Plots.multi_line()
# =============================================================================

        
        print('1. The ideal polynomial degree for this model is the point where our MSE is lowest for both training') 
        print('and test data. Please identify it.')
        
        print('                                                                                                     ')
        
        print('2. Compare the MSE of the ideal polynomial order here with the testing MSE you get when predicting the same') 
        print('variable with Linear Regression. Which MSE is lower, that is the better model for that specific prediction')
        
        
    
    def DecisionTree(Xtr, Xtest, Ytr, Ytest):
        DTR = DecisionTreeRegressor()
        DTR_model = DTR.fit(Xtr, Ytr)
        ypred_train = DTR_model.predict(Xtr)
        print(f'Training MSE is {mean_squared_error(ypred_train, Ytr)}')
        print(f'Training R2 score is {r2_score(ypred_train, Ytr)}')
        
        ypred_test = DTR_model.predict(Xtest)
        print(f'Testing MSE is {mean_squared_error(ypred_test, Ytest)}')
        print(f'Testing R2 score is {r2_score(ypred_test, Ytest)}')
    
    
    def CompareAllModels(Xtr, Xtest, Ytr, Ytest):
        mse_LR = []
        r2_LR = []
        mse_DTR = []
        r2_DTR = []
        mse_poly = []
        r2_poly = []
        
        regr = linear_model.LinearRegression()
        DTR = DecisionTreeRegressor()
        poly = PolynomialFeatures()
        cv = KFold(n_splits=10, shuffle=True)
        for train_index, test_index in cv.split(Xtr):
            Xtrain, Xtst = Xtr[train_index], Xtr[test_index]
            Ytrain, Ytst = Ytr[train_index], Ytr[test_index]
            
            model_LR = regr.fit(Xtrain, Ytrain)
            LR_pred = model_LR.predict(Xtst)
            mse_LR.append(mean_squared_error(Ytst, LR_pred))
            r2_LR.append(r2_score(Ytst, LR_pred))
            
            model_DTR = DTR.fit(Xtrain, Ytrain)
            DTR_pred = model_DTR.predict(Xtst)
            mse_DTR.append(mean_squared_error(Ytst, DTR_pred))
            r2_DTR.append(r2_score(Ytst, DTR_pred))
            
            Xtrain_new = poly.fit_transform(Xtrain)
            Xtst_new = poly.fit_transform(Xtst)
            model_poly = regr.fit(Xtrain_new, Ytrain) #fit transformed data and target to regression model 
            poly_pred = model_poly.predict(Xtst_new)
            mse_poly.append(mean_squared_error(Ytst, poly_pred))
            r2_poly.append(r2_score(Ytst, poly_pred))
        
# =============================================================================
#         box_plot_data=[mse_LR,mse_DTR, mse_poly]
#         plt.boxplot(box_plot_data,labels=['Linear \nRegression', 'Decision Tree \nRegression', 'Polynomial \nRegression'])
#         plt.rcParams["figure.figsize"] = [7.50, 3.50]
#         plt.rcParams["figure.autolayout"] = True
#         plt.title('Comparison of AI model performances', fontsize=18) #Plot the given title   
#         plt.xlabel('AI models', fontsize=14)#Plot the given x-axis label
#         plt.ylabel('Mean Squared Error', fontsize=14) #Plot the given y-axis label
#         plt.show()
# =============================================================================
        AllMSE = []
        AllMSE.append(mse_LR)
        AllMSE.append(mse_DTR)
        AllMSE.append(mse_poly)
        labels = ['Linear \nRegression', 'Decision Tree \nRegression', 'Polynomial \nRegression']
        xlabel = 'AI models'
        ylabel = 'Mean Squared Error'
        title = 'Comparison of AI model performances'
        Plots = Gph.Data_Viz(AllMSE, None, labels, xlabel, ylabel, title)
        Plots.multi_boxplot()
        #Data_Visualisation.multi_boxplot(AllMSE)
        #Boxplot = Histo_Boxplot.boxplot()
        #Boxplot([mse_LR, mse_DTR])

        
        print(f'LR mse: mean={np.mean(mse_LR)}, sd={np.std(mse_LR)}')
        print(f'LR r2: mean={np.mean(r2_LR)}, sd={np.std(r2_LR)}')
        print(f'DTR mse: mean={np.mean(mse_DTR)}, sd={np.std(mse_DTR)}')
        print(f'DTR r2: mean={np.mean(r2_DTR)}, sd={np.std(r2_DTR)}') 
        print(f'LR vs. DTR: {ttest_rel(mse_LR,mse_DTR)}')
    
    def SelectTargetVariable():
        var_choice = VF.Variable_Finder("", master_data)
        Y_var = var_choice.variable_finder()
        master_data_copy = master_data.copy()
        X = master_data_copy.drop(columns=[Y_var.name, 'Local Authority Name', 'Region name'])
        return X, Y_var    
    

    Parameters, Target = SelectTargetVariable()
    
    Xtraining, Xtesting, Ytraining, Ytesting = traintestsplit(Parameters, Target)
    Xtraining = Xtraining.to_numpy()
    Xtesting = Xtesting.to_numpy()
    Ytraining = Ytraining.to_numpy()
    Ytesting = Ytesting.to_numpy()
    
    
    
    regression_type = input("Do you want to use a linear regression model (L), Polynomial regression (P), Decision Tree Regression (D) or compare all (C)? ")
    if regression_type == "L":
        linear(Xtraining, Xtesting, Ytraining, Ytesting)
    elif regression_type == "P":
         Polynomial(Xtraining, Xtesting, Ytraining, Ytesting)
    elif regression_type == "D":
        DecisionTree(Xtraining, Xtesting, Ytraining, Ytesting)
    elif regression_type == "C":
        CompareAllModels(Xtraining, Xtesting, Ytraining, Ytesting)
    
    
