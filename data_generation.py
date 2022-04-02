#!/usr/bin/env python3
## This script cleans the data files we provide to users of the code, and generates a master dataset that
## analysis can be performed on. This dataset is then downloaded as an excel file. 


## ADDING RELEVANT PACKAGES

def data_generation():

  import pandas as pd

  file_location = input("Where have you saved the data?")


  ## ADDING COVID-19 CASE DATA

  case_data = pd.read_csv(f'{file_location}/Cumulative Cases.csv')

  case_data

  case_data = pd.read_csv(f'{file_location}/Cumulative Cases.csv')

  ## ADDING COVID-19 DEATH AND VACCINATION DATA

  vax_death_data = pd.read_csv(f'{file_location}/Vaccination and Death.csv')

  ## MERGING CASE, DEATH AND VACCINATION DATAFRAMES TOGETHER

  master_data = case_data.merge(vax_death_data, left_on='areaName', right_on='areaName')

  ## ADDING AND MERGING AGE AND DENSITY DATA

  demo_data = pd.read_csv(f'{file_location}/Age and Density.csv')

  master_data = master_data.merge(demo_data, left_on='areaCode_x', right_on='Area code')

  ## ADDING AND MERGING ETHNICITY DATA

  eth_data = pd.read_csv(f'{file_location}/Ethnicity.csv')

  master_data = master_data.merge(eth_data, left_on='areaCode_x', right_on='Area code')

  ## ADDING AND MERGING KEY WORKER DATA

  key_data = pd.read_csv(f'{file_location}/Key Worker.csv')

  master_data = master_data.merge(key_data, left_on='areaCode_x', right_on='Area code')

  ## ADDING AND MERGING EMPLOYMENT DATA

  employ_data = pd.read_csv(f'{file_location}/Employment.csv')

  master_data = master_data.merge(employ_data, left_on='areaCode_x', right_on='Area code')

  ## ADDING AND MERGING CHILD DATA

  child_data = pd.read_csv(f'{file_location}/Children.csv')

  master_data = master_data.merge(child_data, left_on='areaCode_x', right_on='Area code')

  ## ADDING AND MERGING DEPRIVATION DATA

  depri_data = pd.read_csv(f'{file_location}/Deprivation.csv')

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

  master_data = master_data.rename(columns={"areaName": "Local Authority Name", "cumCasesByPublishDate": "Cumulative Cases", "Average Score":"Deprivation Score", "cumPeopleVaccinatedFirstByPublishDate":"First dose (cumulative)", "cumPeopleVaccinatedSecondByPublishDate":"Second dose (cumulative)", "cumPeopleVaccinatedThirdByPublishDate":"Third dose (cumulative)", "cumDeaths28DaysByPublishDate":"Deaths (cumulative)"})

  ## CHANGING DATA TYPES
  master_data['People per sq. km'] = master_data['People per sq. km'].str.replace(',', '').astype(float)

  master_data["Cumulative Cases"] = master_data["Cumulative Cases"].astype(float)

  master_data["Deaths (cumulative)"] = master_data["Deaths (cumulative)"].astype(float)

  ## REMOVING DUPLICATE DATA

  master_data.drop_duplicates()

  #check for missing values
  master_data.isnull

  #drop missing values

  master_data.dropna(axis = "index", how = "any")

  #assign new data to master_data variable

  master_data = master_data.dropna(axis = "index", how = "any")

  ## EXPORTING DATAFRAME TO EXCEL

  save_location = input("Where would you like to save the data?")

  #input file path

  master_data.to_csv(f'{save_location}Master Data.csv', index = False)
