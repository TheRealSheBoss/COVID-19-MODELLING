#!/usr/bin/env python

def regression(file_location):
    
    import matplotlib.pyplot as plt
    import pandas as pd
    from sklearn.metrics import mean_squared_error, r2_score
    from sklearn import linear_model
    from sklearn.preprocessing import PolynomialFeatures
    
    master_data = pd.read_csv(f'{file_location}/Master Data.csv')
    regr = linear_model.LinearRegression()

    def traintestsplit(X_data, Y_data):
        from sklearn.model_selection import train_test_split
    
        size_test = input("What test size do you want? ")
    
        state_random = input("What random state do you want? ")
        
        Xtr, Xtest, Ytr, Ytest = train_test_split(X_data, Y_data, test_size = float(size_test), random_state = int(state_random))
        
        return Xtr, Xtest, Ytr, Ytest 
    
        #from sklearn.model_selection import train_testT_split
        #size_test = input("What test size do you want? ")
        #state_random = input("What random state do you want? ")
        #Xtr, Xtest, Ytr, Ytest = train_test_split(X, Y, test_size = float(size_test), random_state = int(state_random))

    def linear():
        Y_var = input('Which Y variable do you want to predict (enter exact from Parameter names): ')
        Y = master_data[Y_var]
    
        master_data_copy = master_data.copy()
        X = master_data_copy.drop(columns=[Y_var, 'Local Authority Name', 'Region name'])
        
        
        split_data = traintestsplit(X, Y)
        
        Xtr = split_data[0]
        Xtest = split_data[1]
        Ytr = split_data[2]
        Ytest = split_data[3]
        
        #from sklearn.metrics import mean_squared_error, r2_score
        #from sklearn import linear_model
    
        
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
        
    def Polynomial(): #cross validation happening inside this function too
        Y_var = input('Which Y variable do you want to predict (enter exact from Parameter names): ')
        Y = master_data[Y_var]
    
        master_data_copy = master_data.copy()
        X = master_data_copy.drop(columns=[Y_var, 'Local Authority Name', 'Region name'])
        
        split_data = traintestsplit(X, Y)
        
        Xtr = split_data[0]
        Xtest = split_data[1]
        Ytr = split_data[2]
        Ytest = split_data[3]
        
        poly_degree_test = int(input("Please enter an integer as the maximum number of polynomial degree values you wish to test. In this model, we will perform a cross-validation to see which polynomial degree has the best MSE: "))
        
        MSE_test_data = []
        MSE_train_data = []
        
        for i in range(poly_degree_test):
            poly = PolynomialFeatures(degree=i+1)
            
            Xtr_new = poly.fit_transform(Xtr)
            Xtest_new = poly.fit_transform(Xtest)
            
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
        
        print('1. The ideal polynomial degree for this model is the point where our MSE is lowest for both training') 
        print('and test data. Please identify it.')
        
        print('                                                                                                     ')
        
        print('2. Compare the MSE of the ideal polynomial order here with the testing MSE you get when predicting the same') 
        print('variable with Linear Regression. Which MSE is lower, that is the better model for that specific prediction')
        
        
        
        
    regression_type = input("Do you want to use a linear regression model (L) or Polynomial Regression(P)? ")
    if regression_type == "L":
        linear()
    elif regression_type == "P":
        Polynomial()
        
    
    

    
