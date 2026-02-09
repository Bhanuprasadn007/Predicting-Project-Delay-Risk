import streamlit as st
import numpy as np
import pickle

# Load model
with open("model/delay_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Project Delay Predictor", layout="centered")

st.title("📈 Project Delay Predictor")
st.write("Predict expected project delay using Linear Regression")

st.divider()

# User inputs
duration = st.number_input("Project Duration (days)", 20, 300, 80)
team_size = st.number_input("Team Size", 2, 20, 5)
budget = st.number_input("Budget (in lakhs / units)", 5, 100, 15)
experience = st.number_input("Average Team Experience (years)", 1, 15, 3)
task_count = st.number_input("Number of Tasks", 10, 200, 65)
requirement_changes = st.number_input("Requirement Changes", 0, 15, 3)
risk = st.slider("Risk Level (1 = Low, 10 = High)", 1, 10, 7)

st.divider()

if st.button("🔍 Predict Delay"):
    input_data = np.array([[duration, team_size, budget,
                             experience, task_count,
                             requirement_changes, risk]])

    prediction = model.predict(input_data)[0]

    st.subheader("📊 Prediction Result")

    if prediction < 5:
        st.success(f"Expected Delay: {prediction:.1f} days (Low Risk)")
    elif prediction < 15:
        st.warning(f"Expected Delay: {prediction:.1f} days (Moderate Risk)")
    else:
        st.error(f"Expected Delay: {prediction:.1f} days (High Risk)")

    st.caption("Prediction generated using Linear Regression model")
