import numpy as np
import pandas as pd

CATEGORICAL_LIST = ['A', 'B', 'A', 'C', 'D', 'B', 'A']
CATEGORICAL_NUMPY = np.array(['A', 'B', 'A', 'C', 'D', 'B', 'A'])
CATEGORICAL_PANDAS = pd.Series(['A', 'B', 'A', 'C', 'D', 'B', 'A'])
CATEGORICAL_LIST_WITH_NONE = ['A', None, 'A', 'C', 'D', 'B', None]
CATEGORICAL_MULTI_DIM_LIST = [['A', 'B', 'C']]

NUMERICAL_LIST = [1, 2, 3, 4, 5, 6]

CAT_AND_NUM_LIST = [1, 'abcd', 3, 'defg', 5, 'ghij']
CAT_NUM_AND_DICT_LIST = [1, 'A', {'a': 1}, 3, 4, 5, 6]

RANDOM_STRING = 'abcd'
RANDOM_NUMBER = 1234
RANDOM_DICT = {'a': 1, 'b': 2}

RANDOM_TITLE = 'Some Random Title'
RANDOM_XLABEL = 'Random xlabel'
RANDOM_YLABEL = 'Random ylabel'

EMPTY_LIST = []
ALL_NONE_LIST = [None, None, None, None, None]