import pandas as pd

# Load the dataset
df = pd.read_csv('Invoice.csv')

# Display basic info and first few rows
print("Shape of data:", df.shape)
print(df.info())
print("\nFirst 5 rows:")
print(df.head())