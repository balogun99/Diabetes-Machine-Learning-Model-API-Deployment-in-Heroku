#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 05:55:28 2025

@author: balogunishaq
"""
# installing the required libraries

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

# calling the instance of FASTAPI

app = FastAPI()

# creating the class for BaseModel

class model_input(BaseModel):
    Pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int

# loading the saved model
diabetes_model = pickle.load(open('/Users/balogunishaq/Desktop/Complete Machine Learning Course - Siddhardhan/Machine Learning/MLtuTs - Part 5 Model Deployment/Diabetes Model for API/diabetes_trained_model.sav', 'rb'))

# create the API
@app.post('/diabetes_prediction')

# create a function for input parameters
def diabetes_pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    preg = input_dictionary['Pregnancies']
    glu = input_dictionary['Glucose']
    bp = input_dictionary['BloodPressure']
    skin = input_dictionary['SkinThickness']
    insulin = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    dpf = input_dictionary['DiabetesPedigreeFunction']
    age = input_dictionary['Age']
    
    input_list = [preg, glu, bp, skin, insulin, bmi, dpf, age]
    
    prediction = diabetes_model.predict([input_list])
    
    if prediction[0] == 0:
        return 'The person is not Diabetic'
    else:
        return 'The person is Diabetic'
    