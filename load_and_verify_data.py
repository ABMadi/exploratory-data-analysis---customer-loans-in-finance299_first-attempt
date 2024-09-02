import pandas as pd

# Define the file path
file_path = 'C:/Users/user/Desktop/my_test_repo/Finance Project/loan_payments_data_final.csv'

# Load the data into a DataFrame
df_final = pd.read_csv(file_path)

# Verify the DataFrame is loaded correctly
print("DataFrame Loaded:")
print(df_final.head())

# Check DataFrame info
print("DataFrame Info:")
print(df_final.info())

# Check for missing values
print("Missing Values Summary:")
print(df_final.isnull().sum())

# Check for duplicate rows
print("Number of Duplicate Rows:")
print(df_final.duplicated().sum())
