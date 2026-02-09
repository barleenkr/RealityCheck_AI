import streamlit as st

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Patient Context")
st.caption("Enter basic socioeconomic and practical constraints")

with st.form("patient_context_form"):
    income_level = st.selectbox(
        "Income level",
        ["Low", "Middle", "High"]
    )

    employment_type = st.selectbox(
        "Employment type",
        ["Daily wage", "Fixed job", "Unemployed"]
    )

    travel_distance = st.slider(
        "Travel distance to hospital (km)",
        0, 100, 10
    )

    family_support = st.radio(
        "Family support available?",
        ["Yes", "No"]
    )

    literacy_level = st.selectbox(
        "Literacy level",
        ["Low", "Medium", "High"]
    )

    submitted = st.form_submit_button("Save Patient Context")

if submitted:
    st.session_state.patient_context = {
        "income_level": income_level.lower(),
        "employment_type": employment_type.lower().replace(" ", "_"),
        "travel_distance": travel_distance,
        "family_support": family_support.lower(),
        "literacy_level": literacy_level.lower()
    }

    st.success("Patient context saved successfully.")