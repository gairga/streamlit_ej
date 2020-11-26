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



fig = px.scatter_mapbox(df, lat="Lat", lon="Long_", hover_name="Country_Region", hover_data=["Province_State", "Population"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
