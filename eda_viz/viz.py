"""Visualization module."""
import gc
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import warnings

from eda_viz.exceptions import InvalidDataError, \
    NonNumericTypeNotSupportedError, TypeNotSupportedError
from eda_viz.warnings import DifferentLengthWarning
# from tests.test_data import *

sns.set(style='whitegrid', palette='muted', font_scale=1.5)
FIG_SIZE = (14, 8)
ACCEPTED_GENERIC_TYPES = (pd.Series, np.ndarray, list)
DEFAULT_COLOR = '#4878d0'


def column_distribution(column, title='Class Distribution', xlabel='Class',
                        ylabel='Count', sort=True):
    """
    Displays distribution bar chart.

    :param column: pandas Series, numpy ndarray or list
    :param title: title of plot (str)
    :param xlabel: label of x-axis (str)
    :param ylabel: label of y-axis (str)
    :param sort: boolean, to sort the column distribution bars from highest to lowest
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
        if sort:
            count_classes = pd.value_counts(column, sort=True)
        else:
            count_classes = pd.value_counts(column)
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
        raise NonNumericTypeNotSupportedError('Column other than type numeric '
                                              'is not supported by this '
                                              'method. Make sure the type is '
                                              'numeric.')

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


def bar_plot(x, y, title='Bar Plot', xlabel='x-axis',
              ylabel='y-axis'):
    """
    Displays Bar plot.

    :param x: pandas Series, numpy ndarray or list for x-axis
    :param y: pandas Series, numpy ndarray or list for y-axis
    :param title: title of plot (str)
    :param xlabel: label of x-axis (str)
    :param ylabel: label of y-axis (str)
    :return: None
    :raise TypeNotSupportedError: if the column passed is one of pandas Series, numpy ndarray or list
    :raise NonNumericTypeNotSupportedError: if the column passed is non-numeric
    :raise InvalidDataError: if the data cannot be displayed
    :raise DifferentLengthWarning: when x and y data are of different lengths
    """
    if not isinstance(x, ACCEPTED_GENERIC_TYPES):
        raise TypeNotSupportedError(
            'Column of type {} is not supported by '
            'this method. Make sure the type is one '
            'of {}'.format(type(x), ', '.join(
                [str(t) for t in ACCEPTED_GENERIC_TYPES])))

    if not isinstance(y, ACCEPTED_GENERIC_TYPES):
        raise TypeNotSupportedError(
            'Column of type {} is not supported by '
            'this method. Make sure the type is one '
            'of {}'.format(type(y), ', '.join(
                [str(t) for t in ACCEPTED_GENERIC_TYPES])))

    x_pd_column = pd.Series(x)
    y_pd_column = pd.Series(y)
    if not pd.api.types.is_numeric_dtype(y_pd_column):
        raise NonNumericTypeNotSupportedError('Column other than type numeric '
                                              'is not supported for y-axis by '
                                              'this method. Make sure the type '
                                              'is numeric.')

    # Check if x and y have equal length
    if len(x_pd_column) != len(y_pd_column):
        warnings.warn('x and y have different lengths.', DifferentLengthWarning)

    try:
        plt.subplots(figsize=FIG_SIZE)
        sns.barplot(x_pd_column, y_pd_column, color=DEFAULT_COLOR)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()
        del x_pd_column
        del y_pd_column
        gc.collect()
    except TypeError:
        raise InvalidDataError('Something is wrong with the data provided. '
                               'Make sure there are some valid data values to '
                               'plot.')
    except ValueError:
        raise InvalidDataError('Something is wrong with the data provided. '
                               'Make sure there are some valid data values to '
                               'plot.')


# if __name__ == '__main__':
#     bar_plot(CATEGORICAL_LIST, DICTIONARY_LIST)
