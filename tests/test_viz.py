import mock
import numpy as np
import os
import pandas as pd
import pytest
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from eda_viz.viz import column_distribution
from eda_viz.exception import TypeNotSupportedError


@mock.patch("eda_viz.viz.plt")
@pytest.mark.parametrize('column', [
    (['A', 'B', 'A', 'C', 'D', 'B', 'A']),
    (np.array(['A', 'B', 'A', 'C', 'D', 'B', 'A'])),
    (pd.Series(['A', 'B', 'A', 'C', 'D', 'B', 'A'])),
    ([1, 2, 3, 4, 5, 6]),
    ([1, 'abcd', 3, 'defg', 5, 'ghij'])
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
    (['A', 'B', 'A', 'C', 'D', 'B', 'A'], 'Some Random Chart', 'Random xlabel',
              'Random ylabel'),
    (np.array(['A', 'B', 'A', 'C', 'D', 'B', 'A']), 'Numpy Chart',
              'Numpy xlabel', 'Numpy ylabel'),
    (pd.Series(['A', 'B', 'A', 'C', 'D', 'B', 'A']), 'Pandas Chart',
               'Pandas xlabel', 'Pandas ylabel')
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
    ('abcd', 1234, {'a': 1, 'b': 2})
])
def test_column_distribution_exception(mock_plt, column):
    """Test column_distribution() method when exception is raised."""
    with pytest.raises(TypeNotSupportedError):
        column_distribution(column)
