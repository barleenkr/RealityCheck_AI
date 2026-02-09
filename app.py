import streamlit as st

st.set_page_config(
    page_title="RealityCheck AI",
    layout="wide"
)

st.sidebar.title("RealityCheck AI")
st.sidebar.caption("Doctor-facing treatment feasibility platform")

st.title("Welcome to RealityCheck AI")
st.write(
    """
    RealityCheck AI helps doctors evaluate whether a treatment plan
    is **practically feasible** for a patient in real Indian contexts.
    """
)

st.info("Use the sidebar to navigate through the system.")