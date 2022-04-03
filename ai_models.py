#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 15:02:25 2022

@author: danieljoinson
"""

def model_choice(file_location):

    ai_type = input("Do you want to use a regression model (R) or clustering model (C)? ")
    
    if ai_type == "R":
        from Regression_models import regression
        regression(file_location)
        
            
    elif ai_type == "C":
        from clustering import clustering
        clustering(file_location)
    
