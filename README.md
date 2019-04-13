# EDA and Visualization Library
[![Build Status](https://travis-ci.com/ajaymaity/eda-viz.svg?branch=master)](https://travis-ci.com/ajaymaity/eda-viz)

Light-weight Python EDA and Visualization Library for Data Scientists.

The `eda_viz` module is a light-weight library that will make your data 
exploration and visualization tasks lot simpler.

Currently, the library only supports Pandas DataFrame.

## Installation

You can install `eda-viz` from PyPI:

```buildoutcfg
pip install eda-viz
```

The library is only tested in Python 3.6.5, and on Mac OS v10.13.6.

## How to use

To plot `column_distribution`, you can use the following example:

```buildoutcfg
import pandas as pd
from eda_viz.viz import column_distribution

df = pd.DataFrame({
    'categories': ['A', 'A', 'B', 'C', 'A', 'B']
})
column_distribution(df['categories'])
```

which will plot the following chart:

![Column Distribution Chart](https://raw.githubusercontent.com/ajaymaity/ajaymaity.github.io/master/Documents/eda-viz/example_column_distribution.png)

Other charts are a WIP.