# my_data_lib

A Python library for data cleaning, analysis, and visualization.

## Description

`myDataLib` is a versatile Python library designed to streamline the process of data preparation, exploration, and analysis. It provides a collection of functions for cleaning messy data, performing statistical analysis, and generating insightful visualizations. This library aims to simplify common data science tasks, making it easier to extract valuable information from your datasets.

## Features

-   **Data Loading and Export:**
    -   Supports importing data from CSV, JSON, Parquet, and Excel files.
    -   Exports data to CSV, JSON, Parquet, and Excel file formats.

-   **Data Cleaning:**
    -   Handles missing values using various strategies (mean, median, mode, constant fill, drop).
    -   Removes outliers using the Interquartile Range (IQR) method.
    -   Converts column types to int, float, datetime, etc.
    -   Normalizes numerical data using standard scaling and min-max scaling.
    -   Removes duplicate rows.
    -   Cleans text columns (lowercase, removes extra spaces, removes special characters).

-   **Data Analysis:**
    -   Calculates descriptive statistics (mean, median, standard deviation, etc.).
    -   Performs correlation analysis (Pearson, Spearman, Kendall).
    -   Performs t-tests and ANOVA for group comparisons.
    -   Conducts linear regression analysis.
    -   Performs K-means clustering.

-   **Data Visualization:**
    -   Creates histograms, scatter plots, box plots, bar charts, line plots, pie charts, and pair plots.
    -   Generates correlation matrix heatmaps.
    -   Offers customizable plot titles, labels, colors, and markers.

## Installation

You can install `myDataLib` directly from GitHub using `pip`:

```bash
pip install -e git+https://github.com/SooryR/myDataLib.git#egg=my_data_lib
```

import pandas as pd
from my_data_lib.io import import_data, export_data
from my_data_lib.cleaning import clean_data
from my_data_lib.analysis import *
from my_data_lib.visualization import *

# Load the data
file_path = 'complete.csv'
df = import_data(file_path)

# Data Cleaning
df = clean_data(
    file_path,
    strategy = 'median',
    convert_type = {'duration (seconds)':float, 'latitude':float,'longitude':float},
    text_cols=['city','state','country','shape','comments']
    )

# Data Analysis
print("\nDescriptive Statistics (numerical columns):\n",
      calculate_descriptive_statistics(df, columns = ['duration (seconds)','latitude','longitude']))

# Data Visualization
plot_histogram(df, column='duration (seconds)', title = "Distribution of Duration(sec)")

# Export cleaned data
export_data(df, 'cleaned_data.csv')

