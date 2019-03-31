## Please follow the steps below for publishing the library to PyPI or test PyPI

### Publish to test PyPI
1. Change the values in `version-config.ini` to:
```buildoutcfg
[pypi]
project_name=eda-viz-test
version=0.0.3
```
Make sure the version is incremented since last publish.

2. Execute the following command to create python packages:
```buildoutcfg
python setup.py sdist bdist_wheel
```

3. Make sure the distribution file for the version you mentioned in 
`version-config.ini` is present in `dist/` directory.

4. Upload to test PyPI using the following command:
```buildoutcfg
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

Enter your username and password, and let it publish to test PyPI.

5. Delete the files in `dist/` directory.

-----

### Publish to test PyPI
1. Change the values in `version-config.ini` to:
```buildoutcfg
[pypi]
project_name=eda-viz
version=0.0.3
```
Make sure the version is incremented since last publish.

2. Execute the following command to create python packages:
```buildoutcfg
python setup.py sdist bdist_wheel
```

3. Make sure the distribution file for the version you mentioned in 
`version-config.ini` is present in `dist/` directory.

4. Upload to test PyPI using the following command:
```buildoutcfg
twine upload dist/*
```

Enter your username and password, and let it publish to test PyPI.

5. Delete the files in `dist/` directory.