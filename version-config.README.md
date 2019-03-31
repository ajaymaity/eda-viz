## Usage of `version-config.ini`

Make sure to update the parameters in `version-config.ini` to appropriate 
`project_name` and `version`. This is used by setup.py to set up correct
values for publishing to PyPI or test PyPI.

For PyPI, the contents of `version-config.ini` should be as follows:
```buildoutcfg
[pypi]
project_name=eda-viz
version=0.0.3
```

For test PyPI, the contents of `version-config.ini` should be as follows:
```buildoutcfg
[pypi]
project_name=eda-viz-test
version=0.0.3
```

Make sure to increment the `version` parameter before you publish.