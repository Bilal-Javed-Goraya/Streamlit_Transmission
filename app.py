import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the model and encoders
model = joblib.load('workout_type_classifier_model.joblib')
label_encoder_target = joblib.load('label_encoder_workout_type.joblib')
label_encoder_feature = joblib.load('label_encoder_gender.joblib')

# Function to predict workout type
def predict_workout_type(age, gender, weight, height, max_bpm, avg_bpm, resting_bpm,
                          session_duration, calories_burned, fat_percentage, water_intake,
                          workout_frequency, experience_level, bmi):
    # Create a DataFrame from the input
    input_data = pd.DataFrame([[age, gender, weight, height, max_bpm, avg_bpm, resting_bpm,
                                session_duration, calories_burned, fat_percentage, water_intake,
                                workout_frequency, experience_level, bmi]],
                              columns=['Age', 'Gender', 'Weight (kg)', 'Height (m)', 'Max_BPM', 'Avg_BPM',
                                       'Resting_BPM', 'Session_Duration (hours)', 'Calories_Burned', 
                                       'Fat_Percentage', 'Water_Intake (liters)', 'Workout_Frequency (days/week)', 
                                       'Experience_Level', 'BMI'])

    # Label encode the 'Gender' column
    input_data['Gender'] = label_encoder_feature.transform(input_data['Gender'])

    # Make the prediction using the trained model
    prediction = model.predict(input_data)

    # Decode the prediction back to the original class label (Workout Type)
    workout_type = label_encoder_target.inverse_transform(prediction)
    
    return workout_type[0]

# Streamlit app UI
st.set_page_config(page_title="Workout Type Prediction", page_icon="🏋️", layout="centered")

# Add a title with some style
st.markdown("""
    <h1 style="text-align: center; color: #3E8E41; font-size: 40px;">Predict Your Workout Type</h1>
    <p style="text-align: center; font-size: 20px;">Enter the details below to find out which workout is best for you!</p>
""", unsafe_allow_html=True)

# Add a fun image
st.image("https://www.pngall.com/wp-content/uploads/5/Workout-PNG-Image.png", width=400)

# Create a sidebar with a catchy title
st.sidebar.header("Enter your details:")
st.sidebar.text("Fill in the following information:")

# Create input fields for user data
age = st.sidebar.number_input("Age", min_value=18, max_value=100, value=25)
gender = st.sidebar.selectbox("Gender", options=["Female", "Male"])
weight = st.sidebar.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=70.0)
height = st.sidebar.number_input("Height (m)", min_value=1.2, max_value=2.5, value=1.75)
max_bpm = st.sidebar.number_input("Max BPM", min_value=100, max_value=220, value=180)
avg_bpm = st.sidebar.number_input("Average BPM", min_value=50, max_value=220, value=150)
resting_bpm = st.sidebar.number_input("Resting BPM", min_value=40, max_value=100, value=60)
session_duration = st.sidebar.number_input("Session Duration (hours)", min_value=0.5, max_value=5.0, value=1.0)
calories_burned = st.sidebar.number_input("Calories Burned", min_value=100, max_value=2000, value=500)
fat_percentage = st.sidebar.number_input("Fat Percentage", min_value=5.0, max_value=50.0, value=20.0)
water_intake = st.sidebar.number_input("Water Intake (liters)", min_value=0.5, max_value=5.0, value=2.0)
workout_frequency = st.sidebar.number_input("Workout Frequency (days/week)", min_value=1, max_value=7, value=3)
experience_level = st.sidebar.number_input("Experience Level (1 = Beginner, 10 = Expert)", min_value=1, max_value=10, value=5)
bmi = st.sidebar.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)

# Add a separator line for better visual appeal
st.markdown("---")

# Button to make prediction
if st.button("Predict Workout Type", key="predict_button"):
    with st.spinner("Predicting..."):
        # Predict workout type
        workout_type = predict_workout_type(age, gender, weight, height, max_bpm, avg_bpm, resting_bpm,
                                            session_duration, calories_burned, fat_percentage, water_intake,
                                            workout_frequency, experience_level, bmi)
    
    # Display the result with a nice style
    st.markdown(f"""
        <h3 style="text-align: center; color: #3E8E41;">The predicted workout type is: <span style="color: #FF6347;">{workout_type}</span></h3>
    """, unsafe_allow_html=True)

    # Show a motivational image for the predicted workout type (optional)
    if workout_type == "Strength":
        st.image("https://www.pngkey.com/png/full/313-3136597_bodybuilding-workout-clipart-male-weight-lifting.png", width=300)
    elif workout_type == "Cardio":
        st.image("https://www.pngkey.com/png/full/945-9453767_running-clipart-cool-jogger-person-running.png", width=300)
    elif workout_type == "HIIT":
        st.image("https://www.pngkey.com/png/full/296-2962279_high-intensity-interval-training-clipart.png", width=300)

# Footer with contact info
st.markdown("""
    <p style="text-align: center; font-size: 12px; color: gray;">Made with ❤️ by Bilal Javed Goraya</p>
    <p style="text-align: center; font-size: 12px; color: gray;">For any queries or support, contact: 2019n10718@gmail.com</p>
""", unsafe_allow_html=True)
