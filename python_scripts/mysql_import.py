import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import os

# -----------------------------
# Load Dataset
# -----------------------------

# Dataset path
dataset_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "dataset",
    "preprocessed_creditcard.csv"
)

print(f"Loading dataset from: {dataset_path}")

# Read CSV
df = pd.read_csv(dataset_path)

# Display dataset shape
print("\nDataset Shape:")
print(df.shape)

# -----------------------------
# MySQL Connection
# -----------------------------

# Replace with your MySQL password
MYSQL_PASSWORD = "teju"

# Create SQLAlchemy engine
engine = create_engine(
    f"mysql+pymysql://root:{MYSQL_PASSWORD}@localhost/fraud_detection",
    connect_args={"connect_timeout": 10}
)

# -----------------------------
# Import Dataset into MySQL
# -----------------------------

try:

    print("\nImporting dataset into MySQL...")

    # Import dataframe into MySQL
    df.to_sql(
        name='preprocessed_creditcard',
        con=engine,
        if_exists='replace',
        index=False,
        chunksize=1000,
        method='multi'
    )

    print("\nDataset imported successfully into MySQL.")

except SQLAlchemyError as e:

    print("\nError importing dataset into MySQL:")
    print(e)

    print("\nCheck:")
    print("1. MySQL server is running")
    print("2. Password is correct")
    print("3. Database 'fraud_detection' exists")

# -----------------------------
# Verify Import
# -----------------------------

try:

    query = "SELECT COUNT(*) AS total_rows FROM preprocessed_creditcard"

    result = pd.read_sql(query, engine)

    print("\nRows Imported into MySQL:")
    print(result)

except Exception as e:

    print("\nError verifying import:")
    print(e)