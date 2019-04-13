"""Contains test data needed to test this application."""
import numpy as np
import pandas as pd

# List of Categorical Data
CATEGORICAL_LIST = ['A', 'B', 'A', 'C', 'D', 'B', 'A']
CATEGORICAL_NUMPY = np.array(CATEGORICAL_LIST)
CATEGORICAL_PANDAS_SERIES = pd.Series(CATEGORICAL_LIST)
CATEGORICAL_PANDAS_DF = pd.DataFrame(CATEGORICAL_LIST)
CATEGORICAL_LIST_WITH_NONE = ['A', None, 'A', 'C', 'D', 'B', None]
CATEGORICAL_MULTI_DIM_LIST = [['A', 'B', 'C']]
CATEGORICAL_MULTI_DIM_LIST_2 = [['A'], ['B'], 'C']

# List of Numerical Data
NUMERICAL_LIST = [1, 2, 1, 3, 4, 2, 1]
NUMERICAL_NUMPY = np.array(NUMERICAL_LIST)
NUMERICAL_PANDAS_SERIES = pd.Series(NUMERICAL_LIST)
NUMERICAL_PANDAS_DF = pd.DataFrame(NUMERICAL_LIST)
NUMERICAL_LIST_WITH_NONE = [1, None, 1, 3, 4, 2, None]
NUMERICAL_MULTI_DIM_LIST = [[1, 2, 3]]
NUMERICAL_MULTI_DIM_LIST_2 = [[1], [2], 3]

# List of multiple Data types
CATEGORICAL_AND_NUMERICAL_LIST = [1, 'A', 3, 'B', 5, 'C']
CATEGORICAL_NUMERICAL_AND_DICTIONARY_LIST = [1, 'A', {'B': 1}, 3, 4, 5, 6]
DICTIONARY_LIST = [{'A': 1}, {'B': 2}, {'C': 3, 'D': 4}]

# Single data types
RANDOM_NUMBER = 1234
RANDOM_STRING = 'abcd'
RANDOM_DICTIONARY = {'a': 1, 'b': 2}
EMPTY_STRING = ''
NONE = None
NUMPY_NAN = np.nan
NUMPY_INF = np.inf

# Others
EMPTY_LIST = []
ALL_NONE_LIST = [None, None, None, None, None]

# Method argument placeholders
RANDOM_TITLE = 'Some Random Title'
RANDOM_XLABEL = 'Random xlabel'
RANDOM_YLABEL = 'Random ylabel'
