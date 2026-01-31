import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(path):
    return pd.read_csv(path)

def basic_info(df):
    print(df.head())
    print(df.info())
    print(df.describe())

def plot_distributions(df):
    for col in df.select_dtypes(include=['int64', 'float64']).columns:
        plt.figure()
        sns.histplot(df[col], kde=True)
        plt.title(f'Distribution of {col}')
        plt.show()

if __name__ == "__main__":
    df = load_data("data/students_mental_health_survey.csv")
    basic_info(df)
    plot_distributions(df)
