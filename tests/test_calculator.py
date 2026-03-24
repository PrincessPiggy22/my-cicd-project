import pytest
import requests
from src.calculator import add

# Replaces writing 4 identical test functions
@pytest.mark.parametrize("a, b, expected", [
    (2,   3,   5),    # positive
    (0,   0,   0),    # zeros
    (-1,  1,   0),    # negative
    (100, -50, 50),   # large values
])
def test_add_cases(a, b, expected):
    assert add(a, b) == expected

# pytest -k "2-3-5"
@pytest.mark.skip(reason="WIP")
@pytest.mark.external
@pytest.mark.slow
def test_weather_api():
    resp = requests.get(WEATHER_URL)
    assert resp.status_code == 200
