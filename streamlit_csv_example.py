import streamlit as st
import pandas as pd

@st.cache
def get_data():
    return pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv')


'# CSV: https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv'
'# ....'
'# Introduce el país Destino para ver las recomendaciones'
df = get_data()


countries = df['Country_Region'].unique()

'## By country'
country = st.selectbox('Country', countries)
df[df['Country_Region'] == country]


'# Recomendaciones'
'# ....'





