

def info(file_location):

    import pandas as pd

    from variable_finder import Variable_Finder

    master_data = pd.read_csv(f'{file_location}/Master Data.csv')
    
    """
    In this program, a while loop is used to provide an interface for the user to input what info about the data they want to know.
    The user can find out the column names of the dataset, and the head, tail and mean of variables. The variable_finder class is used
    to determine whether the variable names the user inputted are within the dataset. 
    """
    
    while True:
        
        info_choice = input("What information would you like to know? (N for column names, H for head of a variable, T for tail of a variable, M for mean of variable, main to go back to main.py) ")
        
        if info_choice == "N":
            print(master_data.columns)
            info_stay = input("Do you want to stay in info? (Y or N) ")
            if info_stay == "Y":
                continue
            elif info_stay == "N":
                break
            else:
                print("Invalid input")
                continue
            
        if info_choice == "H":
            var_choice = Variable_Finder("", master_data)          
            X = var_choice.variable_finder()    
            print(X.head())
            info_stay = input("Do you want to stay in info? (Y or N) ")
            if info_stay == "Y":
                continue
            elif info_stay == "N":
                break
            else:
                print("Invalid input")
                continue
        
        if info_choice == "T":
            var_choice = Variable_Finder("", master_data)          
            X = var_choice.variable_finder()    
            print(X.tail()) 
            info_stay = input("Do you want to stay in info? (Y or N) ")
            if info_stay == "Y":
                continue
            elif info_stay == "N":
                break
            else:
                print("Invalid input")
                continue
        
        if info_choice == "M":
            var_choice = Variable_Finder("", master_data)         
            X = var_choice.variable_finder()   
            if X.dtype != float:
                print("Invalid input - please choose a numeric variable")
                break
            print(X.mean())
            info_stay = input("Do you want to stay in info? (Y or N) ")
            if info_stay == "Y":
                continue
            elif info_stay == "N":
                break
            else:
                print("Invalid input")
                continue
        
        if info_choice == "main":
            break
                
        else:
            print("Invalid input")
            continue
            
        
        
        
        
