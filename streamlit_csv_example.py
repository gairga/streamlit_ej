import streamlit as st
import pandas as pd
import plotly.express as px


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



token = open(".pk.eyJ1IjoiZXJpYm0iLCJhIjoiY2toeWFkYjRqMDU1MDJwb2gwYXh2MGw5aSJ9.9PUU7uhK7sTlPisnXJ1Hfg").read() # you will need your own token


us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")


fig = px.scatter_mapbox(us_cities, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Population"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300)
fig.update_layout(mapbox_style="dark", mapbox_accesstoken=token)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


