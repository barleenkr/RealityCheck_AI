import streamlit as st

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

from logic.scoring import feasibility_score

st.title("Feasibility Analysis")

patient = st.session_state.get("patient_context")
plan = st.session_state.get("treatment_plan")

if not patient or not plan:
    st.warning("Please complete Patient Context and Treatment Plan first.")
else:
    feasibility, patient_risk, treatment_risk = feasibility_score(patient, plan)

    st.subheader("Overall Feasibility Score")
    st.metric(
        label="Treatment Feasibility",
        value=f"{feasibility} %"
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Patient Constraint Burden")
        st.progress(patient_risk)
        st.caption(f"Risk contribution: {round(patient_risk * 100)} %")

    with col2:
        st.subheader("Treatment Complexity Burden")
        st.progress(treatment_risk)
        st.caption(f"Risk contribution: {round(treatment_risk * 100)} %")

    if feasibility >= 70:
        st.success("High likelihood of practical adherence.")
    elif feasibility >= 40:
        st.warning("Moderate feasibility. Adaptations recommended.")
    else:
        st.error("Low feasibility. High risk of treatment dropout.")