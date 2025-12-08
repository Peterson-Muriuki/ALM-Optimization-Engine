import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("ALM Optimization Engine Dashboard")

# Load outputs
summary_file = "outputs/reports/alm_summary.txt"
with open(summary_file, "r") as f:
    summary = f.read()

st.subheader("ALM Summary")
st.text(summary)

# Example plot
weights = [0.4, 0.3, 0.3]  # Replace with actual from main.py if dynamic
labels = ["Asset A", "Asset B", "Asset C"]
fig, ax = plt.subplots()
ax.pie(weights, labels=labels, autopct='%1.1f%%')
ax.set_title("Optimal Asset Allocation")
st.pyplot(fig)
