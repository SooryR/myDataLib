import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def _check_column_exists(df, column):
    """Helper function to check if column exists in dataframe.

    Raises:
        ValueError: If column doesn't exist.
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame.")


def plot_histogram(df, column, title="Histogram", xlabel=None, bins=10, color=None, ax=None):
    """Generates a histogram for a given column in a DataFrame.
    Args:
        df (pd.DataFrame): The DataFrame containing data.
        column (str): The column to plot the histogram for.
        title (str, optional): The title of the histogram. Defaults to "Histogram".
        xlabel (str, optional): The x-axis label. If None, the column name is used. Defaults to None.
        bins (int, optional): Number of bins for the histogram. Defaults to 10.
        color (str, optional): The color of the histogram bars.
        ax (matplotlib.axes.Axes, optional) : Matplotlib ax object to plot on.
    """
    _check_column_exists(df, column)
    if ax is None:
      plt.figure(figsize=(8, 6))
    sns.histplot(df[column], bins=bins, kde=True, color=color, ax=ax)
    plt.title(title) if ax is None else ax.set_title(title)
    plt.xlabel(xlabel if xlabel else column) if ax is None else ax.set_xlabel(xlabel if xlabel else column)
    plt.ylabel("Frequency") if ax is None else ax.set_ylabel("Frequency")
    if ax is None:
        plt.show()


def plot_scatter(df, x_col, y_col, title="Scatter Plot", xlabel=None, ylabel=None, color=None,ax=None,alpha=1):
    """Generates a scatter plot for two columns in a DataFrame.
    Args:
        df (pd.DataFrame): The DataFrame containing data.
        x_col (str): The column to plot on the x-axis.
        y_col (str): The column to plot on the y-axis.
        title (str, optional): The title of the scatter plot. Defaults to "Scatter Plot".
        xlabel (str, optional): The x-axis label. If None, the x_col name is used. Defaults to None.
        ylabel (str, optional): The y-axis label. If None, the y_col name is used. Defaults to None.
        color (str, optional): Color of the scatter points.
        ax (matplotlib.axes.Axes, optional) : Matplotlib ax object to plot on.
        alpha (float, optional): Transparency value of the points.
    """
    _check_column_exists(df, x_col)
    _check_column_exists(df, y_col)
    if ax is None:
      plt.figure(figsize=(8, 6))
    sns.scatterplot(x=x_col, y=y_col, data=df, color=color, ax=ax, alpha=alpha)
    plt.title(title) if ax is None else ax.set_title(title)
    plt.xlabel(xlabel if xlabel else x_col) if ax is None else ax.set_xlabel(xlabel if xlabel else x_col)
    plt.ylabel(ylabel if ylabel else y_col) if ax is None else ax.set_ylabel(ylabel if ylabel else y_col)
    if ax is None:
      plt.show()


def plot_boxplot(df, column, title="Box Plot", xlabel=None, color=None,ax=None):
    """Generates a box plot for a given column in a DataFrame.
    Args:
        df (pd.DataFrame): The DataFrame containing data.
        column (str): The column to plot the box plot for.
        title (str, optional): The title of the box plot. Defaults to "Box Plot".
        xlabel (str, optional): The y-axis label. If None, the column name is used. Defaults to None.
         color (str, optional): The color of the box plot.
        ax (matplotlib.axes.Axes, optional) : Matplotlib ax object to plot on.
    """
    _check_column_exists(df, column)
    if ax is None:
      plt.figure(figsize=(8, 6))
    sns.boxplot(y=column, data=df, color=color, ax=ax)
    plt.title(title) if ax is None else ax.set_title(title)
    plt.ylabel(xlabel if xlabel else column) if ax is None else ax.set_ylabel(xlabel if xlabel else column)
    if ax is None:
      plt.show()


def plot_correlation_matrix(df, title="Correlation Matrix",annot=True, cmap="coolwarm",ax=None):
    """Generates a heatmap of the correlation matrix.
    Args:
        df (pd.DataFrame): The DataFrame containing data.
        title (str, optional): The title of the correlation matrix plot. Defaults to "Correlation Matrix".
        annot (bool): if True, then the correlation value is displayed.
        cmap (str): The color scheme.
        ax (matplotlib.axes.Axes, optional) : Matplotlib ax object to plot on.
    """
    corr_matrix = df.corr()
    if ax is None:
      plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=annot, cmap=cmap, ax=ax)
    plt.title(title) if ax is None else ax.set_title(title)
    if ax is None:
      plt.show()


def plot_bar_chart(df, column, title="Bar Chart", xlabel=None, ylabel="Count", color=None,ax=None):
    """Creates a bar chart showing the counts of unique values in a column.
     Args:
        df (pd.DataFrame): The DataFrame containing data.
        column (str): The column to plot the bar chart for.
        title (str, optional): The title of the bar chart. Defaults to "Bar Chart".
        xlabel (str, optional): The x-axis label. If None, the column name is used. Defaults to None.
        ylabel (str, optional): The y-axis label. Defaults to "Count".
        color (str, optional): The color of the bars.
        ax (matplotlib.axes.Axes, optional) : Matplotlib ax object to plot on.
    """
    _check_column_exists(df, column)
    value_counts = df[column].value_counts()
    if ax is None:
      plt.figure(figsize=(10, 6))
    value_counts.plot(kind='bar', color=color, ax=ax)
    plt.title(title) if ax is None else ax.set_title(title)
    plt.xlabel(xlabel if xlabel else column) if ax is None else ax.set_xlabel(xlabel if xlabel else column)
    plt.ylabel(ylabel) if ax is None else ax.set_ylabel(ylabel)
    if ax is None:
      plt.xticks(rotation=45, ha="right")
      plt.tight_layout()
      plt.show()
    else:
      ax.tick_params(axis='x', rotation=45)

def plot_line_chart(df, x_col, y_col, title="Line Chart", xlabel=None, ylabel=None, color=None, ax=None, marker='o'):
    """Generates a line chart.
     Args:
        df (pd.DataFrame): The DataFrame containing data.
        x_col (str): The column to plot on the x-axis.
        y_col (str): The column to plot on the y-axis.
        title (str, optional): The title of the line chart. Defaults to "Line Chart".
        xlabel (str, optional): The x-axis label. If None, the x_col name is used. Defaults to None.
        ylabel (str, optional): The y-axis label. If None, the y_col name is used. Defaults to None.
        color (str, optional): Color of the line.
        ax (matplotlib.axes.Axes, optional) : Matplotlib ax object to plot on.
        marker (str, optional): Marker style
    """
    _check_column_exists(df, x_col)
    _check_column_exists(df, y_col)
    if ax is None:
      plt.figure(figsize=(8, 6))
    sns.lineplot(x=x_col, y=y_col, data=df, marker=marker, color=color, ax=ax)
    plt.title(title) if ax is None else ax.set_title(title)
    plt.xlabel(xlabel if xlabel else x_col) if ax is None else ax.set_xlabel(xlabel if xlabel else x_col)
    plt.ylabel(ylabel if ylabel else y_col) if ax is None else ax.set_ylabel(ylabel if ylabel else y_col)
    if ax is None:
        plt.show()

def plot_pie_chart(df, column, title="Pie Chart", labels=None, colors=None, ax=None, autopct='%1.1f%%'):
    """Creates a pie chart showing the distribution of values in a column.
     Args:
        df (pd.DataFrame): The DataFrame containing data.
        column (str): The column to plot the pie chart for.
        title (str, optional): The title of the pie chart. Defaults to "Pie Chart".
        labels (list, optional): Labels for the pie chart slices.
        colors (list, optional): Colors for the pie chart slices.
        ax (matplotlib.axes.Axes, optional) : Matplotlib ax object to plot on.
        autopct (str, optional): String for how values will be displayed.

    """
    _check_column_exists(df, column)
    value_counts = df[column].value_counts()
    if ax is None:
      plt.figure(figsize=(8,8))
    value_counts.plot(kind='pie', autopct=autopct, labels=labels, colors=colors, ax=ax)
    plt.title(title) if ax is None else ax.set_title(title)
    plt.ylabel('') if ax is None else ax.set_ylabel('')
    if ax is None:
      plt.show()

def plot_pair_plot(df, columns=None, title="Pair Plot", hue=None, palette=None, ax=None):
    """Generates a pair plot for the selected columns.

      Args:
        df (pd.DataFrame): The DataFrame containing data.
        columns (list, optional): List of columns to include in the pair plot.
        title (str, optional): The title of the pair plot. Defaults to "Pair Plot".
        hue (str, optional): Column name to color points by.
        palette (str, optional): The color palette to use.
         ax (matplotlib.axes.Axes, optional) : Matplotlib ax object to plot on.
    """
    if columns:
        for col in columns:
          _check_column_exists(df, col)
    else:
        columns = df.columns
    if ax is None:
       plot = sns.pairplot(df[columns], hue=hue, palette=palette)
    else:
       plot = sns.pairplot(df[columns], hue=hue, palette=palette, ax=ax)
    plot.fig.suptitle(title, y=1.02)
    if ax is None:
        plt.show()