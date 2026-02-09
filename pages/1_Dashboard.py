import streamlit as st

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Dashboard")
st.write("Overview of recent analyses and system insights.")