# data_transform_outliers.py

print("Script execution started")

import pandas as pd
import numpy as np

class DataFrameTransformOutliers:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def identify_outliers(self, column: str) -> pd.Series:
        """
        Identify outliers in a column based on the IQR method.
        """
        Q1 = self.df[column].quantile(0.25)
        Q3 = self.df[column].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = self.df[(self.df[column] < lower_bound) | (self.df[column] > upper_bound)]
        print(f"Outliers identified in column '{column}': {len(outliers)} rows")
        return outliers

    def remove_outliers(self, column: str) -> None:
        """
        Remove outliers from a column based on the IQR method.
        """
        if self.df[column].dtype in [np.float64, np.float32, np.int64, np.int32]:
            Q1 = self.df[column].quantile(0.25)
            Q3 = self.df[column].quantile(0.75)
            IQR = Q3 - Q1

            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            initial_count = len(self.df)
            self.df = self.df[(self.df[column] >= lower_bound) & (self.df[column] <= upper_bound)]
            removed_count = initial_count - len(self.df)
            print(f"Removed {removed_count} outliers from column '{column}'")
        else:
            print(f"Skipping column '{column}' as it is not numeric.")

    def transform_outliers(self, column: str, method: str = 'cap') -> None:
        """
        Transform outliers in a column. Method can be 'cap' for capping.
        """
        if self.df[column].dtype in [np.float64, np.float32, np.int64, np.int32]:
            Q1 = self.df[column].quantile(0.25)
            Q3 = self.df[column].quantile(0.75)
            IQR = Q3 - Q1

            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            if method == 'cap':
                self.df[column] = np.where(self.df[column] > upper_bound, upper_bound,
                                           np.where(self.df[column] < lower_bound, lower_bound, self.df[column]))
                print(f"Capped outliers in column '{column}'")
            else:
                raise ValueError("Unsupported method. Use 'cap' for capping outliers.")
        else:
            print(f"Skipping column '{column}' as it is not numeric.")

input_file_path = 'C:/Users/user/Desktop/my_test_repo/Finance Project/loan_payments_data_skewed_transformation.csv'
print(f"Input file path: {input_file_path}")

# Example test section (add at the end of data_transform_outliers.py)

if __name__ == "__main__":
    print("Script execution started")

    # Load the dataset
    try:
        df = pd.read_csv(input_file_path)
        print(f"Data loaded successfully. Number of rows: {len(df)}")
    except FileNotFoundError:
        print(f"File not found: {input_file_path}")
        exit()

    # Create an instance of DataFrameTransformOutliers
    df_transformer = DataFrameTransformOutliers(df)

    # List of columns to process (excluding id and member_id)
    exclude_columns = ['id', 'member_id']
    columns_to_process = [col for col in df.columns if col not in exclude_columns]

    # Print the columns being processed
    print(f"Columns to process: {columns_to_process}")

    # Perform operations on each column
    for column in columns_to_process:
        print(f"Processing column: {column}")
        df_transformer.remove_outliers(column)
        print(f"Finished processing column: {column}")

    # Optionally save the transformed data if desired
    output_file_path = 'C:/Users/user/Desktop/my_test_repo/Finance Project/loan_payments_data_transformed_outliers.csv'
    df_transformer.df.to_csv(output_file_path, index=False)
    print(f"Transformed data saved to: {output_file_path}")
