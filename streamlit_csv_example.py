import streamlit as st
import pandas as pd


@st.cache
def get_data():
    return pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/Errata.csv')


'# World GDP'

df = get_data()

lan = int(df['Lat'].min())
long = int(df['Long_'].max())

countries = df['Country_Region'].unique()

'## By country'
country = st.selectbox('Country', countries)
df[df['Country_Region'] == country]



