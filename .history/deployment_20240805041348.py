import streamlit as st
import pickle
models = pickle.load(open('My_pickeld_model', 'rb'))

st.title('Customer Churn Prediction')
st.write('Enter the customer information to predict churn.')