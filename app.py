import streamlit as st

st.set_page_config(
    page_title="RealityCheck AI",
    layout="wide"
)

# --------- SESSION STATE ---------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "patient_context" not in st.session_state:
    st.session_state.patient_context = {}

if "treatment_plan" not in st.session_state:
    st.session_state.treatment_plan = {}

# --------- LOGIN SCREEN ---------
if not st.session_state.logged_in:
    st.markdown("## 👩‍⚕️ Doctor Login")
    st.caption("RealityCheck AI – Clinical Feasibility Support System")

    with st.form("login_form"):
        doctor_id = st.text_input("Doctor ID")
        hospital = st.text_input("Institution / Hospital")
        submit = st.form_submit_button("Login")

    if submit:
        if doctor_id and hospital:
            st.session_state.logged_in = True
            st.session_state.doctor_id = doctor_id
            st.session_state.hospital = hospital
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Please enter all fields.")

    st.stop()

# --------- MAIN APP ---------
st.sidebar.title("RealityCheck AI")
st.sidebar.markdown("---")
st.sidebar.markdown("### Workflow")
st.sidebar.markdown("""
1. Patient Context  
2. Treatment Plan  
3. Feasibility Analysis  
4. Clinical Suggestions  
""")
st.sidebar.caption("Doctor-facing feasibility intelligence")

st.sidebar.markdown(
    f"""
    **Doctor:** {st.session_state.doctor_id}  
    **Institution:** {st.session_state.hospital}
    """
)

st.title("Welcome to RealityCheck AI")
st.write(
    """
    RealityCheck AI assists clinicians in evaluating whether a treatment plan
    is **practically feasible** for a patient, given real-world Indian constraints.
    """
)

st.info("Navigate using the sidebar to begin analysis.")