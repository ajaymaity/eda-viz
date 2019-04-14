"""Test bar_plot() method in eda_viz.viz module."""
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
from eda_viz.viz import bar_plot  # noqa: E402
from eda_viz.exceptions import InvalidDataError, \
    NonNumericTypeNotSupportedError, TypeNotSupportedError  # noqa: E402
from eda_viz.warnings import DifferentLengthWarning  # noqa: E402


class TestBarPlot(object):
    """Test bar_plot() method."""

    @mock.patch("eda_viz.viz.plt")
    @pytest.mark.parametrize('x, y', [
        (CATEGORICAL_LIST, NUMERICAL_LIST),
        (CATEGORICAL_NUMPY, NUMERICAL_NUMPY),
        (CATEGORICAL_PANDAS_SERIES, NUMERICAL_PANDAS_SERIES),
        (CATEGORICAL_LIST_WITH_NONE, NUMERICAL_LIST_WITH_NONE),
        (NUMERICAL_LIST, NUMERICAL_LIST),
        (NUMERICAL_NUMPY, NUMERICAL_NUMPY),
        (NUMERICAL_PANDAS_SERIES, NUMERICAL_PANDAS_SERIES),
        (NUMERICAL_LIST_WITH_NONE, NUMERICAL_LIST_WITH_NONE),
        (CATEGORICAL_LIST, NUMERICAL_NUMPY),
        (CATEGORICAL_NUMPY, NUMERICAL_PANDAS_SERIES),
        (CATEGORICAL_AND_NUMERICAL_LIST, NUMERICAL_LIST),
        (NUMERICAL_LIST, EMPTY_LIST)
    ])
    def test_bar_plot_default(self, mock_plt, x, y):
        """Test bar_plot() method with default parameters."""
        bar_plot(x, y)

        assert mock_plt.title.call_args_list[0][0][0] == 'Bar Plot'
        assert mock_plt.xlabel.call_args_list[0][0][0] == 'x-axis'
        assert mock_plt.ylabel.call_args_list[0][0][0] == 'y-axis'
        assert mock_plt.subplots.called
        assert mock_plt.show.called

    @pytest.mark.parametrize('x, y', [
        (CATEGORICAL_PANDAS_DF, NUMERICAL_LIST),
        (NUMERICAL_PANDAS_DF, NUMERICAL_LIST),
        (CATEGORICAL_LIST, NUMERICAL_PANDAS_DF),
        (RANDOM_NUMBER, NUMERICAL_LIST),
        (RANDOM_STRING, NUMERICAL_LIST),
        (RANDOM_DICTIONARY, NUMERICAL_LIST),
        (EMPTY_STRING, NUMERICAL_LIST),
        (NONE, NUMERICAL_LIST),
        (NUMPY_NAN, NUMERICAL_LIST),
        (NUMPY_INF, NUMERICAL_LIST),
        (CATEGORICAL_LIST, RANDOM_DICTIONARY),
    ])
    def test_bar_plot_type_not_supported_exception(self, x, y):
        """Test bar_plot() method when exception is raised."""
        with pytest.raises(TypeNotSupportedError):
            bar_plot(x, y)

    @pytest.mark.parametrize('x, y', [
        (CATEGORICAL_LIST, CATEGORICAL_LIST),
        (CATEGORICAL_LIST, CATEGORICAL_NUMPY),
        (CATEGORICAL_LIST, CATEGORICAL_PANDAS_SERIES),
        (CATEGORICAL_LIST, CATEGORICAL_LIST_WITH_NONE),
        (CATEGORICAL_LIST, NUMERICAL_MULTI_DIM_LIST),
        (CATEGORICAL_LIST, NUMERICAL_MULTI_DIM_LIST_2),
        (CATEGORICAL_LIST, CATEGORICAL_AND_NUMERICAL_LIST),
        (CATEGORICAL_LIST, CATEGORICAL_NUMERICAL_AND_DICTIONARY_LIST),
        (CATEGORICAL_LIST, DICTIONARY_LIST),
        (CATEGORICAL_LIST, ALL_NONE_LIST),
        (CATEGORICAL_LIST, CATEGORICAL_MULTI_DIM_LIST)
    ])
    def test_bar_plot_non_numeric_type_not_supported_exception(self, x, y):
        """Test bar_plot() method when exception is raised."""
        with pytest.raises(NonNumericTypeNotSupportedError):
            bar_plot(x, y)

    @pytest.mark.parametrize('x, y', [
        (CATEGORICAL_MULTI_DIM_LIST, NUMERICAL_LIST),
        (CATEGORICAL_MULTI_DIM_LIST_2, NUMERICAL_LIST),
        (NUMERICAL_MULTI_DIM_LIST, NUMERICAL_LIST),
        (NUMERICAL_MULTI_DIM_LIST_2, NUMERICAL_LIST),
        (CATEGORICAL_NUMERICAL_AND_DICTIONARY_LIST, NUMERICAL_LIST),
        (DICTIONARY_LIST, NUMERICAL_LIST),
        (ALL_NONE_LIST, NUMERICAL_LIST),
        (EMPTY_LIST, NUMERICAL_LIST)
    ])
    def test_bar_plot_invalid_data_exception(self, x, y):
        """Test bar_plot() method when exception is raised."""
        with pytest.raises(InvalidDataError):
            bar_plot(x, y)

    @mock.patch("eda_viz.viz.plt")
    @pytest.mark.parametrize('x, y', [
        (CATEGORICAL_LIST, EMPTY_LIST)
    ])
    def test_bar_plot_different_length_warning(self, mock_plt, x, y):
        """Test bar_plot() method when exception is raised."""
        with pytest.warns(DifferentLengthWarning):
            bar_plot(x, y)

            assert mock_plt.title.call_args_list[0][0][0] == 'Bar Plot'
            assert mock_plt.xlabel.call_args_list[0][0][0] == 'x-axis'
            assert mock_plt.ylabel.call_args_list[0][0][0] == 'y-axis'
            assert mock_plt.subplots.called
            assert mock_plt.show.called

    @mock.patch("eda_viz.viz.plt")
    @pytest.mark.parametrize('x, y, title, xlabel, ylabel', [
        (CATEGORICAL_LIST, NUMERICAL_LIST, RANDOM_TITLE, RANDOM_XLABEL,
         RANDOM_YLABEL),
    ])
    def test_bar_plot_parameters(self, mock_plt, x, y, title,
                                 xlabel, ylabel):
        """Test bar_plot() method with all parameters."""
        bar_plot(x, y, title=title, xlabel=xlabel, ylabel=ylabel)

        assert mock_plt.title.call_args_list[0][0][0] == title
        assert mock_plt.xlabel.call_args_list[0][0][0] == xlabel
        assert mock_plt.ylabel.call_args_list[0][0][0] == ylabel
        assert mock_plt.subplots.called
        assert mock_plt.show.called
