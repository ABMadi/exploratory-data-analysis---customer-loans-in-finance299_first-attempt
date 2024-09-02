import pandas as pd

def load_data(file_path):
    """
    Load the DataFrame from the specified file path.
    """
    df = pd.read_csv(file_path)
    return df

def calculate_skewness(df, exclude_cols):
    """
    Calculate the skewness of numerical columns in a DataFrame, excluding specified columns.
    """
    numerical_cols = df.select_dtypes(include=['number']).columns
    # Exclude identifier columns
    numerical_cols = [col for col in numerical_cols if col not in exclude_cols]
    skewness = df[numerical_cols].skew()
    return skewness

# File path
file_path = 'C:/Users/user/Desktop/my_test_repo/Finance Project/loan_payments_data_final.csv'

# Load data
df = load_data(file_path)

# Exclude identifier columns
exclude_cols = ['id', 'member_id']

# Calculate skewness
skewness = calculate_skewness(df, exclude_cols)

# Print skewness values
print("Skewness (excluding identifier columns):")
print(skewness)
