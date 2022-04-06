#!/usr/bin/env python

def regression(file_location):
    
    import matplotlib.pyplot as plt
    import pandas as pd
    
    master_data = pd.read_csv(f'{file_location}/Master Data.csv')

    def linear():
        Y_var = input('Which Y variable do you want to predict (enter exact from Parameter names): ')
        Y = master_data[Y_var]
    
        master_data_copy = master_data.copy()
        X = master_data_copy.drop(columns=[Y_var, 'Local Authority Name', 'Region name'])
        
        from sklearn.model_selection import train_test_split
    
        size_test = input("What test size do you want? ")
    
        state_random = input("What random state do you want? ")
    
        Xtr, Xtest, Ytr, Ytest = train_test_split(X, Y, test_size = float(size_test), random_state = int(state_random))
        
        from sklearn.metrics import mean_squared_error, r2_score
        from sklearn import linear_model
    
        regr = linear_model.LinearRegression()
        regr.fit(Xtr, Ytr)
    
        print(f'Coefficent is {regr.coef_}')
    
        print(f'Intercept is {regr.intercept_}')
        
        ypred_test = regr.predict(Xtest)
        print(f'Testing MSE is {mean_squared_error(ypred_test, Ytest)}')
        print(f'Testing R2 score is {r2_score(ypred_test, Ytest)}')
        
        ypred_train = regr.predict(Xtr)
        print(f'Training MSE is {mean_squared_error(ypred_train, Ytr)}')
        print(f'Training R2 score is {r2_score(ypred_train, Ytr)}')
        
        plt.scatter(ypred_test, Ytest,color='black')
        plt.show()
        
    regression_type = input("Do you want to use a linear regression model (L)? ")
    if regression_type == "L":
        linear()
            
    
    

    
