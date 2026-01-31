import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def preprocess_data(df):
    df = df.copy()

    # Handle missing values
    df.fillna(method='ffill', inplace=True)

    # Encode categorical columns
    encoder = LabelEncoder()
    for col in df.select_dtypes(include='object').columns:
        df[col] = encoder.fit_transform(df[col])

    # Separate features and target
    X = df.drop('Depression', axis=1)
    y = df['Depression']

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y

if __name__ == "__main__":
    df = pd.read_csv("data/students_mental_health_survey.csv")
    X, y = preprocess_data(df)
