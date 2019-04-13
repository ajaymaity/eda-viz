import pathlib
from setuptools import setup
from configparser import ConfigParser

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# Load the version-config file
config = ConfigParser()
config.read('{}/version-config.ini'.format(HERE))
project_name = config.get('pypi', 'project_name')
version = config.get('pypi', 'version')

with open('requirements.txt') as f:
    required = f.read().splitlines()

# This call to setup() does all the work
setup(
    name=project_name,
    version=version,
    description="Light-weight Python EDA and Visualization Library for Data "
                "Scientists",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ajaymaity/eda-viz",
    author="Ajay Maity",
    author_email="eda.viz.py@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["eda_viz"],
    include_package_data=True,
    install_requires=required
)
