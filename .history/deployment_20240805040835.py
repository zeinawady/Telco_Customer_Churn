import streamlit as st
models = pickle.load(open('Spam_classification_final_project.pkl', 'rb'))
st.title('Customer Churn Prediction')
st.write('Enter the customer information to predict churn.')