import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
import plotly.express as px
from PIL import Image

st.title('Covid India Cases Tracking 🚑')
st.write("""

COVID‐19, which was initiated regionally at Wuhan of China, has become a global pandemic by infecting people of almost all the world. Human civilizations are facing threat for their survival and livelihood. No country are getting any substantial relief and solution from this pandemic rather to convince their citizens to make aware and taking precaution by changing their living style. In view of this, this study attempted to assess the awareness, threat, symptoms and its prevention among people of India about the COVID‐19. A total of 522 responses from all over India were received. The respondents have adequate awareness for COVID‐19 outbreak and its preventive measures, out of total, 98% (513) answered that the virus spreads from one person to another, 95% (494) answered that the disease is caused by a virus. Peoples understand the importance of social distancing and other preventive measures prescribed by the government with good attitude for coronavirus. Peoples are following trusted sources for corona information, having confidence to defeat disease but showed their concern for corona threat, are aware about the virus, its common symptoms and prevention, govt. testing and medical facilities. Principal component analysis was used to identify the latent dimensions regarding people's preventive measures and was found that they are majorly adopting three methods, that is, lockdown, naturopathy and social distancing. This study will help government and peoples to understand and handle this coronavirus pandemic effectively and in prevention of COVID‐19, which is crucial for the awareness of society in coming time.

""")
st.write("""By this we can get informations about the ***Covid Cases*** in India.

""")
st.sidebar.title("Filters")
image = Image.open('corona-tracker-social-image-1-1024x576.jpg')
st.image(image,use_column_width=True)
df = pd.read_csv('https://api.covid19india.org/csv/latest/state_wise.csv')

df = df.iloc[1:,0:]

v = st.sidebar.selectbox('Select a chart type : ',('Bar chart','Pie chart','Line chart'))
stt = st.sidebar.selectbox('Select a State : ',df['State'].unique())
status = st.sidebar.radio('Patient Status : ',('Confirmed cases','Recovered cases','Active cases','Death cases'))
state = df[df['State'] == stt]

st.markdown("## **State level analysis**")

def get_tot(state):
    total = pd.DataFrame({
        'Status' : ['Confirmed','Recovered','Deaths','Active'],
        'Number of cases':(state.iloc[0]['Confirmed'],
        state.iloc[0]['Recovered'],
        state.iloc[0]['Deaths'],
        state.iloc[0]['Active'])
    })
    return total

yui = get_tot(state)


if v == 'Bar chart':
    stg = px.bar(yui,x='Status',y='Number of cases',color='Status')
    st.plotly_chart(stg)
elif v == 'Pie chart':
    if status == 'Confirmed cases':
        st.title("Total Confirmed Cases ")
        fig = px.pie(df,values=df['Confirmed'],names=df['State'])
        st.plotly_chart(fig)
    elif status == 'Recovered cases':
        st.title("Total Recovered cases ")
        fig = px.pie(df,values=df['Recovered'],names=df['State'])
        st.plotly_chart(fig)
    elif status == 'Active cases':
        st.title("Total Active cases ")
        fig = px.pie(df,values=df['Active'],names=df['State'])
        st.plotly_chart(fig)
    else:
        st.title("Total Death cases ")
        fig = px.pie(df,values=df['Deaths'],names=df['State'])
        st.plotly_chart(fig)
elif v == 'Line chart':
    if status == 'Confirmed cases':
        st.title("Total Confirmed Cases ")
        fig = px.line(df,x='State',y='Confirmed')
        st.plotly_chart(fig)
    elif status == 'Recovered cases':
        st.title("Total Recovered cases ")
        fig = px.line(df,x='State',y='Recovered')
        st.plotly_chart(fig)
    elif status == 'Active cases':
        st.title("Total Active cases ")
        fig = px.line(df,x='State',y='Active')
        st.plotly_chart(fig)
    else:
        st.title("Total Death cases ")
        fig = px.line(df,x='State',y='Deaths')
        st.plotly_chart(fig)
st.sidebar.subheader("""Created by [Subham Basu](https://www.linkedin.com/in/subham-basu-891a28183/)""")
    
