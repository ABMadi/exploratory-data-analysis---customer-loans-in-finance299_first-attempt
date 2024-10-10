# visualize_outliers.py

import pandas as pd
from plotter import Plotter
from data_transform_outliers import DataFrameTransformOutliers

# Load the transformed data
df = pd.read_csv('C:/Users/user/Desktop/my_test_repo/Finance Project/loan_payments_data_skewed_transformation.csv')

# Create an instance of DataFrameTransformOutliers
df_transformer = DataFrameTransformOutliers(df)

# List of columns to process (excluding id and member_id)
exclude_columns = ['id', 'member_id']
columns_to_process = [col for col in df.columns if col not in exclude_columns]

# Create an instance of Plotter
plotter = Plotter(df)

# Plot outliers and save visualizations
for column in columns_to_process:
    plotter.plot_outliers(column)
