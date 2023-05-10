import streamlit as st
import pandas as pd
import numpy as np

st.title('Data Fabric')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://docs.google.com/spreadsheets/d/1Lii15km8Q91IWQKrhY6I0f92ZR2o4st7/edit?usp=sharing&ouid=108141985598584621816&rtpof=true&sd=true')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data