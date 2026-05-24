import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("dataset/creditcard.csv")

# Check missing values
print("Missing Values:\n")
print(df.isnull().sum())

# Check duplicate rows
duplicates = df.duplicated().sum()

print(f"\nDuplicate Rows: {duplicates}")

# Remove duplicates if any
df = df.drop_duplicates()

# Feature Scaling
scaler = StandardScaler()

# Scale Amount and Time columns
df['scaled_amount'] = scaler.fit_transform(df['Amount'].values.reshape(-1,1))

df['scaled_time'] = scaler.fit_transform(df['Time'].values.reshape(-1,1))

# Drop original columns
df = df.drop(['Amount', 'Time'], axis=1)

# Reorder columns
scaled_amount = df['scaled_amount']
scaled_time = df['scaled_time']

df.drop(['scaled_amount', 'scaled_time'], axis=1, inplace=True)

df.insert(0, 'scaled_amount', scaled_amount)
df.insert(1, 'scaled_time', scaled_time)

# Final dataset info
print("\nPreprocessed Dataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:\n")
print(df.head())

# Save preprocessed dataset
df.to_csv("dataset/preprocessed_creditcard.csv", index=False)

print("\nPreprocessed dataset saved successfully.")