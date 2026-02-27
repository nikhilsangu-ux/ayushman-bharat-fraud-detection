from sklearn.ensemble import IsolationForest
import joblib

def train_model(df):
    features = df[["claim_amount"]]

    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(features)

    joblib.dump(model, "models/isolation_model.pkl")
    return model

def load_model():
    return joblib.load("models/isolation_model.pkl")

def predict(model, df):
    df["anomaly_score"] = model.predict(df[["claim_amount"]])
    df["is_anomaly"] = df["anomaly_score"] == -1
    return df