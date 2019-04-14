"""Test column_distribution() method in eda_viz.viz module."""
import mock
import os
import pytest
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from tests.test_data import CATEGORICAL_LIST, CATEGORICAL_NUMPY, \
    CATEGORICAL_PANDAS_SERIES, CATEGORICAL_PANDAS_DF, \
    CATEGORICAL_LIST_WITH_NONE, CATEGORICAL_MULTI_DIM_LIST, \
    CATEGORICAL_MULTI_DIM_LIST_2, NUMERICAL_LIST, NUMERICAL_NUMPY, \
    NUMERICAL_PANDAS_SERIES, NUMERICAL_PANDAS_DF, NUMERICAL_LIST_WITH_NONE, \
    NUMERICAL_MULTI_DIM_LIST, NUMERICAL_MULTI_DIM_LIST_2, \
    CATEGORICAL_AND_NUMERICAL_LIST, \
    CATEGORICAL_NUMERICAL_AND_DICTIONARY_LIST, DICTIONARY_LIST, \
    RANDOM_NUMBER, RANDOM_STRING, RANDOM_DICTIONARY, EMPTY_STRING, NONE, \
    NUMPY_NAN, NUMPY_INF, EMPTY_LIST, ALL_NONE_LIST, RANDOM_TITLE, \
    RANDOM_XLABEL, RANDOM_YLABEL  # noqa: E402
from eda_viz.viz import column_distribution  # noqa: E402
from eda_viz.exceptions import InvalidDataError, \
    TypeNotSupportedError  # noqa: E402


class TestColumnDistribution(object):
    """Test column_distribtion() method."""

    @mock.patch("eda_viz.viz.plt")
    @pytest.mark.parametrize('column', [
        CATEGORICAL_LIST, CATEGORICAL_NUMPY, CATEGORICAL_PANDAS_SERIES,
        CATEGORICAL_LIST_WITH_NONE, NUMERICAL_LIST, NUMERICAL_NUMPY,
        NUMERICAL_PANDAS_SERIES, NUMERICAL_LIST_WITH_NONE,
        CATEGORICAL_AND_NUMERICAL_LIST
    ])
    def test_column_distribution_default(self, mock_plt, column):
        """Test column_distribution() method with default parameters."""
        column_distribution(column)

        assert mock_plt.title.call_args_list[0][0][0] == 'Class Distribution'
        assert mock_plt.xlabel.call_args_list[0][0][0] == 'Class'
        assert mock_plt.ylabel.call_args_list[0][0][0] == 'Count'
        assert mock_plt.subplots.called
        assert mock_plt.show.called

    @pytest.mark.parametrize('column', [
        CATEGORICAL_PANDAS_DF, NUMERICAL_PANDAS_DF, RANDOM_NUMBER,
        RANDOM_STRING, RANDOM_DICTIONARY, EMPTY_STRING, NONE, NUMPY_NAN,
        NUMPY_INF
    ])
    def test_column_distribution_type_not_supported_exception(self, column):
        """Test column_distribution() method when exception is raised."""
        with pytest.raises(TypeNotSupportedError):
            column_distribution(column)

    @pytest.mark.parametrize('column', [
        CATEGORICAL_MULTI_DIM_LIST, CATEGORICAL_MULTI_DIM_LIST_2,
        NUMERICAL_MULTI_DIM_LIST, NUMERICAL_MULTI_DIM_LIST_2,
        CATEGORICAL_NUMERICAL_AND_DICTIONARY_LIST, DICTIONARY_LIST, EMPTY_LIST,
        ALL_NONE_LIST
    ])
    def test_column_distribution_invalid_data_exception(self, column):
        """Test column_distribution() method when exception is raised."""
        with pytest.raises(InvalidDataError):
            column_distribution(column)

    @mock.patch("eda_viz.viz.plt")
    @pytest.mark.parametrize('column, title, xlabel, ylabel', [
        (CATEGORICAL_LIST, RANDOM_TITLE, RANDOM_XLABEL, RANDOM_YLABEL),
    ])
    def test_column_distribution_parameters(self, mock_plt, column, title,
                                            xlabel, ylabel):
        """Test column_distribution() method with all parameters."""
        column_distribution(column, title=title, xlabel=xlabel, ylabel=ylabel)

        assert mock_plt.title.call_args_list[0][0][0] == title
        assert mock_plt.xlabel.call_args_list[0][0][0] == xlabel
        assert mock_plt.ylabel.call_args_list[0][0][0] == ylabel
        assert mock_plt.subplots.called
        assert mock_plt.show.called

    @mock.patch("eda_viz.viz.plt")
    @pytest.mark.parametrize('column, sort', [
        (CATEGORICAL_LIST, True),
        (CATEGORICAL_LIST, False)
    ])
    def test_column_distribution_sort(self, mock_plt, column, sort):
        """Test column_distribution() method with all parameters."""
        column_distribution(column, sort=sort)

        assert mock_plt.title.call_args_list[0][0][0] == 'Class Distribution'
        assert mock_plt.xlabel.call_args_list[0][0][0] == 'Class'
        assert mock_plt.ylabel.call_args_list[0][0][0] == 'Count'
        assert mock_plt.subplots.called
        assert mock_plt.show.called
