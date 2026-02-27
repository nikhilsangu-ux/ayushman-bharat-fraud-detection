def create_features(df):

    # Upcoding detection
    df["high_amount_flag"] = df["claim_amount"] > df["claim_amount"].mean()

    # Ghost billing detection
    df["ghost_flag"] = df["patient_id"].duplicated()

    # Frequency anomaly
    claim_counts = df.groupby("hospital_id")["claim_id"].transform("count")
    df["high_frequency_flag"] = claim_counts > claim_counts.mean()

    return df