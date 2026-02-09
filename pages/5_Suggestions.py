import streamlit as st
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

from logic.scoring import feasibility_score
from logic.suggestions import generate_clinical_suggestions

st.title("Clinical Suggestions")
st.caption("AI-assisted clinical adaptation insights")

patient = st.session_state.get("patient_context")
plan = st.session_state.get("treatment_plan")

if not patient or not plan:
    st.warning("Please complete Patient Context and Treatment Plan first.")
else:
    feasibility, _, _ = feasibility_score(patient, plan)
    suggestions = generate_clinical_suggestions(patient, plan, feasibility)

    for category, items in suggestions.items():
        st.markdown(
    f"""
    <div style="
        background:#020617;
        padding:20px;
        border-radius:14px;
        margin-bottom:20px;
    ">
    <h3>{category}</h3>
    """,
    unsafe_allow_html=True
)

        if items:
            for item in items:
                st.markdown(f"- {item}")
        else:
            st.markdown("✔ No major concerns identified in this area.")
    st.markdown("</div>", unsafe_allow_html=True)
    st.divider()
    st.info(
        "These suggestions are advisory in nature and intended to support, not replace, clinical judgement."
    )