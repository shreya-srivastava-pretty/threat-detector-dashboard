
 Insider Threat Detection System 🔐

 Overview:

This project is a Machine Learning based Insider Threat Detection System that analyzes employee behavior and identifies potentially risky users.

The system uses the CERT Insider Threat Dataset and processes employee activity logs such as logon activity, device usage, and file access patterns to generate user risk scores.

The project also includes an interactive Streamlit dashboard for monitoring suspicious behavior.



Project Workflow:



CERT Insider Threat Dataset
|
↓
Data Preprocessing
|
↓
Feature Engineering
|
↓
Risk Score Generation
|
↓
Machine Learning Model
|
↓
Streamlit Dashboard





## Features

- Employee behavioral analysis
- Late login detection
- USB/device activity monitoring
- File access analysis
- User risk score calculation
- Risk level classification
- Machine learning based prediction
- Interactive dashboard
- Employee lookup
- Risk report download

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- Jupyter Notebook

---

## Machine Learning Model

The project uses a Random Forest Classifier to classify users based on their activity patterns.

The model analyzes engineered features such as:

- Late login frequency
- USB activity count
- File access count

and predicts whether a user shows suspicious behavior.

---

## Dashboard

The Streamlit dashboard provides:

- Total employee count
- High-risk user count
- Average risk score
- Top risky users
- Risk distribution visualization
- Individual employee analysis

---

## Dataset

Dataset used:

[CERT Insider Threat Dataset (r4.2)](https://www.kaggle.com/datasets/andrihjonior/cert-insider-threat-dataset-r4-2)

The dataset contains simulated employee activity logs including:

- Logon events
- Device usage
- File operations

---

## Installation

Clone the repository:

#bash
git clone <repository-link>


Install dependencies:

#bash
pip install -r requirements.txt




## Run the Dashboard

Run:

#bash
streamlit run app.py


The dashboard will open in your browser.



Project Structure:


insider-threat-detection/

│
├── app.py                  # Streamlit dashboard
├── firstproject.ipynb      # ML development notebook
├── features.csv            # Engineered dataset
├── insider_model.pkl       # Trained ML model
├── requirements.txt        # Dependencies
└── README.md               # Project documentation




Disclaimer:

This project is a proof-of-concept built for learning and demonstration purposes using a simulated dataset.



Author:

Shreya Srivastava


