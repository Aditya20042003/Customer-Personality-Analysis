# Customer Personality Analysis

Customer Personality Analysis is a machine learning-based customer segmentation and marketing analytics project built with Streamlit. It uses **K-Means clustering** and **PCA** to identify customer groups, analyze behavior patterns, and support targeted marketing strategies through an interactive web application.

## Project Overview

This project helps businesses understand customer behavior by grouping similar customers into meaningful segments.  
Users can enter customer details in the app and get the predicted cluster along with a visual representation of the customer’s position in the segmented space.

## Features

- Customer segmentation using **K-Means clustering**
- **PCA dimensionality reduction** for cluster visualization
- Interactive **Streamlit web app**
- Real-time customer cluster prediction
- Data visualization for customer behavior analysis
- Supports targeted marketing and business decision-making

## Tech Stack

- **Python**
- **Streamlit**
- **Scikit-learn**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Pickle**

## How It Works

1. The user enters customer profile details in the Streamlit app.
2. The input data is preprocessed and transformed using the saved scaler and PCA pipeline.
3. The trained K-Means model predicts the customer cluster.
4. The result is displayed along with a cluster visualization.
5. Businesses can use the output to understand customer segments and plan better marketing strategies.

## Project Structure

```bash
Customer-Personality-Analysis/
│
├── app.py
├── data/
├── models/
├── notebooks/
├── requirements.txt
└── README.md
```
---



