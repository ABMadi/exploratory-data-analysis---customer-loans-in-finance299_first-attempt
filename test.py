import pandas as pd

# Load the transformed DataFrame
transformed_df_path = 'C:/Users/user/Desktop/my_test_repo/Finance Project/loan_payments_data_skewed_transformation.csv'
df_transformed = pd.read_csv(transformed_df_path)

# Calculate and print skewness of the transformed DataFrame
skewness = df_transformed.skew()
print("Skewness of Transformed DataFrame:")
print(skewness)
