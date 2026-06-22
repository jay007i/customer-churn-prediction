# 📞 Customer Churn Prediction using XGBoost & SHAP

## 📌 Project Overview

Customer churn is one of the biggest challenges faced by subscription-based businesses. This project predicts whether a customer is likely to leave a company based on their service usage, contract details, and billing information.

The project follows a complete Machine Learning workflow from data preprocessing to deployment using Streamlit.

---

## 🎯 Objectives

* Predict customer churn accurately
* Handle class imbalance using XGBoost
* Explain model predictions using SHAP
* Deploy the model using Streamlit
* Build an end-to-end machine learning pipeline

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* XGBoost
* SHAP
* Joblib
* Streamlit

---

## 📂 Project Structure

```text
customer_churn_project/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── customer_churn_prediction.ipynb
│
├── models/
│   └── xgboost_churn_model.pkl
│
├── app/
│   └── streamlit_app.py
│
├── requirements.txt
│
└── README.md
```

---

## 🔄 Machine Learning Workflow

### 1. Data Collection

Customer telecom dataset containing:

* Gender
* Senior Citizen
* Tenure
* Monthly Charges
* Total Charges
* Contract Type
* Internet Service
* Tech Support
* Online Security
* Churn

---

### 2. Data Cleaning

* Missing value handling
* Data type correction
* Feature selection

---

### 3. Exploratory Data Analysis (EDA)

Visualized:

* Churn distribution
* Contract impact on churn
* Internet service impact
* Tech support influence
* Online security influence

---

### 4. Feature Engineering

* One-Hot Encoding
* Dummy Variable Creation
* Numerical Feature Scaling
* Train-Test Split

---

### 5. Baseline Model

Implemented Logistic Regression as the baseline model.

Metrics:

* Accuracy
* Precision
* Recall
* F1 Score

---

### 6. Advanced Model

Implemented XGBoost Classifier.

Benefits:

* Handles non-linear relationships
* Better performance on tabular data
* Handles class imbalance
* High predictive accuracy

---

### 7. Model Explainability

Implemented SHAP (SHapley Additive Explanations).

SHAP helps explain:

* Why a customer is predicted to churn
* Which features increase churn risk
* Which features reduce churn risk

---

### 8. Model Saving

Saved trained model using Joblib.

```python
joblib.dump(model, "xgboost_churn_model.pkl")
```

---

### 9. Deployment

Built an interactive Streamlit web application.

Users can:

* Enter customer information
* Predict churn probability
* Understand churn drivers

---

## 📊 Evaluation Metrics

The following metrics were used:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

## 📈 Feature Importance

Important churn-driving factors include:

* Monthly Charges
* Tenure
* Contract Type
* Tech Support
* Online Security

---

## 🚀 How to Run

### Clone Repository

```bash
git clone https://github.com/yourusername/customer-churn-prediction.git
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run app/streamlit_app.py
```

---

## 📷 Future Improvements

* Hyperparameter Tuning
* Cross Validation
* Probability Calibration
* Customer Retention Recommendation System
* Cloud Deployment

---

## Business Benefits
- Identify customers at risk
- Improve customer retention
- Reduce revenue loss
- Support targeted marketing campaigns
- Enhance customer satisfaction

## 👨‍💻 Author

Jay Kumbhani

Bachelor of Engineering (Information Technology)

Aspiring Data Scientist

```
```
