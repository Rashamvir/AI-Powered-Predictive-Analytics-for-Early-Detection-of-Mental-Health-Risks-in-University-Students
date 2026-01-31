# 🧠 AI-Powered Predictive Analytics for Early Detection of Mental Health Risks in University Students

A machine learning–driven approach to identify **student mental health risk levels (Low, Medium, High)** using behavioral, academic, and lifestyle data, enabling early intervention and informed decision-making.

---
## 🚀 Interactive Streamlit Demo

https://mental-health-risk-self-assessment-demo.streamlit.app/

This project includes a questionnaire-based Streamlit web application
that provides a **basic mental health risk self-assessment** using
AI-inspired rule-based logic.

⚠️ The deployed app is intended for **awareness and decision support only**
and does not provide medical diagnosis.

The underlying machine learning models are documented separately
for research and analysis purposes.

## 📍 Project Goal

This project builds a **predictive analytics system** that classifies university students into mental health risk categories using survey-based data.  
The primary objective is to support **early detection and preventive intervention** by universities, counselors, and wellness support teams through data-driven insights.

---

## ✅ Key Features

| Module | Description |
|------|------------|
| 🔍 Data Preprocessing | Handling missing values, encoding categorical data, feature scaling |
| 📊 Exploratory Data Analysis | Correlation heatmaps, feature distributions, risk-level analysis |
| 🤖 Multi-Model Training | Logistic Regression, Decision Tree, Random Forest, Gradient Boosting, XGBoost |
| ⚖️ Class Imbalance Handling | SMOTE (Synthetic Minority Oversampling Technique) |
| 🏆 Model Comparison | Accuracy, F1-score, confusion matrix, performance comparison |
| 🧠 Explainability | Feature importance analysis (optional SHAP support) |

---

## 📂 Dataset

- **Source:** Kaggle – Students Mental Health Assessments  
- **Dataset Link:** https://www.kaggle.com/datasets/sonia22222/students-mental-health-assessments  
- **Format:** CSV  
- **Type:** Structured survey data  
- **Target Variable:** Mental Health Risk Level (Low / Medium / High)

## 📊 Model Performance (After SMOTE Balancing)

| Model | Accuracy | F1 Score |
|--------|----------|----------|
| **Gradient Boosting** ⭐ | **0.404** | **0.375** |
| Random Forest | 0.403 | 0.371 |
| Logistic Regression | 0.384 | 0.380 |
| XGBoost | 0.382 | 0.366 |
| Decision Tree | 0.349 | 0.351 |

➡️ Gradient Boosting performed best overall.

### Features Include
- Academic pressure  
- Sleep patterns  
- Anxiety indicators  
- Lifestyle habits  
- Self-reported stress levels  

> ⚠️ **Ethical Note**  
> The dataset is anonymized and used strictly for academic and research purposes.  
> This project does not provide medical or clinical diagnoses.

---

## 🛠 Tech Stack Used

| Category | Tools / Technologies |
|--------|----------------------|
| Language | Python |
| Data Handling | Pandas, NumPy |
| Machine Learning | Scikit-learn, XGBoost |
| Imbalance Handling | imbalanced-learn (SMOTE) |
| Visualization | Matplotlib, Seaborn |
| Environment | Jupyter Notebook |
| Version Control | Git & GitHub |

## ▶️ How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/mental-health-risk-prediction.git
