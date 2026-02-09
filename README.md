# 📊 Project Delay Prediction using Linear Regression

---

## 🚀 Overview

This project predicts **project delay (in days)** using a Linear Regression model trained on historical project data.

The objective is to estimate potential delays early and support better project planning, budgeting, and risk management.

---

## 🧠 Problem Statement

Projects often get delayed due to multiple factors such as:

- Poor planning
- Team size mismatch
- Budget constraints
- Frequent requirement changes
- High project risk

This model learns patterns from past data and predicts expected delay in days.

---

## 📌 Features Used

| Feature | Description |
|----------|-------------|
| duration | Planned project duration |
| team_size | Number of team members |
| budget | Project budget |
| experience | Average team experience level |
| task_count | Total number of tasks |
| requirement_changes | Number of requirement modifications |
| risk | Project risk score |

Target Variable:
delay_days → Actual delay in days

---

## 🛠 Tech Stack

- Python
- Pandas
- Scikit-learn
- NumPy
- Pickle

---

## 📂 Project Structure

Regression-project/

│
├── data/
│   └── project_delay_dataset_1200_rows.csv
│
├── train.py
├── delay_model.pkl
└── README.md

---

## ⚙️ Installation

Clone the repository:

git clone <your-repo-url>
cd Regression-project

Install dependencies:

pip install pandas scikit-learn numpy

---

## ▶️ How to Run

python train.py

The script will:
- Split dataset into training and testing sets
- Train Linear Regression model
- Evaluate performance
- Save trained model as delay_model.pkl

---

## 📈 Model Evaluation Metrics

R² Score → Measures how well model explains variance  
MAE → Average prediction error in days  
RMSE → Penalizes larger errors

---

## 💾 Model Saving

The trained model is saved using pickle and can be reused for deployment.

---

## 🎯 Future Improvements

- Add Ridge and Lasso comparison
- Hyperparameter tuning
- Feature importance analysis
- Deploy as Flask/FastAPI app
- Build frontend dashboard

---

## 👨‍💻 Author

Bhanu Prasad  
Machine Learning Enthusiast | Backend Developer
