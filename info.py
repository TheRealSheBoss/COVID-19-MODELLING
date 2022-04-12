def info(file_location):

    import pandas as pd

    from variable_finder import Variable_Finder

    master_data = pd.read_csv(f'{file_location}/Master Data.csv')
    
   
    while True:
        
        info_choice = input("What information would you like to know? (N for column names, H for head of a variable, T for tail of a variable, M for mean of variable) ")
        
        if info_choice == "N":
            print(master_data.columns)
            break
        
        if info_choice == "H":
        	var_choice = Variable_Finder("", master_data)          
        	X = var_choice.variable_finder()    
        	print(X.head())
        	break
        
        if info_choice == "T":
            var_choice = Variable_Finder("", master_data)          
            X = var_choice.variable_finder()    
            print(X.tail()) 
            break
        
        if info_choice == "M":
            var_choice = Variable_Finder("", master_data)         
            X = var_choice.variable_finder()    
            print(X.mean()) 
            break
        
        else:
            print("Invalid input")
            continue
            
        
        
        
        