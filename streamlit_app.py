import streamlit as st
import pandas as pd

st.title('🎈 App Name')

st.write('Пингвинчики')

df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
with st.expander('Data'):
  st.write("y")
  x_raw=df.drop('species', axis=1)
  st.dataframe(x_raw)

  st.write("y")
  y_raw=df.species
  st.dataframe(y_raw)

with st.sidebar:
  st.header("Выбери:")
  island=st.selectbox('Island', ('Torgersen', 'Dream', Biscoe'))
  bill_length_mm=st.slider('Bill length (mm)',)
  
