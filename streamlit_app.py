
import streamlit as st
import json

# Title of the app
st.title("Updated Application")

# Welcome message
st.write("Welcome to the updated application!")

# Form to submit JSON data
st.header("Submit JSON Data")
json_data = st.text_area("Enter JSON data here")

if st.button("Submit"):
    try:
        # Parse JSON data
        data = json.loads(json_data)
        st.success("Data received successfully!")
        st.json(data)
    except json.JSONDecodeError:
        st.error("Invalid JSON data. Please enter valid JSON.")
