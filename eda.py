import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Function to ensure the plots directory exists
def ensure_plots_folder():
    if not os.path.exists("plots"):
        os.makedirs("plots")

def perform_eda(file_path):
    # Ensure plots folder exists
    ensure_plots_folder()

    # Load dataset
    df = pd.read_csv(file_path)

    # Example 1: Churn Distribution
    sns.countplot(x='Churn', data=df)
    plt.title("Churn Distribution")
    plt.savefig("plots/churn_distribution.png")  # Save plot
    plt.close()

    # Example 2: Churn vs. Tenure
    sns.boxplot(x='Churn', y='tenure', data=df)
    plt.title("Churn vs. Tenure")
    plt.savefig("plots/churn_vs_tenure.png")  # Save plot
    plt.close()

    # Example 3: Correlation Heatmap
    # Select only numeric columns
    numeric_columns = df.select_dtypes(include=["number"])
    corr = numeric_columns.corr()

    # Plot the correlation heatmap
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.savefig("plots/correlation_heatmap.png")  # Save plot
    plt.close()

    print("EDA plots saved in the 'plots/' folder!")

if __name__ == "__main__":
    file_path = './data/Telco-Customer-Churn.csv'
    perform_eda(file_path)
