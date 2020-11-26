import streamlit as st
import pandas as pd


@st.cache
def get_data():
    return pd.read_csv('https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv')


'# World GDP'

df = get_data()

lan = int(df['Lat'].min())
long = int(df['Long_'].max())

countries = df['Country_Region'].unique()

'## By country'
country = st.selectbox('Country', countries)
df[df['Country_Region'] == country]



