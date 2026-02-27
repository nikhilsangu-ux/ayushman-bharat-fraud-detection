def generate_report(df):

    total_claims = len(df)
    fraud_cases = df[df["risk_level"] == "High"].shape[0]

    report = f"""
    ===== Fraud Detection Report =====

    Total Claims: {total_claims}
    High Risk Claims: {fraud_cases}
    Fraud Percentage: {(fraud_cases/total_claims)*100:.2f}%

    ================================
    """

    return report