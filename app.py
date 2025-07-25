import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("💧 Smart Water Monitoring Dashboard")

# Load data
df = pd.read_csv("data/water_data.csv", names=["Time", "Water Level (%)", "Flow Rate (L/min)"])

# Show latest status
latest = df.iloc[-1]
st.metric("Water Level", f"{latest['Water Level (%)']} %")
st.metric("Flow Rate", f"{latest['Flow Rate (L/min)']} L/min")

# Chart
st.subheader("Water Level Over Time")
fig, ax = plt.subplots()
ax.plot(df["Time"], df["Water Level (%)"], color='blue')
plt.xticks(rotation=45)
st.pyplot(fig)

# Alert
if latest["Water Level (%)"] < 20:
    st.error("⚠️ Alert: Water level is critically low!")

