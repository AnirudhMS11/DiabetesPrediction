import os
import streamlit as st
import requests
 
FASTAPI_URL = os.environ["FASTAPI_URL"]  # Change if hosted elsewhere
 
st.title("Diabetes Prediction")
 
# Fetch dropdown options
gender_response = requests.get(f"{FASTAPI_URL}/get-gender")
smoking_response = requests.get(f"{FASTAPI_URL}/get-smoking")
 
# Get lists and append custom options
if gender_response.status_code == 200 and smoking_response.status_code == 200:
    genders = gender_response.json().get("gender", [])
    smoking_histories = smoking_response.json().get("smoking_history", [])

    if isinstance(genders,str):
        genders=[genders]
    if "Female" not in genders:
        genders.append("Female")

    if isinstance(smoking_histories,str):
        genders=[smoking_histories]
    if "current" not in smoking_histories:
        smoking_histories.append("current")
else:
    st.error("Failed to load gender or smoking history options.")
    st.stop()
 
# Input form
with st.form("prediction_form"):
    age = st.number_input("Age", min_value=25.0, max_value=80.0, step=0.1)
    
    hypertension_input = st.radio("Hypertension", ["No", "Yes"])
    hypertension = 1 if hypertension_input == "Yes" else 0
 
    heart_disease_input = st.radio("Heart Disease", ["No", "Yes"])
    heart_disease = 1 if heart_disease_input == "Yes" else 0
 
    bmi = st.number_input("BMI", min_value=15.04, max_value=69.55, step=0.01)
    hba1c_level = st.number_input("HbA1c Level", min_value=3.5, max_value=8.2, step=0.1)
    blood_glucose_level = st.number_input("Blood Glucose Level", min_value=80, max_value=240, step=1)
 
    gender = st.selectbox("Gender", genders)
    smoking_history = st.selectbox("Smoking History", smoking_histories)
 
    submitted = st.form_submit_button("Get Prediction")
 
    if submitted:
        data = {
            "age": age,
            "hypertension": hypertension,
            "heart_disease": heart_disease,
            "bmi": bmi,
            "HbA1c_level": hba1c_level,
            "blood_glucose_level": blood_glucose_level,
            "gender": gender,
            "smoking_history": smoking_history,
        }
 
        response = requests.post(f"{FASTAPI_URL}/get-prediction", data=data)
        if response.status_code == 200:
            output_response = response.json()['Prediction']
            output = 'Yes' if output_response==1 else 'No'
            st.success(f"Prediction: {output}")
        else:
            st.error("Failed to get prediction from server.")