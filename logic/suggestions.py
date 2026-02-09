# logic/suggestions.py

def generate_clinical_suggestions(patient, plan, feasibility):
    suggestions = {
        "Regimen Adjustments": [],
        "Follow-up Strategy": [],
        "Counselling Focus": [],
        "Monitoring Alerts": []
    }

    # --- Regimen Adjustments ---
    if plan["doses_per_day"] >= 3:
        suggestions["Regimen Adjustments"].append(
            "High dosing frequency detected. Consider simplifying dosing schedule if clinically appropriate."
        )

    if plan["duration_days"] > 60:
        suggestions["Regimen Adjustments"].append(
            "Long treatment duration may reduce adherence. Shorter or phased regimens may improve feasibility."
        )

    # --- Follow-up Strategy ---
    if plan["visits_required"] > 3 and patient["employment_type"] == "daily_wage":
        suggestions["Follow-up Strategy"].append(
            "Frequent hospital visits may conflict with daily-wage employment. Tele-follow-ups or bundled visits may help."
        )

    if patient["travel_distance"] > 30:
        suggestions["Follow-up Strategy"].append(
            "Significant travel burden detected. Consider reducing visit frequency where possible."
        )

    # --- Counselling Focus ---
    if patient["literacy_level"] == "low":
        suggestions["Counselling Focus"].append(
            "Low literacy level detected. Enhanced verbal counselling and visual aids are recommended."
        )

    if patient["family_support"] == "no":
        suggestions["Counselling Focus"].append(
            "Limited family support detected. Additional counselling and follow-up reinforcement advised."
        )

    # --- Monitoring Alerts ---
    if feasibility < 40:
        suggestions["Monitoring Alerts"].append(
            "High risk of early treatment dropout. Close monitoring recommended during initial weeks."
        )

    if plan["estimated_cost"] > 8000 and patient["income_level"] == "low":
        suggestions["Monitoring Alerts"].append(
            "High cost sensitivity detected. Financial counselling or alternative options may be needed."
        )

    return suggestions