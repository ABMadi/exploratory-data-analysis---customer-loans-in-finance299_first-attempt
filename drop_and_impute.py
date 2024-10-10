import pandas as pd
from dataframe_transform import DataFrameTransform
from plotter import Plotter

def decide_imputation_strategy(df):
    """
    Automatically decide between mean or median for imputing numerical columns.
    """
    numerical_cols = df.select_dtypes(include=['number']).columns
    strategies = {}
    
    for col in numerical_cols:
        # Check the distribution of the column
        mean = df[col].mean()
        median = df[col].median()
        skewness = df[col].skew()
        
        # Decide strategy based on skewness
        if abs(skewness) > 1:  # Highly skewed
            strategies[col] = 'median'
        else:
            strategies[col] = 'mean'
    
    return strategies

# Load the cleaned DataFrame
file_path = 'C:/Users/user/Desktop/my_test_repo/Finance Project/loan_payments_data_cleaned.csv'
df = pd.read_csv(file_path)

# Initialize the DataFrameTransform
df_transform = DataFrameTransform(df)

# Print the summary of missing values before any transformations
print("Missing Values Summary Before Transformation:")
print(df_transform.missing_values_summary())

# Print columns before dropping
print("Columns Before Dropping High Missing Value Columns:")
print(df_transform.df.columns)

# Drop columns with more than 50% missing values
df_transform.drop_columns_with_high_missing(threshold=50)

# Verify that columns were dropped
print("Columns After Dropping High Missing Value Columns:")
print(df_transform.df.columns)

# Apply the employment length transformation
df_transform.transform_employment_length()

# Print the summary of missing values after dropping columns
print("Missing Values Summary After Dropping High Missing Value Columns and Transformation:")
print(df_transform.missing_values_summary())

# Automatically decide the imputation strategy
strategies = decide_imputation_strategy(df_transform.df)
print(f"Decided Imputation Strategies: {strategies}")

# Impute remaining missing values
# You should consider applying different strategies to different columns if needed
for col, strategy in strategies.items():
    df_transform.impute_missing_values(strategy=strategy)

# Verify the DataFrame after imputation
print("DataFrame after Imputation:")
print(df_transform.df.head())
print(df_transform.df.shape)

# Save the imputed DataFrame to a new CSV file
imputed_file_path = 'C:/Users/user/Desktop/my_test_repo/Finance Project/loan_payments_data_imputed.csv'
df_transform.df.to_csv(imputed_file_path, index=False)
print(f"Imputed DataFrame saved to {imputed_file_path}")

# Initialize the Plotter
plotter = Plotter(df)

# Plot missing values before and after imputation
before_df = pd.read_csv(file_path)
plotter.plot_missing_values(before_df=before_df, after_df=df_transform.df)
