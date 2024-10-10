import pandas as pd
import numpy as np

# Load the dataset
input_file_path = 'C:/Users/user/Desktop/my_test_repo/Finance Project/loan_payments_data_transformed_outliers.csv'
df = pd.read_csv(input_file_path)

# Drop 'id' and 'member_id' columns
exclude_columns = ['id', 'member_id']
df_filtered = df.drop(columns=exclude_columns, errors='ignore')

# Filter out non-numeric columns
numeric_df = df_filtered.select_dtypes(include=['float64', 'int64'])

# Compute the correlation matrix
correlation_matrix = numeric_df.corr()

# Define the threshold
threshold = 0.7  # Threshold for correlation

# Find pairs of correlated features
corr_pairs = correlation_matrix.abs().unstack().sort_values(ascending=False)
corr_pairs = corr_pairs[corr_pairs < 1]

# Identify columns to drop
to_drop = set()
for (i, j), corr in corr_pairs.items():
    if corr > threshold:
        to_drop.add(j)

# Drop highly correlated columns
df_reduced = df_filtered.drop(columns=to_drop, errors='ignore')

# Save the reduced dataset
output_file_path = 'C:/Users/user/Desktop/my_test_repo/Finance Project/loan_payments_data_reduced.csv'
df_reduced.to_csv(output_file_path, index=False)

print(f"Reduced dataset saved to: {output_file_path}")
print(f"Columns removed: {to_drop}")
