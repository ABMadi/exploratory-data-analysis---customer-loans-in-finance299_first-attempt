import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

class Plotter:
    def __init__(self, df: pd.DataFrame, output_dir: str):
        self.df = df
        self.output_dir = output_dir

    def plot_missing_values(self, before_df: pd.DataFrame, after_df: pd.DataFrame):
        """
        Plot missing values before and after transformation.
        """
        plt.figure(figsize=(14, 6))

        # Plot missing values before transformation
        plt.subplot(1, 2, 1)
        sns.heatmap(before_df.isnull(), cbar=False, cmap='viridis')
        plt.title('Missing Values Before Transformation')

        # Plot missing values after transformation
        plt.subplot(1, 2, 2)
        sns.heatmap(after_df.isnull(), cbar=False, cmap='viridis')
        plt.title('Missing Values After Transformation')

        plt.tight_layout()
        plt.show()

    def plot_distribution(self, column: str):
        """
        Plot the distribution of a specific column.
        """
        plt.figure(figsize=(8, 4))

        # Plot the distribution of the specified column
        sns.histplot(self.df[column].dropna(), kde=True, bins=30)
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')

        plt.show()

    def plot_outliers(self, column: str, save_path: str = None):
        """
        Plot the boxplot for a specific column to visualize outliers.
        """
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=self.df[column])
        plt.title(f'Outliers in {column}')
        plt.xlabel(column)

        if save_path:
            plt.savefig(save_path)
            print(f"Plot saved to {save_path}")
        else:
            plt.show()
