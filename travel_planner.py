import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

# Function to get data from Gemini API
def get_data_from_gemini(requirements):
    response = model.generate_content(requirements)
    return response.text

# Streamlit interface
st.title('Travel Planner')

# Collect travel requirements from the user
col1, col2 = st.columns(2, gap="medium")
with col1:
    num = st.text_input("Enter the number of your group:")
    destination = st.text_input("Enter your destination:")
    budget = st.slider("Budget", 100, 5000, 1000)
with col2:
    start_date = st.date_input("Start date:")
    end_date = st.date_input("End date:")
    preference = st.text_input("Enter your interests: eg.museums, outdoor, indoor, love foods...")

requirements = f"""
Plan a detailed itinerary for a group of {num} going to {destination} from {start_date} to {end_date}.
Budget: {budget}. Interests: {preference}.
Consider travel times, meal times, and rest periods between activities.
Suggest morning, afternoon, and evening activities for each day with dining options nearby.
"""

if 'feedback' not in st.session_state:
    st.session_state.feedback = {}

if st.button('Get Data'):
    initial_plan = get_data_from_gemini(requirements)
    st.session_state.initial_plan = initial_plan
    st.write("Initial Plan:", initial_plan)

# Allow users to give feedback on the initial plan
if 'initial_plan' in st.session_state:
    feedback = st.text_area("Provide your feedback to refine the plan:", height=150)
    if st.button('Refine Plan'):
        new_requirements = requirements + " Feedback: " + feedback
        refined_plan = get_data_from_gemini(new_requirements)
        st.write("Refined Plan:", refined_plan)
