def info():

    import pandas as pd

    file_location = input("Where have you saved the data?")

    master_data = pd.read_csv(file_location)

    master_data.info
