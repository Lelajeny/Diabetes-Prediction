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
loaded_model=pickle.load(open("C:/Users/RINGROW/Documents/GitHub/Diabetes-Prediction/diabetes/trained_model1.sav",'rb'))

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
    BMI=st.text_input("what is your BMI")
    DiabetesPedigreeFunction=st.text_input("Your Diabetes predigree function")
    
    
    
    
    #code for prediction
    Diabetes =''
    
    #creating a button for prediction
    if st.button('Diabetes Prediction Result'):
        Diabetes=DiabetesPrediction([Age, Glucose, Pregnancies, BloodPressure, SkinThickness, Insulin, BMI, 
                              DiabetesPedigreeFunction,])
    
    st.success(Diabetes)
    
    st.sidebar.header("User Feedback")
feedback = st.sidebar.text_area("Provide feedback:")
if st.sidebar.button("Submit Feedback"):
    # Store user feedback in a database or file for analysis
    with open("feedback.txt", "a") as f:
        f.write(feedback + "\n")
        
print("Thank you for your feedback")
if __name__== '__main__':
    main()

