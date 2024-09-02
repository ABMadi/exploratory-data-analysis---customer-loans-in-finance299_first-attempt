import pandas as pd
import numpy as np

class DataFrameTransform:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def missing_values_summary(self):
        """
        Calculate the number of missing values and their percentage.
        """
        missing_count = self.df.isnull().sum()
        missing_percentage = (missing_count / len(self.df)) * 100
        
        missing_summary = pd.DataFrame({
            'Missing Values': missing_count,
            'Percentage': missing_percentage
        })
        
        missing_summary = missing_summary[missing_summary['Missing Values'] > 0]
        
        return missing_summary

    def drop_columns_with_high_missing(self, threshold=50):
        """
        Drop columns with missing values exceeding the given threshold percentage.
        """
        missing_percentage = self.df.isnull().mean() * 100
        cols_to_drop = missing_percentage[missing_percentage > threshold].index
        
        if not cols_to_drop.empty:
            print(f"Dropping columns with more than {threshold}% missing values: {list(cols_to_drop)}")
            self.df = self.df.drop(columns=cols_to_drop)
        else:
            print("No columns to drop.")
        
        return self.df

    def impute_missing_values(self, strategy='mean'):
        """
        Impute missing values in numerical columns.
        
        Parameters:
        strategy (str): The imputation strategy ('mean' or 'median'). Default is 'mean'.
        
        Returns:
        pd.DataFrame: DataFrame with missing values imputed.
        """
        if strategy not in ['mean', 'median']:
            raise ValueError("Strategy must be 'mean' or 'median'")
        
        # Impute numerical columns
        numerical_cols = self.df.select_dtypes(include=['number']).columns
        for col in numerical_cols:
            if self.df[col].isnull().any():
                if strategy == 'mean':
                    self.df[col] = self.df[col].fillna(self.df[col].mean())
                elif strategy == 'median':
                    self.df[col] = self.df[col].fillna(self.df[col].median())
        
        # Impute categorical columns with mode
        categorical_cols = self.df.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            if self.df[col].isnull().any():
                self.df[col] = self.df[col].fillna(self.df[col].mode()[0])

        return self.df

    def transform_employment_length(self):
        """
        Transform the 'employment_length' column to numeric values.
        """
        def transform_employment_length(value):
            if pd.isna(value):
                return np.nan
            value = str(value)  # Ensure the value is a string
            if '10+' in value:
                return 10
            elif '1 year' in value:
                return 1
            elif 'less than 1 year' in value:
                return 0
            else:
                return int(value.split()[0])
        
        self.df['employment_length'] = self.df['employment_length'].apply(transform_employment_length)

