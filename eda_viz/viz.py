import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pylab import rcParams

from eda_viz.exception import PandasSeriesError

sns.set(style='whitegrid', palette='muted', font_scale=1.5)
rcParams['figure.figsize'] = 14, 8


def column_distribution(column, title='Class Distribution', xlabel='Class',
                        ylabel='Count'):
    """
    Displays distribution bar chart of pandas Series.

    :param column: pandas Series
    :param title: title of plot (str)
    :param xlabel: label of x-axis (str)
    :param ylabel: label of y-axis (str)
    :return: None
    :raise PandasSeriesError: if the column passed is not a pandas Series
    """
    # column must be a pandas Series
    if not isinstance(column, pd.Series):
        raise PandasSeriesError('column is not a Pandas Series.')

    # TODO: Add support for list passed as argument instead of pandas Series

    count_classes = pd.value_counts(column, sort=True)
    count_classes.plot(kind='bar', rot=0)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
