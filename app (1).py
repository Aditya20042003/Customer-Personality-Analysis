import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the trained KMeans model
with open('kmeans_model.pkl', 'rb') as f:
    kmeans = pickle.load(f)

st.title("Customer Segmentation Prediction")

# Input fields for all features used in training
income = st.number_input("Income", min_value=0)
age = st.number_input("Age", min_value=0, max_value=120)
recency = st.number_input("Recency", min_value=0)
total_spending = st.number_input("Total Spending", min_value=0)
kidhome = st.number_input("Number of Kids at Home", min_value=0)
teenhome = st.number_input("Number of Teens at Home", min_value=0)
marital_status = st.selectbox("Marital Status", ["Single", "Together", "Married", "Divorced", "Widow"])
education = st.selectbox("Education", ["Basic", "2n Cycle", "Graduation", "Master", "PhD"])

# Encoding for categorical variables (example, adjust as per your preprocessing)
marital_map = {"Single":0, "Together":1, "Married":2, "Divorced":3, "Widow":4}
education_map = {"Basic":0, "2n Cycle":1, "Graduation":2, "Master":3, "PhD":4}

marital_status_encoded = marital_map[marital_status]
education_encoded = education_map[education]

# Prepare input for prediction (order must match training)
X = np.array([[income, age, recency, total_spending, kidhome, teenhome, marital_status_encoded, education_encoded]])

if st.button("Predict Cluster"):
    cluster = kmeans.predict(X)
    st.success(f"Predicted Cluster: {cluster[0]}")
