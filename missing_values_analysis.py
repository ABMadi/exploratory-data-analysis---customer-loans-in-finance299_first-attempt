import pandas as pd
from dataframe_transform import DataFrameTransform
from plotter import Plotter

# Load the original DataFrame from the specified file path
file_path = 'C:/Users/user/Desktop/my_test_repo/Finance Project/loan_payments_data_cleaned.csv'
df = pd.read_csv(file_path)

# Verify that the DataFrame is loaded correctly
print("DataFrame Loaded:")
print(df.head())

# Function to analyze missing values
def analyze_missing_values(df: pd.DataFrame):
    print("Starting missing values analysis...")

    # Initialize the DataFrameTransform and Plotter
    df_transform = DataFrameTransform(df)
    plotter = Plotter(df)

    # Get a summary of missing values
    missing_summary = df_transform.missing_values_summary()
    print("Missing Values Summary:")
    print(missing_summary)
    
    # Visualize missing values
    plotter.plot_missing_percentage()
    
    # Print columns with missing values
    columns_with_missing = missing_summary[missing_summary['Missing Values'] > 0]
    if not columns_with_missing.empty:
        print("Columns with missing values:")
        print(columns_with_missing)
    else:
        print("No columns with missing values found.")

# Run the analysis on the loaded DataFrame
analyze_missing_values(df)
