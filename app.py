# src/app.py

import streamlit as st
import sys
import os

# Ensure the parent directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_processing import process_input
from src.model import generate_meditation

st.title("Personalized Meditation Session Generator")

# User Inputs
mood = st.selectbox("How are you feeling?", ["Relaxed", "Stressed", "Anxious"])
time = st.slider("How much time do you have? (in minutes)", 5, 60, 10)

# Generate Meditation Session
if st.button("Generate Meditation"):
    with st.spinner('Creating your personalized meditation session...'):
        input_data = {"mood": mood, "time": time}
        features = process_input(input_data)
        session = generate_meditation(features)
        st.success("Here is your meditation session:")
        st.write(session)
