def info(file_location):

    import pandas as pd

    master_data = pd.read_csv(f'{file_location}/Master Data.csv')
    
    info_choice = input("What information would you like to know? (N for column names) ")
    
    if info_choice == "N":
        print(master_data.columns)
           
    
