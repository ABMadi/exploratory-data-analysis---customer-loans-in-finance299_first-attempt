# visualize_outliers_after_transformation.py

import pandas as pd
import os
from plotter import Plotter

# Load the transformed dataset
input_file_path = 'C:/Users/user/Desktop/my_test_repo/Finance Project/loan_payments_data_transformed_outliers.csv'
df = pd.read_csv(input_file_path)
print(f"Data loaded successfully from {input_file_path}. Number of rows: {len(df)}")

# Create the output directory for plots
output_dir = 'C:/Users/user/Desktop/my_test_repo/Finance Project/plots_transformed'
os.makedirs(output_dir, exist_ok=True)
print(f"Output directory is set to: {output_dir}")

# Create an instance of the Plotter class with the output directory
plotter = Plotter(df, output_dir)

# List of columns to visualize (excluding id and member_id)
exclude_columns = ['id', 'member_id']
columns_to_visualize = [col for col in df.columns if col not in exclude_columns]

# Visualize each column to check for outliers
for column in columns_to_visualize:
    print(f"Visualizing column: {column}")
    save_path = f"{output_dir}/{column}_outliers_transformed.png"
    plotter.plot_outliers(column, save_path=save_path)
    print(f"Visualization saved for column: {column} at {save_path}")

print("Outlier visualization completed.")
