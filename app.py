import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import random
import time

st.set_page_config(page_title="Smart Water Temperature Monitor", layout="wide")

st.title("💧 Smart Water Temperature Monitoring System")

# Initialize or get existing data
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Time (s)", "Temperature (°C)"])

# Function to simulate temperature
def get_temperature():
    return round(random.uniform(15, 35), 2)

# Button to start monitoring
if st.button("Start Monitoring"):
    for i in range(1, 101):
        temp = get_temperature()
        new_row = {"Time (s)": i, "Temperature (°C)": temp}
        st.session_state.data = pd.concat([st.session_state.data, pd.DataFrame([new_row])], ignore_index=True)

        st.metric("Current Water Temperature", f"{temp} °C")

        fig, ax = plt.subplots()
        ax.plot(st.session_state.data["Time (s)"], st.session_state.data["Temperature (°C)"], color="blue")
               ax.set_xlabel("Time (s)")
        ax.set_ylabel("Temperature (°C)")
        ax.set_title("Water Temperature Over Time")
        st.pyplot(fig)

        time.sleep(0.1)

        plt.xticks(rotation=45)
        st.pyplot(fig)

        # Alert
        if latest["Water Level (%)"] < 20:
            st.error("⚠️ Alert: Water level is critically low!")
r level is critically low!")

