import os
from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel
from backend.utils import log_event
from backend.behavior import update_behavior, is_anomalous

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "model", "model.pkl")

model = joblib.load(model_path)

class LoginData(BaseModel):
    username: str
    login_hour: int
    failed_attempts: int
    ip_change: int
    device_change: int

@app.post("/predict")
def predict(data: LoginData):
    
    features = np.array([[data.login_hour, data.failed_attempts,
                          data.ip_change, data.device_change]])

    pred = model.predict(features)[0]

    # 🔥 Risk Engine
    risk = 0

    if data.failed_attempts > 5:
        risk += 0.4

    if data.ip_change:
        risk += 0.3

    if data.device_change:
        risk += 0.3

    if is_anomalous(data.username, data.login_hour):
        risk += 0.3

    result = "intrusion" if pred == 1 or risk > 0.6 else "normal"

    update_behavior(data.username, data.login_hour)

    log_event(f"{data.username} → {result}, risk={risk}")

    return {
        "result": result,
        "risk_score": risk
    }