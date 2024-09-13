import streamlit as st
import numpy as np
import pandas as pd
import pickle
from lr import train_model, predict  # Make sure 'predict' is defined in your 'lr' module

# Load the trained model
model = pickle.load(open('pickeld_model', 'rb'))

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
    with st.spinner('Loading...'):
        # Prepare the input for prediction and encode categorical variables
        input_data = np.array([[
            1 if gender == 'Male' else 0,  # Gender
            senior_citizen,  # Senior Citizen
            1 if partner == 'Yes' else 0,  # Partner
            1 if dependents == 'Yes' else 0,  # Dependents
            tenure,  # Tenure
            1 if phone_service == 'Yes' else 0,  # Phone Service
            1 if multiple_lines == 'Yes' else 0,  # Multiple Lines
            1 if internet_service == 'Fiber optic' else (0 if internet_service == 'DSL' else 2),  # Internet Service
            1 if online_security == 'Yes' else 0,  # Online Security
            1 if online_backup == 'Yes' else 0,  # Online Backup
            1 if device_protection == 'Yes' else 0,  # Device Protection
            1 if tech_support == 'Yes' else 0,  # Tech Support
            1 if streaming_tv == 'Yes' else 0,  # Streaming TV
            1 if streaming_movies == 'Yes' else 0,  # Streaming Movies
            1 if contract == 'One year' else (2 if contract == 'Two year' else 0),  # Contract
            1 if paperless_billing == 'Yes' else 0,  # Paperless Billing
            1 if payment_method == 'Electronic check' else (0 if payment_method == 'Mailed check' else 2),  # Payment Method
            monthly_charges,  # Monthly Charges
            total_charges  # Total Charges
        ]])

        # Make predictions
        prediction = model.predict(input_data)

    # Display the result
    if prediction[0] == 1:  # Assuming 1 indicates churn and 0 indicates no churn
        st.success('Customer is likely to churn.')
        st.balloons()  # Optional: Show balloons for success
    else:
        st.success('Customer is likely to stay.')
