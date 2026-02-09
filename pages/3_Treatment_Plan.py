import streamlit as st

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.title("Treatment Plan")
st.caption("Define treatment structure and burden")

with st.form("treatment_plan_form"):
    duration_days = st.slider(
        "Treatment duration (days)",
        1, 180, 30
    )

    doses_per_day = st.selectbox(
        "Doses per day",
        [1, 2, 3, 4]
    )

    visits_required = st.slider(
        "Number of hospital visits required",
        0, 10, 2
    )

    estimated_cost = st.slider(
        "Estimated treatment cost (₹)",
        0, 20000, 3000, step=500
    )

    investigations = st.selectbox(
        "Investigations required",
        ["Low", "Medium", "High"]
    )

    submitted = st.form_submit_button("Save Treatment Plan")

if submitted:
    st.session_state.treatment_plan = {
        "duration_days": duration_days,
        "doses_per_day": doses_per_day,
        "visits_required": visits_required,
        "estimated_cost": estimated_cost,
        "investigations": investigations.lower()
    }

    st.success("Treatment plan saved successfully.")