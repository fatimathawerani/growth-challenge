import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(page_title="Growth Inset Project", layout="wide")

# Title
st.title("Growth Inset Analysis")

# User Input Section
st.sidebar.header("Input Growth Data")
n = st.sidebar.number_input("Number of Data Points", min_value=5, max_value=100, value=20)

dates = pd.date_range(start="2023-01-01", periods=n, freq="M")
growth_values = np.cumsum(np.random.randn(n) * 10) + 100  # Simulated growth data

data = pd.DataFrame({"Date": dates, "Growth": growth_values})

# Display Data Table
st.subheader("Growth Data Table")
st.dataframe(data)

# Line Chart Visualization
st.subheader("Growth Trend Over Time")
st.line_chart(data.set_index("Date"))

# Insights & Analysis
st.subheader("Analysis & Insights")
st.write("- The chart shows growth trends over time.")
st.write("- Identify patterns and fluctuations for better decision-making.")
st.write("- Customize inputs using the sidebar for different data simulations.")

# Matplotlib Custom Plot
fig, ax = plt.subplots()
ax.plot(data["Date"], data["Growth"], marker='o', linestyle='-', color='b')
ax.set_title("Growth Inset Visualization")
ax.set_xlabel("Date")
ax.set_ylabel("Growth Value")
plt.xticks(rotation=45)
st.pyplot(fig)

# Footer
st.write("\n*Powered by Streamlit* 🚀")
