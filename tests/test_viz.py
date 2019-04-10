import mock
import numpy as np
import os
import pandas as pd
import pytest
import sys

from test_data import ALL_NONE_LIST,  CATEGORICAL_LIST, \
    CATEGORICAL_LIST_WITH_NONE, CATEGORICAL_MULTI_DIM_LIST, CATEGORICAL_NUMPY, \
    CATEGORICAL_PANDAS, CAT_AND_NUM_LIST, CAT_NUM_AND_DICT_LIST, EMPTY_LIST, \
    NUMERICAL_LIST, RANDOM_DICT, RANDOM_NUMBER, RANDOM_STRING, RANDOM_TITLE, \
    RANDOM_XLABEL, RANDOM_YLABEL
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from eda_viz.viz import column_distribution, histogram
from eda_viz.exception import  InvalidDataError, TypeNotSupportedError


# ======================================================================
# ======================================================================
# ======================================================================
# ======================================================================
# ======================================================================
@mock.patch("eda_viz.viz.plt")
@pytest.mark.parametrize('column', [
    CATEGORICAL_LIST, CATEGORICAL_NUMPY, CATEGORICAL_PANDAS, NUMERICAL_LIST,
    CAT_AND_NUM_LIST, CATEGORICAL_LIST_WITH_NONE
])
def test_column_distribution_default(mock_plt, column):
    """Test column_distribution() method with default parameters."""
    column_distribution(column)

    assert mock_plt.title.call_args_list[0][0][0] == 'Class Distribution'
    assert mock_plt.xlabel.call_args_list[0][0][0] == 'Class'
    assert mock_plt.ylabel.call_args_list[0][0][0] == 'Count'
    assert mock_plt.subplots.called
    assert mock_plt.show.called


@mock.patch("eda_viz.viz.plt")
@pytest.mark.parametrize('column, title, xlabel, ylabel', [
    (CATEGORICAL_LIST, RANDOM_TITLE, RANDOM_XLABEL, RANDOM_YLABEL),
    (CATEGORICAL_NUMPY, RANDOM_TITLE, RANDOM_XLABEL, RANDOM_YLABEL),
    (CATEGORICAL_PANDAS, RANDOM_TITLE, RANDOM_XLABEL, RANDOM_YLABEL)
])
def test_column_distribution_parameters(mock_plt, column, title, xlabel,
                                        ylabel):
    """Test column_distribution() method with all parameters."""
    column_distribution(column, title=title, xlabel=xlabel, ylabel=ylabel)

    assert mock_plt.title.call_args_list[0][0][0] == title
    assert mock_plt.xlabel.call_args_list[0][0][0] == xlabel
    assert mock_plt.ylabel.call_args_list[0][0][0] == ylabel
    assert mock_plt.subplots.called
    assert mock_plt.show.called


@mock.patch("eda_viz.viz.plt")
@pytest.mark.parametrize('column', [
    (RANDOM_STRING, RANDOM_NUMBER, RANDOM_DICT)
])
def test_column_distribution_type_not_supported_exception(mock_plt, column):
    """Test column_distribution() method when exception is raised."""
    with pytest.raises(TypeNotSupportedError):
        column_distribution(column)


@mock.patch("eda_viz.viz.plt")
@pytest.mark.parametrize('column', [
    EMPTY_LIST, ALL_NONE_LIST, CAT_NUM_AND_DICT_LIST, CATEGORICAL_MULTI_DIM_LIST
])
def test_column_distribution_invalid_data_exception(mock_plt, column):
    """Test column_distribution() method when exception is raised."""
    with pytest.raises(InvalidDataError):
        column_distribution(column)


# ======================================================================
# ======================================================================
# ======================================================================
# ======================================================================
# ======================================================================
# @mock.patch("eda_viz.viz.plt")
# @pytest.mark.parametrize('column', [
#     (['A', 'B', 'A', 'C', 'D', 'B', 'A']),
#     (np.array(['A', 'B', 'A', 'C', 'D', 'B', 'A'])),
#     (pd.Series(['A', 'B', 'A', 'C', 'D', 'B', 'A'])),
#     ([1, 2, 3, 4, 5, 6]),
#     ([1, 'abcd', 3, 'defg', 5, 'ghij'])
# ])
# def test_histogram_default(mock_plt, column):
#     """Test histogram() method with default parameters."""
#     histogram(column)
#
#     assert mock_plt.title.call_args_list[0][0][0] == 'Class Distribution'
#     assert mock_plt.xlabel.call_args_list[0][0][0] == 'Class'
#     assert mock_plt.ylabel.call_args_list[0][0][0] == 'Count'
#     assert mock_plt.subplots.called
#     assert mock_plt.show.called
