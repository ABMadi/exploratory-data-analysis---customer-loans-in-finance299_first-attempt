import pandas as pd
from scipy import stats

def transform_skewed_columns(df, exclude_cols=None):
    if exclude_cols is None:
        exclude_cols = []

    # Exclude non-numeric columns from skewness calculation
    numeric_df = df.drop(columns=exclude_cols).select_dtypes(include='number')

    # Identify skewed columns (skewness > 0.5 or < -0.5)
    skewness = numeric_df.skew()
    skewed_cols = skewness[abs(skewness) > 0.5].index

    for col in skewed_cols:
        # Shift data to be positive if necessary
        if df[col].min() <= 0:
            shift_value = abs(df[col].min()) + 1  # Shift to make all values positive
            df[col] = df[col] + shift_value
        
        # Check for remaining zero values and handle them
        if (df[col] <= 0).any():
            df[col] = df[col] + 1  # Shift again if there are still non-positive values

        # Apply Box-Cox transformation
        df[col], _ = stats.boxcox(df[col])
    
    return df

# File paths
input_file_path = 'C:/Users/user/Desktop/my_test_repo/Finance Project/loan_payments_data_final.csv'
output_file_path = 'C:/Users/user/Desktop/my_test_repo/Finance Project/loan_payments_data_skewed_transformation.csv'

# Load the DataFrame
df = pd.read_csv(input_file_path)

# List of columns to exclude from transformation
exclude_columns = ['id', 'member_id']

# Transform skewed columns
df_transformed = transform_skewed_columns(df, exclude_cols=exclude_columns)

# Save the transformed DataFrame
df_transformed.to_csv(output_file_path, index=False)
print(f"Transformed data saved to {output_file_path}")
