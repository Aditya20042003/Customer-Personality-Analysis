import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------- PAGE CONFIG ----------------
st.set_page_config(layout="wide")

# ---------------- LOAD MODELS ----------------
kmeans = pickle.load(open("models/kmeans_model.pkl","rb"))
scaler = pickle.load(open("models/scaler.pkl","rb"))
pca = pickle.load(open("models/pca.pkl","rb"))

# Load PCA visualization data
pca_df = pd.read_csv("data/pca_data.csv")

st.title("Customer Segmentation Dashboard")

# ---------------- LAYOUT ----------------
left, right = st.columns([1,2], gap="large")

# =====================================================
# LEFT PANEL INPUTS
# =====================================================
with left:

    st.markdown("## Customer Inputs")

    income = st.number_input("Income", min_value=0)
    age = st.number_input("Age", min_value=0, max_value=120)
    recency = st.number_input("Recency", min_value=0)
    total_spending = st.number_input("Total Spending", min_value=0)

    kidhome = st.number_input("Kids at Home", min_value=0)
    teenhome = st.number_input("Teens at Home", min_value=0)

    marital_status = st.selectbox(
        "Marital Status",
        ["Single","Together","Married","Divorced","Widow"]
    )

    education = st.selectbox(
        "Education",
        ["Basic","2n Cycle","Graduation","Master","PhD"]
    )

    predict = st.button("Predict Cluster")

# =====================================================
# RIGHT PANEL OUTPUT
# =====================================================
with right:

    if predict:

        # ---------- ENCODING ----------
        marital_map = {
            "Single":0,
            "Together":1,
            "Married":2,
            "Divorced":3,
            "Widow":4
        }

        education_map = {
            "Basic":0,
            "2n Cycle":1,
            "Graduation":2,
            "Master":3,
            "PhD":4
        }

        marital_encoded = marital_map[marital_status]
        education_encoded = education_map[education]

        # ---------- INPUT VECTOR ----------
        X = np.array([[
            income,
            age,
            recency,
            total_spending,
            kidhome,
            teenhome,
            marital_encoded,
            education_encoded
        ]])

        # =================================================
        # PIPELINE 1: USER INPUT → SCALER → KMEANS
        # =================================================
        X_scaled = scaler.transform(X)
        cluster = int(kmeans.predict(X_scaled)[0])

        # =================================================
        # PIPELINE 2: USER INPUT → SCALER → PCA
        # =================================================
        user_pca = pca.transform(X_scaled)

        # ---------- RESULT TABLE ----------
        result_df = pd.DataFrame({
            "Income":[income],
            "Age":[age],
            "Recency":[recency],
            "Total Spending":[total_spending],
            "KidHome":[kidhome],
            "TeenHome":[teenhome],
            "Marital Status":[marital_status],
            "Education":[education],
            "Predicted Cluster":[cluster]
        })

        st.subheader("Prediction Result")
        st.dataframe(result_df, use_container_width=True)

        # ---------- CLUSTER VISUALIZATION ----------
        st.subheader("Cluster Visualization (PCA)")

        fig, ax = plt.subplots(figsize=(8,5))

        sns.scatterplot(
            data=pca_df,
            x="PC1",
            y="PC2",
            hue="Cluster",
            palette="Set1",
            alpha=0.8,
            ax=ax
        )

        # Highlight user point
        ax.scatter(
            user_pca[0][0],
            user_pca[0][1],
            color="black",
            s=300,
            marker="X",
            label=f"New Customer (Cluster {cluster})"
        )

        ax.set_title("K-Means Clusters Visualized using PCA")

        ax.legend()

        st.pyplot(fig)