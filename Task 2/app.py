import streamlit as st
import pandas as pd
import joblib

# Load the saved model
model = joblib.load('model.pkl')

# Define the input fields for user data
st.title('Credit Card Fraud Detection')
cc_num = st.number_input('Credit Card Number', min_value=1)
merchant = st.number_input('Merchant ID', min_value=1)
category = st.number_input('Category', min_value=1)
amt = st.number_input('Transaction Amount', min_value=0.0)
first = st.number_input('First Transaction', min_value=0)
last = st.number_input('Last Transaction', min_value=0)
gender = st.number_input('Gender (0 for Male, 1 for Female)', min_value=0, max_value=1)
street = st.number_input('Street', min_value=0)
city = st.number_input('City', min_value=0)
state = st.number_input('State', min_value=0)
city_pop = st.number_input('City Population', min_value=0)
job = st.number_input('Job Type', min_value=0)
trans_num = st.number_input('Transaction Number', min_value=0)
merch_long = st.number_input('Merchant Longitude', min_value=0.0)
year = st.number_input('Year', min_value=2000, max_value=2100)
month = st.number_input('Month', min_value=1, max_value=12)
day = st.number_input('Day', min_value=1, max_value=31)
hour = st.number_input('Hour', min_value=0, max_value=23)
minute = st.number_input('Minute', min_value=0, max_value=59)

# Prepare the input data in the required format
input_data = pd.DataFrame({
    'cc_num': [cc_num],
    'merchant': [merchant],
    'category': [category],
    'amt': [amt],
    'first': [first],
    'last': [last],
    'gender': [gender],
    'street': [street],
    'city': [city],
    'state': [state],
    'city_pop': [city_pop],
    'job': [job],
    'trans_num': [trans_num],
    'merch_long': [merch_long],
    'year': [year],
    'month': [month],
    'day': [day],
    'hour': [hour],
    'minute': [minute]
})

# Make prediction using the loaded model
if st.button('Predict'):
    prediction = model.predict(input_data)
    if prediction == 1:
        st.write("Fraudulent Transaction Detected!")
    else:
        st.write("Transaction is not fraudulent.")
