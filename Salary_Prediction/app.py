import streamlit as st ,numpy as np,pandas as pd

from predict_page import *
from Explore_page import * 
page = st.sidebar.selectbox("Explore Or Predict",("Predict","Explore"))
if page == "Predict":
    show_predict_page()
else:
    show_explore_page()

