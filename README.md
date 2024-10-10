# Exploratory Data Analysis - Customer Loans in Finance

## Project Overview

This project involves performing **Exploratory Data Analysis (EDA)** on customer loan data stored in an AWS RDS database. The goal is to extract, analyze, and visualize the data to gain insights into customer loans, with a focus on identifying outliers, handling correlations, and improving data quality through transformations.

## 1. Database Connection and Data Extraction

- **`RDSDatabaseConnector` class:**
  - Manages the connection to the AWS RDS database using credentials stored in `credentials.yaml`.
  - Key methods:
    - `connect()`: Establishes a connection to the RDS database using `psycopg2`.
    - `create_engine()`: Initializes a SQLAlchemy engine for running SQL queries.
    - `get_loan_payments_data()`: Extracts loan payment data from the `loan_payments` table and returns it as a Pandas DataFrame.

- **Data Saving:**
  - Extracted data is saved locally as a CSV file using the `save_to_csv()` method.
  - The file is saved at:  
    `C:/Users/user/Desktop/my_test_repo/Finance Project/loan_payments_data.csv`.

- **Loading Data from CSV:**
  - `load_data_from_csv(file_path: str) -> pd.DataFrame`: This function loads the saved CSV file into a Pandas DataFrame for further analysis.

## 2. Data Transformation and Cleaning

- **Outlier Detection & Removal:**
  - Outliers in loan-related columns are identified using the Interquartile Range (IQR) method.
  - A custom class `DataFrameTransformOutliers` was created to:
    - Identify outliers.
    - Remove outliers based on a threshold.
    - Optionally, cap outliers within the upper and lower bounds to retain more data.

- **Highly Correlated Columns:**
  - A correlation matrix was generated, and columns with correlations higher than 0.7 were identified.
  - These highly correlated columns were removed to mitigate multicollinearity, improving model interpretability.

## 3. Visualization

- **Outlier Visualization:**
  - The `Plotter` class was designed to generate box plots of each column to visualize outliers.
  - Pre-transformation and post-transformation visualizations were saved in the respective directories:
    - `plots/`: Contains plots before outlier removal.
    - `plots_transformed/`: Contains plots after outlier removal.

- **Correlation Visualization:**
  - The correlation matrix was visualized and saved as a heatmap to identify highly correlated columns.
  - The visualization was saved in the project folder for future reference.

## 4. Future Work

- Continue performing EDA to uncover more insights from the data.
- Refine data transformation methods, including handling missing values and scaling.
- Build and evaluate machine learning models using the cleaned dataset.

## Repository Structure

```plaintext
├── db_utils.py                # Handles database connection and data extraction.
├── data_transform_outliers.py  # Outlier transformation and removal logic.
├── visualize_outliers.py       # Visualizes outliers before transformation.
├── visualize_correlation_matrix.py  # Visualizes the correlation matrix.
├── plots/                      # Directory for pre-transformation visualizations.
├── plots_transformed/           # Directory for post-transformation visualizations.
├── loan_payments_data.csv      # Extracted loan payments data (CSV).
├── loan_payments_data_transformed_outliers.csv # Transformed data (outliers removed).
├── README.md                   # Project overview and progress.
