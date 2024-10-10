import pandas as pd

class DataFrameInfo:
    def __init__(self, df: pd.DataFrame):
        """
        Initialize with a DataFrame.
        
        Parameters:
        df (pd.DataFrame): The DataFrame to analyze.
        """
        self.df = df

    def describe_columns(self):
        """ 
        Describe all columns in the DataFrame to check their data types and summary statistics.
        """
        return self.df.describe(include='all')
    
    def extract_statistics(self):
        """
        Extract statistical values (mean, median, std) for numerical columns.
        
        Returns:
        pd.DataFrame: A DataFrame containing the mean, median, and standard deviation.
        """
        stats = pd.DataFrame({
            'mean': self.df.mean(),
            'median': self.df.median(),
            'std': self.df.std()
        })
        return stats
    
    def count_distinct(self):
        """
        Count distinct values in each categorical column.
        
        Returns:
        pd.Series: A series with the count of unique values for each categorical column.
        """
        categorical_cols = self.df.select_dtypes(include=['object', 'category']).columns
        return self.df[categorical_cols].nunique()
    
    def dataframe_shape(self):
        """
        Print the shape of the DataFrame.
        
        Returns:
        tuple: The shape of the DataFrame (rows, columns).
        """
        return self.df.shape
    
    def null_value_counts(self, percentage=False):
        """
        Generate a count or percentage count of NULL values in each column.
        
        Parameters:
        percentage (bool): If True, return the percentage of NULL values. If False, return the count of NULL values.
        
        Returns:
        pd.Series: A series with the count/percentage of NULL values for each column.
        """
        if percentage:
            return self.df.isnull().mean() * 100
        else:
            return self.df.isnull().sum()
    
    def get_numeric_columns(self):
        """
        Retrieve the list of numeric columns in the DataFrame.
        
        Returns:
        list: List of column names that are numeric.
        """
        return self.df.select_dtypes(include=['number']).columns.tolist()

    def get_categorical_columns(self):
        """
        Retrieve the list of categorical columns in the DataFrame.
        
        Returns:
        list: List of column names that are categorical.
        """
        return self.df.select_dtypes(include=['object', 'category']).columns.tolist()
    
    def value_counts_for_column(self, column_name):
        """
        Get the value counts of a specific column.
        
        Parameters:
        column_name (str): The name of the column.
        
        Returns:
        pd.Series: A series with the counts of unique values in the specified column.
        """
        return self.df[column_name].value_counts()

# Example usage:
# df = pd.read_csv('your_dataset.csv')
# df_info = DataFrameInfo(df)
# print(df_info.describe_columns())
# print(df_info.extract_statistics())
# print(df_info.count_distinct())
# print(df_info.dataframe_shape())
# print(df_info.null_value_counts(percentage=True))
# print(df_info.get_numeric_columns())
# print(df_info.get_categorical_columns())
# print(df_info.value_counts_for_column('some_column'))
