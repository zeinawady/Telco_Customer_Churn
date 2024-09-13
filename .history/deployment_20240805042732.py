import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('My_pickled_model.pkl', 'rb'))

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

# Prepare the input for prediction and include all one-hot encoded features
if st.button('Predict'):
    # Prepare input data
    input_data = np.array([[
        1 if gender == 'Male' else 0,  # Gender (assuming Male = 1, Female = 0)
        senior_citizen,  # Senior Citizen
        1 if partner == 'Yes' else 0,  # Partner
        1 if dependents == 'Yes' else 0,  # Dependents
        tenure,  # Tenure
        1 if phone_service == 'Yes' else 0,  # Phone Service
        1 if multiple_lines == 'Yes' else (0 if multiple_lines == 'No' else 2),  # Multiple Lines
        1 if internet_service == 'Fiber optic' else (0 if internet_service == 'DSL' else 2),  # Internet Service
        1 if online_security == 'Yes' else (0 if online_security == 'No' else 2),  # Online Security
        1 if online_backup == 'Yes' else (0 if online_backup == 'No' else 2),  # Online Backup
        1 if device_protection == 'Yes' else (0 if device_protection == 'No' else 2),  # Device Protection
        1 if tech_support == 'Yes' else (0 if tech_support == 'No' else 2),  # Tech Support
        1 if streaming_tv == 'Yes' else (0 if streaming_tv == 'No' else 2),  # Streaming TV
        1 if streaming_movies == 'Yes' else (0 if streaming_movies == 'No' else 2),  # Streaming Movies
        1 if contract == 'One year' else (2 if contract == 'Two year' else 0),  # Contract
        1 if paperless_billing == 'Yes' else 0,  # Paperless Billing
        1 if payment_method == 'Electronic check' else (0 if payment_method == 'Mailed check' else 2),  # Payment Method
        monthly_charges,  # Monthly Charges
        total_charges,  # Total Charges
        # One-hot encoding for Multiple Lines
        1 if multiple_lines == 'No phone service' else 0,  # Multiple Lines - No phone service
        1 if multiple_lines == 'Yes' else 0,  # Multiple Lines - Yes
        1 if internet_service == 'Fiber optic' else 0,  # Internet Service - Fiber optic
        1 if internet_service == 'No' else 0,  # Internet Service - No
        1 if online_security == 'Yes' else 0,  # Online Security - Yes
        1 if online_security == 'No internet service' else 0,  # Online Security - No internet service
        1 if online_backup == 'Yes' else 0,  # Online Backup - Yes
        1 if online_backup == 'No internet service' else 0,  # Online Backup - No internet service
        1 if device_protection == 'Yes' else 0,  # Device Protection - Yes
        1 if device_protection == 'No internet service' else 0,  # Device Protection - No internet service
        1 if tech_support == 'Yes' else 0,  # Tech Support - Yes
        1 if tech_support == 'No internet service' else 0,  # Tech Support - No internet service
        1 if streaming_tv == 'Yes' else 0,  # Streaming TV - Yes
        1 if streaming_tv == 'No internet service' else 0,  # Streaming TV - No internet service
        1 if streaming_movies == 'Yes' else 0,  # Streaming Movies - Yes
        1 if streaming_movies == 'No internet service' else 0,  # Streaming Movies - No internet service
        1 if contract == 'One year' else 0,  # Contract - One year
        1 if contract == 'Two year' else 0,  # Contract - Two year
        1 if payment_method == 'Credit card (automatic)' else 0,  # Payment Method - Credit card (automatic)
        1 if payment_method == 'Mailed check' else 0  # Payment Method - Mailed check
    ]])

    # Make predictions
    prediction = model.predict(input_data)

    # Display the result
    if prediction[0] == 1:  # Assuming 1 indicates churn and 0 indicates no churn
        st.success('Customer is likely to churn.')
    else:
        st.success('Customer is likely to stay.')
