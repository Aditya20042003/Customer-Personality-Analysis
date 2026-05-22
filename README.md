# Customer Personality Analysis

Customer Personality Analysis is a Machine Learning-based customer segmentation and marketing analytics project built using Streamlit. The project uses K-Means Clustering and PCA (Principal Component Analysis) to identify customer groups, analyze purchasing behavior, and support targeted marketing strategies through an interactive web application.

---

## Project Overview

This project helps businesses understand customer behavior by grouping customers into meaningful segments based on spending patterns, income, age, recency, family structure, education, and marital status.

Users can enter customer details in the Streamlit app and get real-time customer cluster predictions along with PCA-based visualizations.

---

## Features

- Customer Segmentation using K-Means Clustering
- PCA-based Dimensionality Reduction
- Interactive Streamlit Dashboard
- Real-time Customer Cluster Prediction
- Customer Behavior Analysis and Visualization
- Business Insights for Targeted Marketing

---

## Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Pickle

---

## How It Works

1. User enters customer profile details in the Streamlit app.
2. Input data is preprocessed using the saved scaler and PCA pipeline.
3. The trained K-Means model predicts the customer cluster.
4. The app displays the predicted segment and visualization.
5. Businesses can use the output for marketing and customer analysis.

---

## Project Structure

```bash
Customer-Personality-Analysis/
│
├── app.py
├── app (1).py
├── data/
├── models/
├── notebooks/
├── requirements.txt
├── README.md
└── README.md.txt
```

---

## Input Features Used

- Income
- Age
- Recency
- Total Spending
- Kids at Home
- Teens at Home
- Marital Status
- Education

---

## Output

- Predicted Customer Cluster
- PCA-based Cluster Visualization
- Interactive Prediction Results

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Aditya20042003/Customer-Personality-Analysis.git
```

Move into the project directory:

```bash
cd Customer-Personality-Analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

---

## Use Case

This project helps businesses perform customer segmentation, understand customer behavior, identify hidden patterns, and improve marketing strategies through data-driven insights.

---

## Future Improvements

- Add more advanced clustering algorithms
- Improve dashboard UI/UX
- Add customer cluster profiling
- Generate downloadable business reports
- Deploy on Streamlit Cloud

---

## Author

### Aditya Poonia
