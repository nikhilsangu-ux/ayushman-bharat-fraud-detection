def calculate_risk(df):

    df["risk_score"] = (
        df["high_amount_flag"].astype(int) * 30 +
        df["ghost_flag"].astype(int) * 30 +
        df["high_frequency_flag"].astype(int) * 20 +
        df["is_anomaly"].astype(int) * 20
    )

    df["risk_level"] = df["risk_score"].apply(
        lambda x: "High" if x >= 60 else
                  "Medium" if x >= 30 else
                  "Low"
    )

    return df