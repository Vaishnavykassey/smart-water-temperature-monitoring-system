import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random
from datetime import datetime

# Title
st.set_page_config(page_title="Smart Water Temperature Monitor", layout="centered")
st.title("💧 Smart Water Temperature Monitoring System")

# Simulated temperature reading
def get_current_temperature():
    return round(random.uniform(20.0, 35.0), 2)

# Save to CSV
def save_data(timestamp, temperature):
    df = pd.DataFrame([[timestamp, temperature]], columns=["Timestamp", "Temperature"])
    df.to_csv("temperature_log.csv", mode="a", header=not pd.io.common.file_exists("temperature_log.csv"), index=False)

# Read from CSV
def read_data():
    try:
        return pd.read_csv("temperature_log.csv")
    except FileNotFoundError:
        return pd.DataFrame(columns=["Timestamp", "Temperature"])

# Generate reading
if st.button("🔄 Take Temperature Reading"):
    temp = get_current_temperature()
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_data(time_now, temp)
    st.success(f"🌡️ Current Water Temperature: {temp} °C at {time_now}")

# Display historical data
st.markdown("### 📈 Temperature Readings History")
data = read_data()

if not data.empty:
    st.dataframe(data.tail(10), use_container_width=True)

    # Plotting
    st.markdown("### 📊 Temperature Trend Over Time")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(pd.to_datetime(data["Timestamp"]), data["Temperature"], marker='o', linestyle='-')
    ax.set_xlabel("Timestamp")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Water Temperature Over Time")
    plt.xticks(rotation=45)
    st.pyplot(fig)
else:
    st.warning("No temperature readings recorded yet.")
