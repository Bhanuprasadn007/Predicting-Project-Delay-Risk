import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Load dataset
df = pd.read_csv("/Users/bhanuprasadn/Documents/Regression project/data/project_delay_dataset_1200_rows.csv")

X = df[['duration','team_size','budget','experience',
        'task_count','requirement_changes','risk']]
y = df['delay_days']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
print(f"R² Score (Accuracy): {r2:.4f}")

# Save model
with open("delay_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved successfully")
