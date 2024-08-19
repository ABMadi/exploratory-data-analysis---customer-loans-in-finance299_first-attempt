# Exploratory Data Analysis - Customer Loans in Finance

## Project Overview

This project involves performing exploratory data analysis (EDA) on customer loan data stored in an AWS RDS database. The primary goal is to extract, analyze, and visualize the data to gain insights into customer loans.

## Progress Update

### 1. Database Connection and Data Extraction

- **Created `RDSDatabaseConnector` class:** This class handles the connection to the AWS RDS database using credentials stored in a `credentials.yaml` file.
- **Implemented methods:**
  - `connect()`: Establishes a connection to the RDS database using `psycopg2`.
  - `create_engine()`: Initializes a SQLAlchemy engine for executing queries.
  - `get_loan_payments_data()`: Extracts the loan payments data from the `loan_payments` table and returns it as a Pandas DataFrame.

### 2. Data Storage and Retrieval

- **Implemented data saving functionality:**
  - The extracted data is saved locally as a CSV file using the `save_to_csv()` method. The file is saved at the specified path: `C:/Users/user/Desktop/my_test_repo/Finance Project/loan_payments_data.csv`.

- **Created a function to load data from CSV:**
  - Added `load_data_from_csv(file_path: str) -> pd.DataFrame` function to load the saved CSV data into a Pandas DataFrame for further analysis.

### 3. Future Work

- Perform exploratory data analysis (EDA) on the loaded data.
- Implement additional data transformation and visualization functions.
- Document insights and findings.

## Repository Structure

```plaintext
├── db_utils.py
├── credentials.yaml (Not included in the repository for security reasons)
├── README.md

How to Run the Project
Clone the repository to your local machine.
Set up your credentials.yaml file with the appropriate database credentials.
Run the db_utils.py script to extract, save, and load the loan payments data.

python db_utils.py

Prerequisites
Python 3.x
Pandas
SQLAlchemy
psycopg2
PyYAML
