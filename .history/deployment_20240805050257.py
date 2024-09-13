import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load the model
lr = pickle.load(open('pickeld_model', 'rb'))

st.toast('Welcome!', icon='✨')
st.title("Customer Churn Prediction")
st.write('Enter the customer information to predict churn.')

# Create input fields for user to enter feature values
gender = st.selectbox('Gender', ['Female', 'Male'])
senior_citizen = st.selectbox('Senior Citizen', [0, 1])  # 0 for No, 1 for Yes
partner = st.selectbox('Partner', ['Yes', 'No'])
dependents = st.selectbox('Dependents', ['Yes', 'No'])
tenure = st.number_input('Tenure (in months)', min_value=0, max_value=100, value=0)
paperless_billing = st.selectbox('Paperless Billing', ['Yes', 'No'])
monthly_charges = st.number_input('Monthly Charges', min_value=0.0, value=0.0)
total_charges = st.number_input('Total Charges', min_value=0.0, value=0.0)

# One-hot encoding for the remaining categorical variables
multiple_lines = st.selectbox('Multiple Lines', ['Yes', 'No', 'No phone service'])
internet_service = st.selectbox('Internet Service', ['DSL', 'Fiber optic', 'No'])
online_security = st.selectbox('Online Security', ['Yes', 'No', 'No internet service'])
online_backup = st.selectbox('Online Backup', ['Yes', 'No', 'No internet service'])
device_protection = st.selectbox('Device Protection', ['Yes', 'No', 'No internet service'])
tech_support = st.selectbox('Tech Support', ['Yes', 'No', 'No internet service'])
streaming_tv = st.selectbox('Streaming TV', ['Yes', 'No', 'No internet service'])
streaming_movies = st.selectbox('Streaming Movies', ['Yes', 'No', 'No internet service'])
contract = st.selectbox('Contract', ['Month-to-month', 'One year', 'Two year'])
payment_method = st.selectbox('Payment Method', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])

if st.button('Predict'):
  with st.spinner('Loading...'):
    # Prepare the input for prediction with the correct feature names and order
    input_data = {
        'Seniorcitizen': senior_citizen,
        'Partner': 1 if partner == 'Yes' else 0,
        'Dependents': 1 if dependents == 'Yes' else 0,
        'Tenure': tenure,
        'Paperlessbilling': 1 if paperless_billing == 'Yes' else 0,
        'Monthlycharges': monthly_charges,
        'Totalcharges': total_charges,
        'Multiplelines_No phone service': 1 if multiple_lines == 'No phone service' else 0,
        'Multiplelines_Yes': 1 if multiple_lines == 'Yes' else 0,
        'Internetservice_Fiber optic': 1 if internet_service == 'Fiber optic' else 0,
        'Internetservice_No': 1 if internet_service == 'No' else 0,
        'Onlinesecurity_No internet service': 1 if online_security == 'No internet service' else 0,
        'Onlinesecurity_Yes': 1 if online_security == 'Yes' else 0,
        'Onlinebackup_No internet service': 1 if online_backup == 'No internet service' else 0,
        'Onlinebackup_Yes': 1 if online_backup == 'Yes' else 0,
        'Deviceprotection_No internet service': 1 if device_protection == 'No internet service' else 0,
        'Deviceprotection_Yes': 1 if device_protection == 'Yes' else 0,
        'Techsupport_No internet service': 1 if tech_support == 'No internet service' else 0,
        'Techsupport_Yes': 1 if tech_support == 'Yes' else 0,
        'Streamingtv_No internet service': 1 if streaming_tv == 'No internet service' else 0,
        'Streamingtv_Yes': 1 if streaming_tv == 'Yes' else 0,
        'Streamingmovies_No internet service': 1 if streaming_movies == 'No internet service' else 0,
        'Streamingmovies_Yes': 1 if streaming_movies == 'Yes' else 0,
        'Contract_One year': 1 if contract == 'One year' else 0,
        'Contract_Two year': 1 if contract == 'Two year' else 0,
        'Paymentmethod_Credit card (automatic)': 1 if payment_method == 'Credit card (automatic)' else 0,
        'Paymentmethod_Electronic check': 1 if payment_method == 'Electronic check' else 0,
        'Paymentmethod_Mailed check': 1 if payment_method == 'Mailed check' else 0
    }
    
    # Convert to DataFrame to match model input
    input_df = pd.DataFrame([input_data])

    # Make predictions
    prediction = lr.predict(input_df) 
    

    # Display the result
    if prediction[0] == 1 : # Assuming 1 indicates churn and 0 indicates no churn
        st.error('Customer is likely to churn.')
        st.snow()
    else:
        st.success('Customer is likely to stay.')
        st.balloons()
