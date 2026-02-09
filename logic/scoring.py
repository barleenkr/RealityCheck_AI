# logic/scoring.py

def patient_constraint_score(patient):
    score = 0

    # Income constraint
    if patient["income_level"] == "low":
        score += 0.30
    elif patient["income_level"] == "middle":
        score += 0.15
    else:
        score += 0.05

    # Employment constraint
    if patient["employment_type"] == "daily_wage":
        score += 0.30
    elif patient["employment_type"] == "unemployed":
        score += 0.20
    else:
        score += 0.10

    # Literacy constraint
    if patient["literacy_level"] == "low":
        score += 0.25
    elif patient["literacy_level"] == "medium":
        score += 0.15
    else:
        score += 0.05

    # Travel burden
    if patient["travel_distance"] > 50:
        score += 0.20
    elif patient["travel_distance"] > 20:
        score += 0.10

    return min(score, 1.0)


def treatment_complexity_score(plan):
    score = 0

    # Duration burden
    if plan["duration_days"] > 90:
        score += 0.30
    elif plan["duration_days"] > 30:
        score += 0.20
    else:
        score += 0.10

    # Dosing burden
    if plan["doses_per_day"] >= 3:
        score += 0.30
    elif plan["doses_per_day"] == 2:
        score += 0.20
    else:
        score += 0.10

    # Visit burden
    if plan["visits_required"] > 5:
        score += 0.25
    elif plan["visits_required"] > 2:
        score += 0.15

    # Cost burden
    if plan["estimated_cost"] > 10000:
        score += 0.30
    elif plan["estimated_cost"] > 5000:
        score += 0.20
    else:
        score += 0.10

    return min(score, 1.0)


def feasibility_score(patient, plan):
    patient_risk = patient_constraint_score(patient)
    treatment_risk = treatment_complexity_score(plan)

    # Weighted combination
    combined_risk = (0.6 * patient_risk) + (0.4 * treatment_risk)

    # Convert to feasibility percentage
    feasibility = round((1 - combined_risk) * 100, 1)

    return feasibility, patient_risk, treatment_risk