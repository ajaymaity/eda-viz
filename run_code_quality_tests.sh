#!/usr/bin/env bash
echo 'Running flake8 on eda_viz...'
flake8 eda_viz
echo 'Running flake8 on tests...'
flake8 tests

echo 'Running pylint on eda_viz...'
pylint eda_viz