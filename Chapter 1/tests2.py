import pytest
import BinSe as bs

# 4 test cases
@pytest.mark.parametrize("arr, target, expected", [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 10, -1),
    ([], 1, -1),
    ([1], 1, 0),
    ([1], 2, -1)
])

def test_add(arr, target, expected):
    assert bs.binSearch(arr, target) == expected
