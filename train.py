import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(BASE_DIR, "data", "realistic_logs.csv")

df = pd.read_csv(data_path)

X = df[["login_hour", "failed_attempts", "ip_change", "device_change"]]
y = df["label"]

model = RandomForestClassifier(n_estimators=200)
model.fit(X, y)

model_path = os.path.join(BASE_DIR, "model", "model.pkl")
joblib.dump(model, model_path)

print("Model trained successfully!")