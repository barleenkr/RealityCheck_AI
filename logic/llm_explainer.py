# logic/llm_explainer.py
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def explain_feasibility(feasibility, patient_risk, treatment_risk, patient, plan):
    prompt = f"""
You are a clinical decision support assistant.
Your role is to EXPLAIN results, not give medical advice.

Context:
- Feasibility Score: {feasibility}%
- Patient Constraint Burden: {round(patient_risk*100)}%
- Treatment Complexity Burden: {round(treatment_risk*100)}%

Patient Context:
- Income level: {patient.get("income_level")}
- Employment type: {patient.get("employment_type")}
- Travel distance: {patient.get("travel_distance")} km
- Literacy level: {patient.get("literacy_level")}

Treatment Characteristics:
- Duration: {plan.get("duration_days")} days
- Doses per day: {plan.get("doses_per_day")}
- Visits required: {plan.get("visits_required")}
- Estimated cost: ₹{plan.get("estimated_cost")}

Task:
Explain to a doctor WHY the feasibility score is at this level.
Use neutral, non-prescriptive language.
Do NOT suggest medications or diagnoses.
Keep it concise and professional.
"""

    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=60)
    return response.json()["response"]