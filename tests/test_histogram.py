"""Test histogram() method in eda_viz.viz module."""
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
from eda_viz.viz import histogram  # noqa: E402
from eda_viz.exceptions import InvalidDataError, \
    NonNumericTypeNotSupportedError, TypeNotSupportedError  # noqa: E402


class TestHistogram(object):
    """Test histogram() method."""

    @mock.patch("eda_viz.viz.plt")
    @pytest.mark.parametrize('column', [
        NUMERICAL_LIST, NUMERICAL_NUMPY, NUMERICAL_PANDAS_SERIES,
        NUMERICAL_LIST_WITH_NONE
    ])
    def test_histogram_default(self, mock_plt, column):
        """Test histogram() method with default parameters."""
        histogram(column)

        assert mock_plt.title.call_args_list[0][0][0] == 'Histogram'
        assert mock_plt.xlabel.call_args_list[0][0][0] == 'Class Bins'
        assert mock_plt.ylabel.call_args_list[0][0][0] == 'Count'
        assert mock_plt.subplots.called
        assert mock_plt.show.called

    @pytest.mark.parametrize('column', [
        CATEGORICAL_PANDAS_DF, NUMERICAL_PANDAS_DF, RANDOM_NUMBER,
        RANDOM_STRING, RANDOM_DICTIONARY, EMPTY_STRING, NONE, NUMPY_NAN,
        NUMPY_INF
    ])
    def test_histogram_type_not_supported_exception(self, column):
        """Test histogram() method when exception is raised."""
        with pytest.raises(TypeNotSupportedError):
            histogram(column)

    @pytest.mark.parametrize('column', [
        CATEGORICAL_LIST, CATEGORICAL_NUMPY, CATEGORICAL_PANDAS_SERIES,
        CATEGORICAL_LIST_WITH_NONE, CATEGORICAL_MULTI_DIM_LIST,
        CATEGORICAL_MULTI_DIM_LIST_2, NUMERICAL_MULTI_DIM_LIST,
        NUMERICAL_MULTI_DIM_LIST_2, CATEGORICAL_AND_NUMERICAL_LIST,
        CATEGORICAL_NUMERICAL_AND_DICTIONARY_LIST, DICTIONARY_LIST,
        ALL_NONE_LIST
    ])
    def test_histogram_non_numeric_type_not_supported_exception(self, column):
        """Test histogram() method when exception is raised."""
        with pytest.raises(NonNumericTypeNotSupportedError):
            histogram(column)

    @pytest.mark.parametrize('column', [
        EMPTY_LIST
    ])
    def test_histogram_invalid_data_exception(self, column):
        """Test histogram() method when exception is raised."""
        with pytest.raises(InvalidDataError):
            histogram(column)

    @mock.patch("eda_viz.viz.plt")
    @pytest.mark.parametrize('column, title, xlabel, ylabel', [
        (NUMERICAL_LIST, RANDOM_TITLE, RANDOM_XLABEL, RANDOM_YLABEL),
    ])
    def test_histogram_parameters(self, mock_plt, column, title,
                                  xlabel, ylabel):
        """Test histogram() method with all parameters."""
        histogram(column, title=title, xlabel=xlabel, ylabel=ylabel)

        assert mock_plt.title.call_args_list[0][0][0] == title
        assert mock_plt.xlabel.call_args_list[0][0][0] == xlabel
        assert mock_plt.ylabel.call_args_list[0][0][0] == ylabel
        assert mock_plt.subplots.called
        assert mock_plt.show.called
