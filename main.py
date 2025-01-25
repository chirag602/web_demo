import streamlit as st
import pandas as pd
from streamlit import button

st.title("Welcome to African New Dream")
#st.header("python")
#st.markdown("I love python")
#st.code("""for i in range(1,5,1):
 #          print("hello")
  #      """)
# Specify the file path
#df = pd.read_excel(r"C:\Users\DELL\PycharmProjects\streamlitpro\african_crises.xlsx")
#print(df.head())

dataset = pd.read_excel(r"C:\Users\DELL\PycharmProjects\streamlitpro\african_crises.xlsx")
st.dataframe(dataset)

name = st.text_input("enter your name :"),
fname = st.text_input("enter your father name :"),
adr = st.text_area("enter your text :"),
classdata = st.selectbox("enter your class :",(1,2,3,4,5,6))

button = st.button("DONE"),
if button :
    st.markdown(f"""
         name : {name},
         father name : {fname},
         address : {adr},
         class : {classdata}""")



