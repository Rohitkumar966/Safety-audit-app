
import streamlit as st
import pandas as pd
from datetime import datetime
from io import BytesIO

# User authentication
def login():
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if username == "admin" and password == "password":
            st.session_state['logged_in'] = True
        else:
            st.sidebar.error("Invalid username or password")

# Main app
def main():
    st.title("Safety Audit Assistant")

    # User input page
    if 'logged_in' not in st.session_state:
        login()
    else:
        st.sidebar.success("Logged in as admin")
        st.sidebar.button("Logout", on_click=lambda: st.session_state.pop('logged_in'))

        st.header("User Input")
        auditor_name = st.text_input("Auditor Name")
        auditor_id = st.text_input("Auditor Staff ID")
        auditee_name = st.text_input("Auditee Name")
        auditee_id = st.text_input("Auditee Staff ID")
        location = st.text_input("Location of Auditing")
        date_of_audit = st.date_input("Date of Audit", datetime.today())

        st.header("Observation Entry")
        observations = []
        for i in range(1, 6):  # Allow up to 5 observations
            st.subheader(f"Observation {i}")
            observation = st.text_area(f"Observation Details {i}")
            hazard_category = st.selectbox(f"Hazard Category {i}", [
                "Electrical", "Hot Work", "Civil/Construction", "Height Work", "Installation",
                "Material Handling", "Drilling", "Grinding", "Confined Space", "Maintenance",
                "Vehicle Testing", "Cooking", "Cylinder Storage", "Trial", "Inspection",
                "Housekeeping", "Others (please specify)"
            ])
            if observation:
                observations.append((observation, hazard_category))

        if st.button("Analyze Observations"):
            results = []
            for obs, category in observations:
                # Predict hazard category (placeholder logic)
                predicted_category = category

                # Map to standards and countermeasures (placeholder logic)
                standards = "Relevant Indian/NBC standards"
                countermeasures = "Suggested countermeasures"

                results.append({
                    "Observation": obs,
                    "Predicted Hazard Category": predicted_category,
                    "Standards": standards,
                    "Countermeasures": countermeasures
                })

            st.header("Results")
            results_df = pd.DataFrame(results)
            st.write(results_df)

            # Export to Excel
            if st.button("Export to Excel"):
                output = BytesIO()
                with pd.ExcelWriter(output, engine='openpyxl') as writer:
                    results_df.to_excel(writer, index=False, sheet_name='Audit Results')
                st.download_button(
                    label="Download Excel file",
                    data=output.getvalue(),
                    file_name='audit_results.xlsx',
                    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )

        # Admin dashboard
        st.header("Admin Dashboard")
        if st.button("View Audit Logs"):
            # Placeholder for audit logs
            audit_logs = pd.DataFrame({
                "Auditor Name": [auditor_name],
                "Auditor ID": [auditor_id],
                "Auditee Name": [auditee_name],
                "Auditee ID": [auditee_id],
                "Location": [location],
                "Date of Audit": [date_of_audit],
                "Observation": [obs for obs, _ in observations],
                "Predicted Hazard Category": [predicted_category for _, predicted_category in observations],
                "Standards": [standards for _ in observations],
                "Countermeasures": [countermeasures for _ in observations]
            })
            st.write(audit_logs)

            # Export audit logs to Excel
            if st.button("Export Audit Logs to Excel"):
                output = BytesIO()
                with pd.ExcelWriter(output, engine='openpyxl') as writer:
                    audit_logs.to_excel(writer, index=False, sheet_name='Audit Logs')
                st.download_button(
                    label="Download Audit Logs Excel file",
                    data=output.getvalue(),
                    file_name='audit_logs.xlsx',
                    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )

if __name__ == "__main__":
    main()
