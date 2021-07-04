import pandas as pd 
import streamlit as st
import seaborn as sns
import numpy as np 
import plotly.express as px


st.write("""
#Covid Tracker
""")


df=pd.read_csv("C:/Users/ghata/Downloads/covid19_italy_region.csv")
df1=df.dropna(how="any")
inp=st.selectbox("select your choice",("Bar Chart","Relative plot","pie chart"))
st.write(inp)
df1
if(inp=="Relative plot"):
    rel=sns.relplot(x="TotalPositiveCases",y="Recovered",data=df1)
    st.pyplot(rel)
elif(inp=="Bar Chart"):
    bar=px.bar(df1,x="RegionName",y="Recovered",color="TotalPositiveCases")
    st.plotly_chart(bar)
else:
    pie=px.pie(df1,values="Recovered",names="RegionName")
    st.plotly_chart(pie)
    # bar=sns.barplot(x="TotalPositiveCases",y="Recovered",data=df1)
    # st.pyplot(bar)

