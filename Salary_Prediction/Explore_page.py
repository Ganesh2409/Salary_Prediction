from pickle import TRUE
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings('ignore')

def remove_values(categories,cutoff):
    categories_dict = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categories_dict[categories.index[i]] = categories.index[i]
        else:
            categories_dict[categories.index[i]] = 'other'
    return categories_dict

def cleaned_experience(x):
    if x =="More than 50 years":
        return 50
    elif x == "Less than 1 year":
        return 0.5
    return float(x)

def clean_edlevel(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelors degree'

    elif 'Master’s degree' in x:
        return 'Master’s degree'
    
    elif 'Professional degree' in x:
        return 'Professional degree'
    return 'Less than a Bachelors'

@st.cache_data # once we execute the below  step once it wont need to re run the below code once more it will store it in the cache 
def load_data():
    # pip install pyxlsb
    xlsb_path = 'survey_results_public.xlsb'
    # this will help u to read the xlsb file such that it will be the compressed version of the original csv file
    data = pd.read_excel(xlsb_path, engine='pyxlsb')
    data['Country'].replace('United Kingdom of Great Britain and Northern Ireland', 'Great Briten & Northern Ireland', inplace=True)
    df = data[['Country','YearsCodePro','EdLevel','Employment','ConvertedCompYearly']]
    df = df.rename({'ConvertedCompYearly':'Salary'},axis=1)
    df = df.dropna() 
    df = df[df['Employment'] == 'Employed, full-time']
    df = df.drop('Employment',axis=1)
    country_map = remove_values(df['Country'].value_counts(),400)
    df['Country'] = df['Country'].map(country_map)
    df = df[df['Salary'] <= 250000]
    df = df[df['Salary'] >= 100000]
    df = df[df['Country'] != 'other']


    df['YearsCodePro'] = df['YearsCodePro'].apply(cleaned_experience)



    df['EdLevel'] = df['EdLevel'].apply(clean_edlevel)

    return df

df = load_data()

def show_explore_page():
    st.title("Explore the Software Engineering Salaries")

    st.write(""" ### Stack Overflow Developer Survey 2023  ..... :) """)
    data = df['Country'].value_counts()
    plt.style.use('Solarize_Light2')
    fig, ax = plt.subplots()
    ax.pie(data, labels=data.index, startangle=52,autopct='%.1f',explode=[0,0.12,0.18,0.20,0.24,0.28,0.38,0.44,0.50,0.54,0.58,0.60,0.68,0.70,0.78,0.85,0.98])

    st.write("""#### Number of data from different Countries""")
    st.pyplot(fig)


    st.write("""#### Country vs Salary """)
    plt.style.use('seaborn-v0_8-bright')
    data = df.groupby(['Country'])['Salary'].mean().sort_values(ascending=TRUE)

    st.bar_chart(data) #Built in build barchart in streamlit 

    st.write("""#### Experience vs Salary """) 
    data = df.groupby(['YearsCodePro'])['Salary'].mean()
    st.line_chart(data)
