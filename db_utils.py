# db_utils.py

import pandas as pd
from sqlalchemy import create_engine
import psycopg2
from psycopg2 import OperationalError

class RDSDatabaseConnector:
    def __init__(self, credentials: dict):
        self.host = credentials.get('RDS_HOST')
        self.user = credentials.get('RDS_USER')
        self.password = credentials.get('RDS_PASSWORD')
        self.database = credentials.get('RDS_DATABASE')
        self.port = credentials.get('RDS_PORT', 5432)

        self.connection = None
        self.engine = None
        self.connect()
        self.create_engine()

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                dbname=self.database,
                port=self.port
            )
            print("Database connection established.")
        except OperationalError as e:
            print(f"An error occurred: {e}")
            self.connection = None

    def create_engine(self):
        try:
            db_url = f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
            self.engine = create_engine(db_url)
            print("SQLAlchemy engine created.")
        except Exception as e:
            print(f"An error occurred while creating the engine: {e}")

    def get_loan_payments_data(self) -> pd.DataFrame:
        query = "SELECT * FROM loan_payments;"
        try:
            df = pd.read_sql_query(query, self.engine)
            return df
        except Exception as e:
            print(f"An error occurred while executing the query: {e}")
            return pd.DataFrame()

    def save_to_csv(self, dataframe: pd.DataFrame, file_name: str) -> None:
        try:
            file_path = f"C:/Users/user/Desktop/my_test_repo/Finance Project/{file_name}"
            dataframe.to_csv(file_path, index=False)
            print(f"Data saved to {file_path}.")
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")

def load_data_from_csv(file_path: str) -> pd.DataFrame:
    """
    Load data from a CSV file into a Pandas DataFrame.

    :param file_path: The path to the CSV file.
    :return: DataFrame containing the loaded data.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}.")
        return df
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
        return pd.DataFrame()  # Return an empty DataFrame if the file is not found
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on other errors

# Main check
if __name__ == "__main__":
    from load_credentials import load_credentials
    
    creds = load_credentials('credentials.yaml')
    db_connector = RDSDatabaseConnector(credentials=creds)
    loan_payments_df = db_connector.get_loan_payments_data()
    db_connector.save_to_csv(loan_payments_df, 'loan_payments_data.csv')
    
    # Load the data back from the saved CSV
    loaded_df = load_data_from_csv("C:/Users/user/Desktop/my_test_repo/Finance Project/loan_payments_data.csv")
    print("Data extraction, saving, and re-loading complete.")
    print(loaded_df.head())

# Load the CSV file
file_path = "C:/Users/user/Desktop/my_test_repo/Finance Project/loan_payments_data.csv"
df = pd.read_csv(file_path)


class DataTransform:
    def __init__(self, df):
        self.df = df
    
    def transform_dates(self, date_columns):
        """Convert date columns to datetime and retain only month and year."""
        self.df[date_columns] = self.df[date_columns].apply(pd.to_datetime, format='%b-%y', errors='coerce')
        self.df[date_columns] = self.df[date_columns].apply(lambda x: x.dt.to_period('M'))
    
    def rename_and_transform_term_column(self):
        """Rename the 'term' column to 'term_in_months' and convert it to numeric."""
        self.df.rename(columns={'term': 'term_in_months'}, inplace=True)
        
        # Extract numeric part of the term and handle NaN values
        self.df['term_in_months'] = self.df['term_in_months'].str.extract(r'(\d+)')
        self.df['term_in_months'] = pd.to_numeric(self.df['term_in_months'], errors='coerce')

    def convert_to_categorical(self, categorical_columns):
        """Convert specified columns to categorical data types."""
        self.df[categorical_columns] = self.df[categorical_columns].astype('category')
    
    def apply_transformations(self):
        """Apply all transformations."""
        # List of date columns to be transformed
        date_columns = ['issue_date', 'earliest_credit_line', 'last_payment_date', 'next_payment_date', 'last_credit_pull_date']
        
        # Apply transformations
        self.transform_dates(date_columns)
        self.rename_and_transform_term_column()
        
        # Example categorical columns (update based on your dataset)
        categorical_columns = ['grade', 'sub_grade', 'home_ownership', 'verification_status', 'loan_status', 'purpose']
        self.convert_to_categorical(categorical_columns)
        
        return self.df

# Instantiate the DataTransform class
transformer = DataTransform(df)

# Apply all transformations
df_transformed = transformer.apply_transformations()

# Save the cleaned DataFrame to a new CSV file
cleaned_file_path = "C:/Users/user/Desktop/my_test_repo/Finance Project/loan_payments_data_cleaned.csv"
df.to_csv(cleaned_file_path, index=False)
