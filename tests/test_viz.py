# Doesn't contain proper tests yet
import pandas as pd

from eda_viz.viz import column_distribution

df = pd.DataFrame({
    'col1': ['ajay', 'nikita', 'ajay', 'sonia', 'sumeet', 'nikita', 'ajay'],
    'col2': [1, 2, 3, 4, 5, 6, 7]
})

if __name__ == '__main__':
    column_distribution(df['col1'])
