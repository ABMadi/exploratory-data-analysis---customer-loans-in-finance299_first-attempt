import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
input_file_path = 'C:/Users/user/Desktop/my_test_repo/Finance Project/loan_payments_data_transformed_outliers.csv'
df = pd.read_csv(input_file_path)

# Drop 'id' and 'member_id' columns
exclude_columns = ['id', 'member_id']
df_filtered = df.drop(columns=exclude_columns, errors='ignore')

# Check data types of columns
print("Data types of columns:")
print(df_filtered.dtypes)

# Filter out non-numeric columns
numeric_df = df_filtered.select_dtypes(include=['float64', 'int64'])

# Compute the correlation matrix
correlation_matrix = numeric_df.corr()

# Plot the correlation matrix
plt.figure(figsize=(14, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix')
plt.tight_layout()

# Save the visualization
output_file_path = 'C:/Users/user/Desktop/my_test_repo/Finance Project/plots_transformed/correlation_matrix.png'
plt.savefig(output_file_path)
plt.show()

print(f"Correlation matrix plot saved to: {output_file_path}")
