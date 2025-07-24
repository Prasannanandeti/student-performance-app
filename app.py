import streamlit as st
import pandas as pd
import joblib
model = joblib.load("student_model.pkl")

st.set_page_config(page_title="Student Performance Predictor")
st.title("🎓 Student Performance Predictor")
st.markdown("Predict a student's final exam score (G3) based on academic and behavioral inputs.")

G1 = st.slider("G1 - First Period Grade", 0, 20, 10)
G2 = st.slider("G2 - Second Period Grade", 0, 20, 10)
studytime = st.selectbox("Study Time (1 = low, 4 = high)", [1, 2, 3, 4])
failures = st.selectbox("Number of Past Failures", [0, 1, 2, 3])
absences = st.number_input("Absences", 0, 100, 5)
schoolsup = st.radio("Extra School Support?", ["yes", "no"])

input_data = {
    'G1': G1,
    'G2': G2,
    'studytime': studytime,
    'failures': failures,
    'absences': absences,
    'schoolsup_yes': 1 if schoolsup == 'yes' else 0
}
df_input = pd.DataFrame([input_data])

if st.button("Predict Final Grade"):
    prediction = model.predict(df_input)[0]
    st.success(f"📚 Predicted Final Grade (G3): {round(prediction, 2)} / 20")
