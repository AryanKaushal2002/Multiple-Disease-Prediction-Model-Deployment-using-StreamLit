# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 2023

@author: AK
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu 


# loading the saved models

diabetes_model = pickle.load(open("./models/diabetes_model_new.sav",'rb'))
heart_model = pickle.load(open("./models/heart_disease_model.sav",'rb'))
parkinsons_model = pickle.load(open("./models/parkinsons_model.sav",'rb'))
breast_model = pickle.load(open("./models/breast_cancer_model.sav",'rb'))

# sidebar navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System', 
                           ['Heart Disease Prediction',
                            'Diabetes Prediction',
                            'Parkinson\'s Prediction',
                            'Breast Cancer Prediction'],
                           icons=['heart','activity','person','gender-female'],
                           default_index=0)
    

# Heart Disease Prediction Page   
if (selected == 'Heart Disease Prediction'): 
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 1 = normal; 2 = fixed defect; 3 = reversible defect')        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        if not all([age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]):
            st.warning("Please fill in all the fields.")
        else:
            heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
            
            if (heart_prediction[0] == 1):
              heart_diagnosis = 'The person has a heart disease'
            else:
              heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)  






# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
        
    # code for prediction
    diab_diagnosis=''
    
    # create a button for prediction
    
    if st.button('Diabetes Test Result'):
        if not all([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]):
            st.warning("Please fill in all the fields.")
        else:
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            
            if (diab_prediction[0] == 1):
              diab_diagnosis = 'The person is diabetic'
            else:
              diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)  
  

    


# Parkinsons Prediction Page  
if (selected == 'Parkinson\'s Prediction'):    
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP: Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP: Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP: Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP: Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP: Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP: RAP')
        
    with col2:
        PPQ = st.text_input('MDVP: PPQ')
        
    with col3:
        DDP = st.text_input('Jitter: DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP: Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP: Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer: APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer: APQ5')
        
    with col3:
        APQ = st.text_input('MDVP: APQ')
        
    with col4:
        DDA = st.text_input('Shimmer: DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        if not all([fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]):
            st.warning("Please fill in all the fields.")
        else:
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
            
            if (parkinsons_prediction[0] == 1):
              parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
              parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)    

    

# Breast Cancer Prediction Page
if selected == 'Breast Cancer Prediction':
    # Page title
    st.title('Breast Cancer Prediction using ML')

    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        mean_radius = st.text_input('Mean Radius')

        mean_smoothness = st.text_input('Mean Smoothness')
        
        mean_symmetry = st.text_input('Mean Symmetry')

        perimeter_error = st.text_input('Perimeter Error')

    with col2:
        mean_texture = st.text_input('Mean Texture')

        mean_compactness = st.text_input('Mean Compactness')

        mean_fractal_dimension = st.text_input('Mean Fractal Dimension')
        
        area_error = st.text_input('Area Error')

    with col3:
        mean_perimeter = st.text_input('Mean Perimeter')

        mean_concavity = st.text_input('Mean Concavity')
        
        radius_error = st.text_input('Radius Error')    

        smoothness_error = st.text_input('Smoothness Error')

    with col4:
        mean_area = st.text_input('Mean Area')

        mean_concave_points = st.text_input('Mean Concave Points')
        
        texture_error = st.text_input('Texture Error')

        compactness_error = st.text_input('Compactness Error')


    with col1:
        concavity_error = st.text_input('Concavity Error')
        
        worst_radius = st.text_input('Worst Radius')
        
        worst_smoothness = st.text_input('Worst Smoothness')
        
        worst_symmetry = st.text_input('Worst Symmetry')

    with col2:        
        concave_points_error = st.text_input('Concave Points Error')
        
        worst_texture = st.text_input('Worst Texture')
        
        worst_compactness = st.text_input('Worst Compactness')
        
        worst_fractal_dimension = st.text_input('Worst Fractal Dimension')

    with col3:
        symmetry_error = st.text_input('Symmetry Error')
        
        worst_perimeter = st.text_input('Worst Perimeter')
        
        worst_concavity = st.text_input('Worst Concavity')

    with col4:
        fractal_dimension_error = st.text_input('Fractal Dimension Error')
        
        worst_area = st.text_input('Worst Area')
        
        worst_concave_points = st.text_input('Worst Concave Points')

        
    # Code for prediction
    cancer_diagnosis = ''
    
    # Creating a button for prediction
    if st.button('Breast Cancer Test Result'):
        if not all([mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness, mean_compactness,
                    mean_concavity, mean_concave_points, mean_symmetry, mean_fractal_dimension, radius_error,
                    texture_error, perimeter_error, area_error, smoothness_error, compactness_error, concavity_error,
                    concave_points_error, symmetry_error, fractal_dimension_error, worst_radius, worst_texture,
                    worst_perimeter, worst_area, worst_smoothness, worst_compactness, worst_concavity,
                    worst_concave_points, worst_symmetry, worst_fractal_dimension]):
            st.warning("Please fill in all the fields.")
        else:
            cancer_prediction = breast_model.predict([[mean_radius, mean_texture, mean_perimeter, mean_area,
                                                       mean_smoothness, mean_compactness, mean_concavity,
                                                       mean_concave_points, mean_symmetry, mean_fractal_dimension,
                                                       radius_error, texture_error, perimeter_error, area_error,
                                                       smoothness_error, compactness_error, concavity_error,
                                                       concave_points_error, symmetry_error, fractal_dimension_error,
                                                       worst_radius, worst_texture, worst_perimeter, worst_area,
                                                       worst_smoothness, worst_compactness, worst_concavity,
                                                       worst_concave_points, worst_symmetry, worst_fractal_dimension]])
            
            if cancer_prediction[0] == 1:
                cancer_diagnosis = 'The person is diagnosed with breast cancer.'
            else:
                cancer_diagnosis = 'The person is not diagnosed with breast cancer.'
        
    st.success(cancer_diagnosis)


    






    
    
    
    
    
    
    
