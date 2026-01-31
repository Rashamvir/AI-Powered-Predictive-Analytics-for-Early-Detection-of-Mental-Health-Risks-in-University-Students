import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def create_risk_level(df):
    df = df.copy()

    df["Risk_Score"] = (
        df["Stress_Level"] +
        df["Depression_Score"] +
        df["Anxiety_Score"]
    )

    df["Risk_Level"] = pd.qcut(
        df["Risk_Score"],
        q=3,
        labels=["Low", "Medium", "High"]
    )

    df.drop("Risk_Score", axis=1, inplace=True)
    return df


def preprocess_data(df, training=False):
    """
    training=True  -> create Risk_Level
    training=False -> assume model will predict Risk_Level
    """
    df = df.copy()
    df = df.ffill()

    if training:
        df = create_risk_level(df)
        y = df["Risk_Level"]
        X = df.drop("Risk_Level", axis=1)
    else:
        y = None
        X = df

    # Encode categorical variables
    encoder = LabelEncoder()
    for col in X.select_dtypes(include="object").columns:
        X[col] = encoder.fit_transform(X[col])

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y
