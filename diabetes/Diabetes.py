# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 18:07:52 2023

@author: RINGROW
"""
# -*- coding: utf-8 -*-

import numpy as np
import pickle 
import streamlit as st

#loading the saved model
#rb read binary file
loaded_model=pickle.load(open("C:/Users/RINGROW/Documents/GitHub/Diabetes-Prediction/diabetes/model.sav",'rb'))

#creating a function for Prediction

def DiabetesPrediction(input):
    #changing the input data to numpy array
    input_as_numpy_array=np.asarray(input)
    #reshape the array as we are predicting for one instance
    input_reshaped=input_as_numpy_array.reshape(1,-1)
    prediction=loaded_model.predict(input_reshaped) 
    print(prediction)
    if(prediction[0]==0):
        return 'Prediction: You are not  Diabetic'
    else:
        return 'Prediction: You are   Diabetic'


def main():
    
    #give the page a title
    st.title('Intelligent Diabetes Prediction System')
    
    #getting the input data of the user
    Age=st.text_input("Age")
    Glucose=st.text_input("Glucose level ")
    Pregnancies =st.text_input("Number of pregnancies")
    BloodPressure =st.text_input(" Blood Pressure level")
    SkinThickness=st.text_input("Skin Thickness")
    Insulin =st.text_input("What is your insulin")
    Insulin_1 =st.text_input("What is your insulin 2")
    BMI=st.text_input("what is your BMI")
    DiabetesPedigreeFunction=st.text_input("Your Diabetes predigree function")
    DiabetesPedigreeFunction_1=st.text_input("Your Diabetes predigree function 2")
    
    
    
    #code for prediction
    Diabetes =''
    
    #creating a button for prediction
    if st.button('Diabetes Prediction Result'):
        Diabetes=DiabetesPrediction([Age, Glucose, Pregnancies, BloodPressure, SkinThickness, Insulin, BMI,Insulin_1, 
                              DiabetesPedigreeFunction,DiabetesPedigreeFunction_1])
    
    st.success(Diabetes)
        

if __name__== '__main__':
    main()

