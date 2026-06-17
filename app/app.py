import streamlit as st
import pandas as pd
import joblib
import os

model_path = os.path.join('models','xgboost_churn_model.pkl')
model = joblib.load(model_path)

st.title("📞 Customer Churn Prediction App")
st.markdown("Adjust The customer's details below to predict if they will leave.")

st.header("Customer Profile")

col1 , col2 = st.columns(2)

with col1:
    tenure = st.slider("Tenure (Months)",0,72,12)
    
    contract = st.selectbox("Contract Type",["Month-to-month","One year","Two year"])

with col2:
    monthly_charges = st.slider("Monthly Charges ($)", 18.0 ,120.0,70.0)
    tech_support = st.selectbox("Tech Support",['Yes','No', 'No internet service'])    

input_data = {
    'tenure': tenure,
    'MonthlyCharges': monthly_charges,
    'TotalCharges' : tenure * monthly_charges,
    'Contract_One year': 1 if contract == "One year" else 0,
    'Contract_Two year': 1 if contract == "Two year" else 0,
    
    
}    