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
