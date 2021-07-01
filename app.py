import pandas as pd 
import streamlit as st
import seaborn as sns
import numpy as np 


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

