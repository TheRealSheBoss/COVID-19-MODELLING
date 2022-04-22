#!/usr/bin/env python3
## This script cleans the data files we provide to users of the code, and generates a master dataset that
## analysis can be performed on. This dataset is then downloaded as an excel file. 


## ADDING RELEVANT PACKAGES

def data_generation(file_location):

  import pandas as pd

  ## ADDING COVID-19 CASE DATA

  while True:
    try:
        case_data = pd.read_csv(f'{file_location}/Cumulative Cases.csv')
        break
    except FileNotFoundError:
        print("File not find, try again")
        file_location = input("Where have you saved the non-master data?")

  ## ADDING COVID-19 DEATH AND VACCINATION DATA

  while True:
    try:
        vax_death_data = pd.read_csv(f'{file_location}/Vaccination and Death.csv')
        break
    except FileNotFoundError:
        print("File not find, try again")
        file_location = input("Where have you saved the non-master data?")

  ## MERGING CASE, DEATH AND VACCINATION DATAFRAMES TOGETHER

  master_data = case_data.merge(vax_death_data, left_on='areaName', right_on='areaName')

  ## ADDING AND MERGING AGE AND DENSITY DATA

  while True:
    try:
        demo_data = pd.read_csv(f'{file_location}/Age and Density.csv')
        break
    except FileNotFoundError:
        print("File not find, try again")
        file_location = input("Where have you saved the non-master data?")

  master_data = master_data.merge(demo_data, left_on='areaCode_x', right_on='Area code')

  ## ADDING AND MERGING ETHNICITY DATA

  while True:
    try:
        eth_data = pd.read_csv(f'{file_location}/Ethnicity.csv')
        break
    except FileNotFoundError:
        print("File not find, try again")
        file_location = input("Where have you saved the non-master data?")	

  master_data = master_data.merge(eth_data, left_on='areaCode_x', right_on='Area code')

  ## ADDING AND MERGING KEY WORKER DATA

  while True:
    try:
        key_data = pd.read_csv(f'{file_location}/Key Worker.csv')
        break
    except FileNotFoundError:
        print("File not find, try again")	
        file_location = input("Where have you saved the non-master data?")

  master_data = master_data.merge(key_data, left_on='areaCode_x', right_on='Area code')

  ## ADDING AND MERGING EMPLOYMENT DATA
  
  while True:
    try:
        employ_data = pd.read_csv(f'{file_location}/Employment.csv')
        break
    except FileNotFoundError:
        print("File not find, try again")
        file_location = input("Where have you saved the non-master data?")	

  master_data = master_data.merge(employ_data, left_on='areaCode_x', right_on='Area code')

  ## ADDING AND MERGING CHILD DATA

  while True:
    try:
        child_data = pd.read_csv(f'{file_location}/Children.csv')
        break
    except FileNotFoundError:
        print("File not find, try again")
        file_location = input("Where have you saved the non-master data?")

  master_data = master_data.merge(child_data, left_on='areaCode_x', right_on='Area code')

  ## ADDING AND MERGING DEPRIVATION DATA

  while True:
    try:
        depri_data = pd.read_csv(f'{file_location}/Deprivation.csv')
        break
    except FileNotFoundError:
        print("File not find, try again")
        file_location = input("Where have you saved the non-master data?")


  master_data = master_data.merge(depri_data, left_on='areaCode_x', right_on='Area Code')


  ## DROPPING REPEATED COLUMNS

  master_data.drop('areaType_x', axis=1, inplace=True) 

  master_data.drop('areaType_y', axis=1, inplace=True) 

  master_data.drop('areaCode_y', axis=1, inplace=True) 

  master_data.drop('Area name ', axis=1, inplace=True) 

  master_data.drop('Region code', axis=1, inplace=True) 

  master_data.drop('Area code', axis=1, inplace=True) 

  master_data.drop('Region Name', axis=1, inplace=True) 

  master_data.drop('Area Code', axis=1, inplace=True) 

  master_data.drop('Area Name ', axis=1, inplace=True)

  master_data.drop('Area code_x', axis=1, inplace=True) 

  master_data.drop('Region code_y', axis=1, inplace=True) 

  master_data.drop('Area code_y', axis=1, inplace=True) 

  master_data.drop('Area name _y', axis=1, inplace=True)

  master_data.drop('Area name _x', axis=1, inplace=True)

  master_data.drop('Region name_y', axis=1, inplace=True)

  master_data.drop('Region name_x', axis=1, inplace=True)

  master_data.drop('date_x', axis=1, inplace=True)

  master_data.drop('date_y', axis=1, inplace=True)

  master_data.drop('areaCode_x', axis=1, inplace = True)

  master_data.drop('Region code_x', axis=1, inplace = True)

  ## RENAMING VARIABLES

  master_data = master_data.rename(columns={"areaName": "Local Authority", "cumCasesByPublishDate": "Cumulative Cases", "Average Score ":"Deprivation Score", "cumPeopleVaccinatedFirstDoseByPublishDate":"First dose (cum.)", "cumPeopleVaccinatedSecondDoseByPublishDate":"Second dose (cum.)", "cumPeopleVaccinatedThirdInjectionByPublishDate":"Third dose (cum.)", "cumDeaths28DaysByPublishDate":"Deaths (cum.)"})
  master_data = master_data.rename(columns={"% of the economically active population aged 16+ who are unemployed":"Unemployed (%)", "% of all people aged 16-64 who are employees": "Employees (%)", "% of all people aged 16-64 who are self-employed": "Self-employed (%)", "% of households with at least 1 early-years or school age child" : "Households, 1+ child (%)"}) 
  ## CHANGING DATA TYPES
  master_data['People per sq. km'] = master_data['People per sq. km'].str.replace(',', '').astype(float)

  master_data["Cumulative Cases"] = master_data["Cumulative Cases"].astype(float)

  master_data["Deaths (cum.)"] = master_data["Deaths (cum.)"].astype(float)

  ## REMOVING DUPLICATE DATA

  master_data.drop_duplicates()

  #check for missing values
  master_data.isnull

  #drop missing values

  master_data.dropna(axis = "index", how = "any")

  #assign new data to master_data variable

  master_data = master_data.dropna(axis = "index", how = "any")

  ## EXPORTING DATAFRAME TO EXCEL

  master_data.to_csv(f'{file_location}/Master Data.csv', index = False)
  
  print('Master Data has been saved in folder with previous data')
