📊 Project Delay Prediction using Linear Regression
🚀 Overview
This project predicts project delay (in days) based on various project-related features using a Linear Regression model.
The goal is to estimate potential delays early using historical data and help in better project planning and risk management.


🧠 Features Used
The model is trained using the following input features:
duration – Planned project duration
team_size – Number of team members
budget – Project budget
experience – Average team experience level
task_count – Number of tasks
requirement_changes – Number of requirement changes
risk – Risk score
Target variable:
delay_days – Actual delay in days


🛠 Tech Stack
Python
Pandas
Scikit-learn
NumPy
Pickle


📂 Project Structure
Regression-project/
│
├── data/
│   └── project_delay_dataset_1200_rows.csv
│
├── train.py
├── delay_model.pkl
└── README.md


⚙️ Installation
Clone the repository:
git clone <your-repo-url>
cd Regression-project
Install dependencies:
pip install pandas scikit-learn numpy

▶️ How to Run
Run the training script:
python train.py
The script will:
Split the dataset into train and test sets
Train a Linear Regression model
Evaluate performance using:
R² Score
MAE
RMSE
Save the trained model as:
delay_model.pkl

📈 Model Evaluation Metrics
The model is evaluated using:
🔹 R² Score
Measures how well the model explains variance in the target variable.
1.0 → Perfect fit
Closer to 1 → Better performance
🔹 MAE (Mean Absolute Error)
Average absolute prediction error in days.
🔹 RMSE (Root Mean Squared Error)
Penalizes large errors more heavily.
💾 Model Saving
The trained model is saved using pickle:
with open("delay_model.pkl", "wb") as f:
    pickle.dump(model, f)
You can later load it for predictions in a web app or API.
🎯 Future Improvements
Add Ridge / Lasso regression comparison
Feature importance analysis
Hyperparameter tuning
Deploy as Flask/FastAPI API
Build a frontend prediction dashboard
