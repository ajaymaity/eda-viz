# EDA and Visualization Library
[![Build Status](https://travis-ci.com/ajaymaity/eda-viz.svg?branch=master)](https://travis-ci.com/ajaymaity/eda-viz)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/ajaymaity/eda-viz/blob/master/LICENSE)

Light-weight Python EDA and Visualization Library for Data Scientists.

The `eda_viz` module is a light-weight library that will make your data 
exploration and visualization tasks lot simpler.

## Installation

You can install `eda-viz` from PyPI:

```buildoutcfg
pip install eda-viz
```

The library is only tested in Python 3.6.5, and on Mac OS v10.13.6.

## How to use

Let's create a sample dataframe:

```buildoutcfg
import pandas as pd
df = pd.DataFrame({
    'categories': ['A', 'B', 'A', 'C', 'D', 'B', 'A'],
    'numbers': [1, 2, 1, 3, 4, 2, 1]
})
```

### Column Distribution

```buildoutcfg
from eda_viz.viz import column_distribution
column_distribution(df['categories'])
```

![Column Distribution](https://raw.githubusercontent.com/ajaymaity/eda-viz/master/images/example-column-distribution.png)

### Histogram

```buildoutcfg
from eda_viz.viz import histogram
histogram(df['numbers'])
```

![Histogram](https://raw.githubusercontent.com/ajaymaity/eda-viz/master/images/example-histogram.png)

### Bar Plot

```buildoutcfg
from eda_viz.viz import bar_plot
bar_plot(df['categories'], df['numbers'])
```

![Bar Plot](https://raw.githubusercontent.com/ajaymaity/eda-viz/master/images/example-bar-plot.png)

Other charts are a WIP.