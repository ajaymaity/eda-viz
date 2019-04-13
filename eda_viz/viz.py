import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from pandas.api.types import is_string_dtype
from eda_viz.exception import InvalidDataError, StringTypeNotSupportedError, \
    TypeNotSupportedError

sns.set(style='whitegrid', palette='muted', font_scale=1.5)
FIG_SIZE = (14, 8)
ACCEPTED_GENERIC_TYPES = [pd.Series, np.ndarray, list]


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
    if type(column) not in ACCEPTED_GENERIC_TYPES:
        raise TypeNotSupportedError('Column of type {} is not supported by '
                                    'this method. Make sure the type is one '
                                    'of {}'.format(type(column),
                                                   ', '.join([str(t) for t in
                                                              ACCEPTED_GENERIC_TYPES])))

    try:
        plt.subplots(figsize=FIG_SIZE)
        count_classes = pd.value_counts(column, sort=True)
        count_classes.plot(kind='bar', rot=0)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()
    except TypeError:
        raise InvalidDataError('Something is wrong with the data provided. '
                               'Make sure there are some valid data values to '
                               'plot.')


# def histogram(column, title='Histogram', xlabel='Class Bins',
#                         ylabel='Count'):
#     """
#     Displays histogram.
#
#     :param column: pandas Series, numpy ndarray or list
#     :param title: title of plot (str)
#     :param xlabel: label of x-axis (str)
#     :param ylabel: label of y-axis (str)
#     :return: None
#     :raise TypeNotSupportedError: if the column passed is one of pandas Series,
#     numpy ndarray or list
#     """
#     if type(column) not in ACCEPTED_GENERIC_TYPES:
#         raise TypeNotSupportedError('Column of type {} is not supported by '
#                                     'this method. Make sure the type is one '
#                                     'of {}'.format(type(column),
#                                                    ', '.join([str(t) for t in
#                                                               ACCEPTED_GENERIC_TYPES])))
#
#     if is_string_dtype(column):
#         raise StringTypeNotSupportedError('Column of type string is not '
#                                           'supported by this method. Make sure '
#                                           'the type is numeric.')
#
#     try:
#         plt.subplots(figsize=FIG_SIZE)
#         pd_column = pd.Series(column)
#         pd_column.plot(kind='hist', rot=0)
#         plt.title(title)
#         plt.xlabel(xlabel)
#         plt.ylabel(ylabel)
#         plt.show()
#     except TypeError:
#         raise InvalidDataError('Something is wrong with the data provided. '
#                                'Make sure there are some valid data values to '
#                                'plot.')


# if __name__ == '__main__':
#     df = pd.DataFrame({
#         'col1': ['ajay', 'nikita', 'ajay', 'sonia', 'sumeet',
#                  'nikita', 'ajay'],
#         'col2': [1, 2, 1, 4, 1, 2, 7],
#         'col3': [1, 'A', 1, 4, 1, 'B', 7],
#         'col4': [None] * 7,
#         'col5': ['A', None, 'A', 'C', 'D', 'B', None],
#         'col6': [1, 'A', {'a': 1}, 3, 4, 5, 6],
#         'col7': [[1, 3], 2, 1, 4, 1, 2, 7]
#     })
    # column_distribution(df['col7'])
    # histogram(df['col1'])
