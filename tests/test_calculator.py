import pytest
from src.calculator import add

@pytest.mark.external
@pytest.mark.slow

# Replaces writing 4 identical test functions
@pytest.mark.parametrize("a, b, expected", [
    (2,   3,   5),    # positive
    (0,   0,   0),    # zeros
    (-1,  1,   0),    # negative
    (100, -50, 50),   # large values
])
def test_add_cases(a, b, expected):
    assert add(a, b) == expected

# pytest -v output:
# PASSED  test_add_cases[2-3-5]
# PASSED  test_add_cases[0-0-0]
# PASSED  test_add_cases[-1-1-0]
# PASSED  test_add_cases[100--50-50]

# Re-run one failing case by ID:
pytest -k "2-3-5"
