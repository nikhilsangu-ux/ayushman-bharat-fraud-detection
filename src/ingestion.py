import pandas as pd
import sqlite3

def load_claims(csv_path):
    df = pd.read_csv(csv_path)
    return df

def save_to_db(df, db_path="database/claims.db"):
    conn = sqlite3.connect(db_path)
    df.to_sql("claims", conn, if_exists="replace", index=False)
    conn.close()