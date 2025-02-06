import streamlit as st
import dill
import numpy as np

st.title("Student Marks Prediction")


Hours=st.text_input("Enter the number of hours you study:")

with open(r"s_project.dill", "rb") as f:
    model = dill.load(f)

if st.button("prediction"):
    data=[[Hours]]
    data_array=np.array(data)
    prediction=model.predict(data_array)
    st.write(prediction)
