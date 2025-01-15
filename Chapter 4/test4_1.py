import pytest
import QuickSort as qs

@pytest.mark.parametrize("arr, sorted_arr", [
    ([2,3,4,6,7,1], [1,2,3,4,6,7]),
    ([9,8,7,6,5,4,3,2,1], [1,2,3,4,5,6,7,8,9]), 
    ([1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9]),
    ([2,3,3,4,5,1], [1,2,3,3,4,5]),
    ([0,0,3,1,0,0], [0,0,0,0,1,3]),
    ([], []), 
    ([1], [1])
])

def test_add(arr, sorted_arr):
    assert qs.QuickSort(arr) == sorted_arr
