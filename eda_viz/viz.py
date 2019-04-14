"""Visualization module."""
import gc
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from eda_viz.exception import InvalidDataError, \
    NonNumericTypeNotSupportedError, TypeNotSupportedError
# from tests.test_data import *

sns.set(style='whitegrid', palette='muted', font_scale=1.5)
FIG_SIZE = (14, 8)
ACCEPTED_GENERIC_TYPES = (pd.Series, np.ndarray, list)


def column_distribution(column, title='Class Distribution', xlabel='Class',
                        ylabel='Count'):
    """
    Displays distribution bar chart.

    :param column: pandas Series, numpy ndarray or list
    :param title: title of plot (str)
    :param xlabel: label of x-axis (str)
    :param ylabel: label of y-axis (str)
    :return: None
    :raise TypeNotSupportedError: if the column passed is one of pandas Series, numpy ndarray or list
    :raise InvalidDataError: if the data cannot be displayed
    """
    if not isinstance(column, ACCEPTED_GENERIC_TYPES):
        raise TypeNotSupportedError(
            'Column of type {} is not supported by '
            'this method. Make sure the type is one '
            'of {}'.format(type(column), ', '.join(
                [str(t) for t in ACCEPTED_GENERIC_TYPES])))

    try:
        plt.subplots(figsize=FIG_SIZE)
        count_classes = pd.value_counts(column, sort=True)
        count_classes.plot(kind='bar', rot=0)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()
        del count_classes
        gc.collect()
    except TypeError:
        raise InvalidDataError('Something is wrong with the data provided. '
                               'Make sure there are some valid data values to '
                               'plot.')


def histogram(column, title='Histogram', xlabel='Class Bins',
              ylabel='Count'):
    """
    Displays histogram.

    :param column: pandas Series, numpy ndarray or list
    :param title: title of plot (str)
    :param xlabel: label of x-axis (str)
    :param ylabel: label of y-axis (str)
    :return: None
    :raise TypeNotSupportedError: if the column passed is one of pandas Series, numpy ndarray or list
    :raise NonNumericTypeNotSupportedError: if the column passed is non-numeric
    :raise InvalidDataError: if the data cannot be displayed
    """
    if not isinstance(column, ACCEPTED_GENERIC_TYPES):
        raise TypeNotSupportedError(
            'Column of type {} is not supported by '
            'this method. Make sure the type is one '
            'of {}'.format(type(column), ', '.join(
                [str(t) for t in ACCEPTED_GENERIC_TYPES])))

    pd_column = pd.Series(column)
    if not pd.api.types.is_numeric_dtype(pd_column):
        raise NonNumericTypeNotSupportedError('Column of type string is not '
                                              'supported by this method. Make '
                                              'sure the type is numeric.')

    try:
        plt.subplots(figsize=FIG_SIZE)
        pd_column.plot(kind='hist', rot=0)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()
        del pd_column
        gc.collect()
    except TypeError:
        raise InvalidDataError('Something is wrong with the data provided. '
                               'Make sure there are some valid data values to '
                               'plot.')


# if __name__ == '__main__':
    # histogram(ALL_NONE_LIST)
