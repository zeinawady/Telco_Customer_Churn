import streamlit as st
import numpy as np
import pandas as pd
import pickle
from model import train_model, predict
models = pickle.load(open('My_pickeld_model', 'rb'))

st.title('Customer Churn Prediction')
st.write('Enter the customer information to predict churn.')

# Create input fields for user to enter feature values
gender = st.selectbox('Gender', ['Female', 'Male'])
senior_citizen = st.selectbox('Senior Citizen', [0, 1])  # 0 for No, 1 for Yes
partner = st.selectbox('Partner', ['Yes', 'No'])
dependents = st.selectbox('Dependents', ['Yes', 'No'])
tenure = st.number_input('Tenure (in months)', min_value=0, max_value=100, value=0)
phone_service = st.selectbox('Phone Service', ['Yes', 'No'])
multiple_lines = st.selectbox('Multiple Lines', ['Yes', 'No', 'No phone service'])
internet_service = st.selectbox('Internet Service', ['DSL', 'Fiber optic', 'No'])
online_security = st.selectbox('Online Security', ['Yes', 'No', 'No internet service'])
online_backup = st.selectbox('Online Backup', ['Yes', 'No', 'No internet service'])
device_protection = st.selectbox('Device Protection', ['Yes', 'No', 'No internet service'])
tech_support = st.selectbox('Tech Support', ['Yes', 'No', 'No internet service'])
streaming_tv = st.selectbox('Streaming TV', ['Yes', 'No', 'No internet service'])
streaming_movies = st.selectbox('Streaming Movies', ['Yes', 'No', 'No internet service'])
contract = st.selectbox('Contract', ['Month-to-month', 'One year', 'Two year'])
paperless_billing = st.selectbox('Paperless Billing', ['Yes', 'No'])
payment_method = st.selectbox('Payment Method', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
monthly_charges = st.number_input('Monthly Charges', min_value=0.0, value=0.0)
total_charges = st.number_input('Total Charges', min_value=0.0, value=0.0)

# Create a button to predict
if st.button('Predict'):
    # Prepare the input for prediction
    input_data = np.array([[gender, senior_citizen, partner, dependents, tenure, 
                            phone_service, multiple_lines, internet_service, 
                            online_security, online_backup, device_protection, 
                            tech_support, streaming_tv, streaming_movies, 
                            contract, paperless_billing, payment_method, 
                            monthly_charges, total_charges]])
    
    # Make predictions
    prediction = predict(model, input_data)

    # Display the result
    if prediction[0] == 'Yes':
        st.success('Customer is likely to churn.')
    else:
        st.success('Customer is likely to stay.')