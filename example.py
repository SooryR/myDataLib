import pandas as pd
from myDataLib.io import import_data, export_data
from myDataLib.cleaning import clean_data
from myDataLib.analysis import *
from myDataLib.visualization import *

# Load the data using your io.py module
file_path = 'complete.csv'
df = import_data(file_path)

if df is None:
    print("Failed to load data. Please check the file path.")
    exit()


# Data Cleaning
print("Original DataFrame:\n", df.head())
df = clean_data(
    file_path,
    strategy = 'median',
    convert_type = {'duration (seconds)':float, 'latitude':float,'longitude':float}, #convert numerical to float
    text_cols=['city','state','country','shape','comments'] #remove special characters
    )

if df is None:
    print("Failed to clean the data.")
    exit()

print("\nCleaned DataFrame:\n", df.head())
# Data Analysis
print("\nDescriptive Statistics (numerical columns):\n",
      calculate_descriptive_statistics(df, columns = ['duration (seconds)','latitude','longitude']))

corr_matrix = calculate_correlation(df, method='pearson', columns = ['duration (seconds)','latitude','longitude'])
print("\nCorrelation Matrix:\n", corr_matrix)


t_test_result = perform_t_test(df, 'latitude','longitude')
if t_test_result:
    t_statistic, p_value = t_test_result
    print(f"\nT-Test Results: \nT-Statistic: {t_statistic:.2f}, P-Value: {p_value:.3f}")

anova_results = perform_anova(df, column='duration (seconds)', group_column='shape')
if anova_results:
    f_statistic, p_value = anova_results
    print(f"\nANOVA Results: \nF-Statistic: {f_statistic:.2f}, P-Value: {p_value:.3f}")

# Linear Regression example: (only use numerical values)
# Since our dataset doesn't have direct numerical features, creating a numerical column.
df['duration_seconds'] = df['duration (seconds)'] #making sure the column is float
regression_results = perform_linear_regression(df, target='duration_seconds', features=['latitude', 'longitude'])
if regression_results:
    print("\nLinear Regression Results:\n", regression_results.summary())


# K-Means Clustering Example (using locations):
cluster_labels, silhouette = perform_kmeans_clustering(df, columns = ['latitude','longitude'], n_clusters = 5)
if cluster_labels is not None:
    print("\nCluster Labels:\n", cluster_labels)
    print(f"\nSilhouette Score: {silhouette:.3f}")
    df['location_cluster'] = cluster_labels


# Data Visualization:

#Plot histogram
plot_histogram(df, column='duration (seconds)', title = "Distribution of Duration(sec)")
#plot boxplot
plot_boxplot(df, column = 'duration (seconds)', title = "Distribution of Duration (sec)")
#Scatterplot between location points
plot_scatter(df, x_col = 'longitude', y_col = 'latitude', title = "Location Data")
# bar chart for shape.
plot_bar_chart(df, column='shape', title="Distribution of UFO Shapes")
#Line chart (not that useful in this data set, good example though)
plot_line_chart(df.sort_values(by = 'datetime'), x_col = 'datetime', y_col = 'duration (seconds)',
                title="Duration Over Time", marker='.')
#plot correlation matrix
plot_correlation_matrix(df[['duration (seconds)','latitude','longitude']], title = "Correlation Matrix")
#plot pie chart
plot_pie_chart(df, column = 'country', title = "UFO sighting by Country")
#pair plot.
plot_pair_plot(df, columns=['duration (seconds)','latitude','longitude'], hue = 'location_cluster')

# Export Clean Data
output_file = 'cleaned_complete_data.csv'
export_result = export_data(df, output_file)
if export_result:
    print(f"\nCleaned data exported to: {output_file}")