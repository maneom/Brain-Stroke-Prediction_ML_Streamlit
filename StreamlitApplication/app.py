import streamlit as st
import pickle
import pandas as pd
import sklearn


transformer = pickle.load(open("transformer.pkl", "rb"))
rfc = pickle.load(open("RandomForestClassifier.pkl", "rb"))

st.set_page_config(layout="wide")
st.title("BRAIN STROKE DETERMINATION")

col1, col2 = st.columns(2)
gender = col1.selectbox("ENTER GENDER", ['Male', 'Female'])
age = col2.number_input("SELECT AGE IN YEARS",min_value=0, max_value=100)
col1, col2, col3 = st.columns(3)
hypertension = col1.radio("DOES PATIENT HAS HYPERTENSION ? ",['True', 'False'])
if hypertension == True:
    hypertension = 1
else:
    hypertension = 0
heart_disease = col2.radio("DOES PATIENT HAVE ANY HEART DISEASE ? ",['True', 'False'])
if heart_disease == True:
    heart_disease = 1
else:
    heart_disease = 0
ever_married = col3.radio("IS PATIENT MARRIED ? ",['Yes','No'])

col1, col2, col3= st.columns(3)
work_type = col1.selectbox("SELECT WORK TYPE OF PATIENT.", ['Private', 'Self-employed', 'Govt_job', 'children'])
residence = col2.selectbox("SELECT RESIDENCE TYPE OF PATIENT.", ['Urban', 'Rural'])
smoke_status = col3.selectbox("SELECT CATEGORY OF PATIENT.", ['formerly smoked', 'never smoked', 'smokes', 'Unknown'])

col1, col2 = st.columns(2)
avg_glucse_level = col1.number_input("ENTER AVERAGE GLUCOSE LEVEL ",step=1)
bmi = col2.number_input("ENTER BODY MASS INDEX ",step=1)


col = ['gender', 'age', 'hypertension', 'heart_disease', 'ever_married','work_type', 'Residence_type', 'avg_glucose_level', 'bmi','smoking_status']

if st.button("SUBMIT DATA"):
    data = pd.DataFrame([[gender,age, hypertension, heart_disease, ever_married, work_type, residence ,avg_glucse_level ,	bmi ,smoke_status]],
                                   columns=['gender', 'age', 'hypertension', 'heart_disease', 'ever_married','work_type', 'Residence_type', 'avg_glucose_level', 'bmi','smoking_status'])
    input = transformer.transform(data)
    if rfc.predict(input)[0] == 1:
        st.success("Patient had a stroke.")
    else:
        st.success("Patient did not had a stroke.")