import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def calculate_descriptive_statistics(df, columns=None):
    """
    Calculates descriptive statistics for specified columns in a DataFrame.
    Args:
        df (pd.DataFrame): The input DataFrame.
        columns (list, optional): List of columns to calculate statistics for.
        If None (default), statistics are calculated for all numerical columns.
    Returns:
        pd.DataFrame: A DataFrame containing descriptive statistics.
    """
    if columns is None:
      numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
      if not numeric_cols:
        print("No numerical columns to calculate statistics.")
        return None
      columns = numeric_cols

    desc_stats = df[columns].describe()
    return desc_stats

def calculate_correlation(df, method='pearson', columns=None):
    """
    Calculates the correlation matrix for specified columns in a DataFrame.
    Args:
      df (pd.DataFrame): The input DataFrame.
      method (str) : The type of correlation. Choose 'pearson', 'spearman', or 'kendall'.
      columns (list, optional): List of columns to calculate statistics for.
        If None (default), statistics are calculated for all numerical columns.
    Returns:
      pd.DataFrame: A DataFrame containing correlation matrix of selected columns
    """
    if columns is None:
      numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
      if not numeric_cols:
        print("No numerical columns to calculate correlation.")
        return None
      columns = numeric_cols
    corr_matrix = df[columns].corr(method=method)
    return corr_matrix

def perform_t_test(df, col1, col2, equal_var=True):
    """
    Performs an independent two-sample t-test for specified columns.

    Args:
        df (pd.DataFrame): The input DataFrame.
        col1 (str): The first column for the t-test.
        col2 (str): The second column for the t-test.
        equal_var (bool, optional): If True, performs a standard independent 2 sample t-test that assumes equal population variances. If False, performs Welch’s t-test that does not assume equal population variances.

    Returns:
        tuple: A tuple containing the t-statistic and p-value, or None on error.
    """
    try:
      t_statistic, p_value = stats.ttest_ind(df[col1], df[col2], equal_var=equal_var)
      return t_statistic, p_value
    except Exception as e:
      print(f"Error performing t-test: {e}")
      return None


def perform_anova(df, column, group_column):
  """Performs ANOVA for specified column and groups.
     Args:
        df (pd.DataFrame): The input DataFrame.
        column (str): The column to be tested.
        group_column (str) : Column with groups.
    Returns:
      tuple: A tuple containing the F-statistic and p-value, or None on error.
    """
  try:
    unique_groups = df[group_column].unique()
    groups = [df[column][df[group_column] == g] for g in unique_groups]
    f_statistic, p_value = stats.f_oneway(*groups)
    return f_statistic, p_value
  except Exception as e:
    print(f"Error performing ANOVA: {e}")
    return None


def perform_linear_regression(df, target, features, add_constant=True):
    """
    Performs a linear regression analysis.

    Args:
      df (pd.DataFrame): The input DataFrame.
      target (str): The target variable (dependent variable).
      features (list): The list of feature variables (independent variables).
      add_constant (bool): If True, add a constant term for intercept to the regression model.

    Returns:
        statsmodels.regression.linear_model.RegressionResultsWrapper: Regression results, or None on error.
    """
    try:
        X = df[features]
        if add_constant:
           X = sm.add_constant(X)
        y = df[target]
        model = sm.OLS(y, X)
        results = model.fit()
        return results
    except Exception as e:
        print(f"Error during linear regression: {e}")
        return None


def perform_kmeans_clustering(df, columns, n_clusters, random_state=42):
    """
    Performs K-Means clustering on specified columns.

    Args:
      df (pd.DataFrame): The input DataFrame.
      columns (list): Columns to perform clustering on
      n_clusters (int): The number of clusters to form.
      random_state (int): Random state for reproducibility
    Returns:
      tuple: The cluster labels and the silhouette score, or None on error.
    """
    try:
        kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=10)  #Added n_init to handle future update issue
        cluster_labels = kmeans.fit_predict(df[columns])
        silhouette = silhouette_score(df[columns],cluster_labels)
        return cluster_labels, silhouette
    except Exception as e:
       print(f"Error during k-means clustering: {e}")
       return None