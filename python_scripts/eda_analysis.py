import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load dataset
df = pd.read_csv("../dataset/creditcard.csv")

# Fraud percentage
fraud_percent = (df['Class'].value_counts()[1] / len(df)) * 100

print(f"Fraud Percentage: {fraud_percent:.4f}%")

# Transaction Amount Distribution
plt.figure(figsize=(8,5))

sns.histplot(df[df['Amount'] < 2000]['Amount'], bins=50)

plt.title("Transaction Amount Distribution")
plt.xlabel("Amount")
plt.ylabel("Frequency")

plt.show()

# Fraud vs Genuine Amount Comparison
plt.figure(figsize=(8,5))

sns.boxplot(x='Class', y='Amount', data=df)

plt.xticks([0,1], ['Genuine', 'Fraud'])

plt.title("Fraud vs Genuine Transaction Amounts")

plt.show()

# Correlation Heatmap

plt.figure(figsize=(16,10))

correlation = df.corr()

sns.heatmap(
    correlation,
    cmap='coolwarm',
    annot=False
)

plt.title("Correlation Heatmap")

plt.show()