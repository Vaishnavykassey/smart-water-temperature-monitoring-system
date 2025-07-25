import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import random
import time

# Page config
st.set_page_config(page_title="Smart Water Temperature Monitoring System", layout="centered")

# Title
st.markdown("## 💧 Smart Water Temperature Monitoring System")

# Start button
start = st.button("Start Monitoring")

# Lists to store data
temperature_data = []
timestamps = []

# Start monitoring when button is clicked
if start:
    placeholder = st.empty()
    chart_placeholder = st.empty()

    start_time = time.time()

    for i in range(100):  # Loop 100 times
        current_time = time.time() - start_time
        temperature = round(random.uniform(25.0, 35.0), 2)

        # Save data
        timestamps.append(round(current_time, 2))
        temperature_data.append(temperature)

        # Show current temperature
        with placeholder.container():
            st.metric(label="Current Water Temperature", value=f"{temperature} °C")

        # Plot graph
        fig, ax = plt.subplots()
        ax.plot(timestamps, temperature_data, color="blue", marker="o")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Temperature (°C)")
        ax.set_title("Water Temperature Over Time")
        plt.xticks(rotation=45)
        chart_placeholder.pyplot(fig)

        time.sleep(0.5)  # Simulate delay

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

