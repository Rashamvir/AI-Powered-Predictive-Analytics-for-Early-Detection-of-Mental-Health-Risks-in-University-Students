import pandas as pd
import joblib

from src.preprocessing import preprocess_data
from src.model_training import train_models

# Load dataset
df = pd.read_csv("data/students_mental_health_survey.csv")

# Preprocess data
X, y = preprocess_data(df,  training=True)

# Train models
models, X_test, y_test = train_models(X, y)

# Select best model manually (Gradient Boosting preferred)
best_model = models.get("Gradient Boosting")

# Save the model
joblib.dump(best_model, "model.pkl")

print("✅ Model trained and saved as model.pkl")
