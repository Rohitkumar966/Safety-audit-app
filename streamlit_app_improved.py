
import streamlit as st
import json

# Title of the app
st.title("Streamlit JSON Data Processor")

# Default JSON example
default_json = '''
{
  "name": "Alice",
  "age": 30,
  "email": "alice@example.com"
}
'''

# Text area for JSON input
json_input = st.text_area("Enter JSON data here:", default_json)

# Submit button
if st.button("Submit"):
    try:
        # Parse the JSON data
        data = json.loads(json_input)
        
        # Display success message
        st.success("JSON data successfully processed!")
        
        # Display the structured data
        st.json(data)
        
    except json.JSONDecodeError as e:
        # Display error message if JSON parsing fails
        st.error(f"Invalid JSON data: {e}")
        
    except Exception as e:
        # Display any other error messages
        st.error(f"An error occurred: {e}")

# Debug output
st.write("Debug Info:")
st.write(f"JSON Input: {json_input}")
