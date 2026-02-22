def analyze_expense(df):
    df["total_expense"] = df.iloc[:, 1:].sum(axis=1)

    total_income = df["income"].sum()
    total_expense = df["total_expense"].sum()

    savings = total_income - total_expense
    ratio = savings / total_income if total_income > 0 else 0

    return {
        "income": total_income,
        "expense": total_expense,
        "savings": savings,
        "ratio": ratio
    }
