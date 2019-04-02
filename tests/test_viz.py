import pytest
from eda_viz.viz import sum_ab


@pytest.mark.parametrize('a, b, expected', [
    (1, 2, 3),
    (45, 22, 68)
])
def test_sum_ab(a, b, expected):
    assert sum_ab(a, b) == expected
