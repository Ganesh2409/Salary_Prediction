import pickle
import streamlit as st
import numpy as np
import pandas as pd 
import seaborn as sns 


label_encoder_column = pickle.load(open('Salary_Prediction/models/label_encoder.pkl', 'rb'))
ordinal_encoder_column = pickle.load(open('Salary_Prediction/models/ordinal_encoder.pkl', 'rb'))
random_forest_model = pickle.load(open('Salary_Prediction/models/random_forest.pkl', 'rb'))


def show_predict_page():
    st.title("Software Developer Salary Predictor")
    st.write("""### we need some information to predict the salary""")

    countries = [
        'Australia','Brazil','Canada','Denmark','France','Germany','Great Briten & Northern Ireland','India','Israel','Italy','Netherlands','Norway','Poland','Spain','Sweden','Switzerland','United States of America',

    ]

    education =[
        'Bachelors degree','Master’s degree','Professional degree','Less than a Bachelors',

    ]

    country = st.selectbox("Specify The Country",countries)
    education = st.selectbox("Provide The Education Qualification",education)
    experience = st.slider("Years Of Experience",0,20,2)
    ok = st.button('Caluculate Salary')



    if ok:
        x = np.array([[country, experience, education]])
        print(f"Label-Encoded Classes for 'country': {label_encoder_column.classes_}")
        transformed_education = ordinal_encoder_column.transform([[education]])
        x[:, 0] = label_encoder_column.transform(x[:, 0])
        x[:, 2] = transformed_education
        x = x.astype(float)
        salary = random_forest_model.predict(x)
        st.subheader(f"The Estimated Salary is {salary[0]:.2f} $ 's ")
