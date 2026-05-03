import streamlit as st
import requests

st.title("🔐 Smart Login IDS")

username = st.text_input("Username")
hour = st.slider("Login Hour", 0, 23)
failed = st.slider("Failed Attempts", 0, 10)
ip = st.selectbox("IP Changed", [0,1])
device = st.selectbox("Device Changed", [0,1])

if st.button("Analyze"):

    res = requests.post("http://127.0.0.1:8000/predict", json={
        "username": username,
        "login_hour": hour,
        "failed_attempts": failed,
        "ip_change": ip,
        "device_change": device
    })

    data = res.json()

    if data["result"] == "intrusion":
        st.error("🚨 Intrusion Detected")
    else:
        st.success("✅ Normal")

    st.metric("Risk Score", data["risk_score"])
    st.progress(data["risk_score"])