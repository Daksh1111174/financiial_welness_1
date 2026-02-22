def predict_risk(income, savings_ratio, age):
    if age < 30 and savings_ratio > 0.2:
        return "High"
    elif age < 50:
        return "Moderate"
    else:
        return "Low"
