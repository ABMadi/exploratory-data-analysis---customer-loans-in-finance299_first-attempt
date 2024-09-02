import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# File path to the transformed data
transformed_file_path = 'C:/Users/user/Desktop/my_test_repo/Finance Project/loan_payments_data_skewed_transformation.csv'

# Load the transformed DataFrame
df_transformed = pd.read_csv(transformed_file_path)

# List of columns to exclude from skewness visualization
exclude_columns = ['id', 'member_id']

# Exclude non-numeric columns and specified columns
numeric_df = df_transformed.drop(columns=exclude_columns).select_dtypes(include='number')

# Calculate skewness
skewness = numeric_df.skew()

# Plot the skewness
plt.figure(figsize=(10, 6))
sns.histplot(skewness, kde=True, bins=30)
plt.title('Distribution of Skewness After Transformation')
plt.xlabel('Skewness')
plt.ylabel('Frequency')
plt.show()

# Print skewness values for reference
print("Skewness of transformed columns:")
print(skewness)
