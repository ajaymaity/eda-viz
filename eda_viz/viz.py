import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from eda_viz.exception import TypeNotSupportedError

sns.set(style='whitegrid', palette='muted', font_scale=1.5)
FIG_SIZE = (14, 8)
ACCEPTED_TYPES = [pd.Series, np.ndarray, list]


def column_distribution(column, title='Class Distribution', xlabel='Class',
                        ylabel='Count'):
    """
    Displays distribution bar chart.

    :param column: pandas Series, numpy ndarray or list
    :param title: title of plot (str)
    :param xlabel: label of x-axis (str)
    :param ylabel: label of y-axis (str)
    :return: None
    :raise TypeNotSupportedError: if the column passed is one of pandas Series,
    numpy ndarray or list
    """
    if type(column) not in ACCEPTED_TYPES:
        raise TypeNotSupportedError('column of type {} is not supported by '
                                    'this method. Make sure the type is one '
                                    'of {}'.format(type(column),
                                                   ', '.join([str(t) for t in
                                                              ACCEPTED_TYPES])))

    plt.subplots(figsize=FIG_SIZE)
    count_classes = pd.value_counts(column, sort=True)
    count_classes.plot(kind='bar', rot=0)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def sum_ab(a, b):
    return a + b


if __name__ == '__main__':
    df = pd.DataFrame({
        'col1': ['ajay', 'nikita', 'ajay', 'sonia', 'sumeet', 'nikita', 'ajay'],
        'col2': [1, 2, 3, 4, 5, 6, 7]
    })
    column_distribution(df['col1'])