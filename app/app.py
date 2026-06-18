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

scaled_tenure = (tenure - 0) / (72.0 - 0)
scaled_monthly = (monthly_charges - 18.25) / (118.75 - 18.25)

total_charges_raw = tenure * monthly_charges
scaled_total = (total_charges_raw - 0) / (8684.80 - 0)




input_data = {
    'tenure': scaled_tenure,
    'MonthlyCharges': scaled_monthly,
    'TotalCharges' : scaled_total,
    'Contract_One year': 1 if contract == "One year" else 0,
    'Contract_Two year': 1 if contract == "Two year" else 0,
    'TechSupport_No internet service': 1 if tech_support == "No internet service" else 0,
    'TechSupport_Yes': 1 if tech_support == 'Yes' else 0
}    

input_df = pd.DataFrame([input_data])

expected_columns = model.feature_names_in_
for col in expected_columns:
    if col not in input_df.columns:
        input_df[col] = 0
        
        
input_df = input_df[expected_columns]

st.header("Prediction Result")

if st.button("Prediction Result"):
    prediction = model.predict(input_df)[0]
    

    if prediction == 1:
        st.error("HIgh Risk! This customer is predicted to CHURN..")
    else:
        st.success(" Safe! This customer is predicted to STAY.")       
                 
