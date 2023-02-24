# 1. pip install streamlit --upgrade
# 2. create a new folder called 📂dapp
# 3. create a new file called app.py
# 4. copy the canada.xlsx file to the 📂dapp folder
# 5. streamlit run dapp/app.py

import streamlit as st
import pandas as pd
import numpy as np
# interactive visualization
import plotly.express as px
import plotly.graph_objects as go

# global variables
years = list(range(1980, 2014)) # list of years from 1980 to 2013

# Loading the data and preprocessing it for the sake of humanity
@st.cache_data
def load_dataset():
    df = pd.read_excel("dapp/canada.xlsx", sheet_name=1, skiprows=20, skipfooter=2)
    df.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
    df.rename(columns={'OdName':'Country', 'AreaName':'Continent', 
                       'RegName':'Region', 'DevName':'Status'}, inplace=True)
    df.set_index('Country', inplace=True)
    df['Total'] = df[years].sum(axis=1)
    return df

with st.spinner('Loading data...'):
    df = load_dataset()
    st.balloons()