import pytest
import SelectionSort as ss

@pytest.mark.parametrize("arr, sorted_arr", [
    ([2,3,4,6,7,1], [1,2,3,4,6,7]),
    ([9,8,7,6,5,4,3,2,1], [1,2,3,4,5,6,7,8,9]), 
    ([1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9]),
    ([], []),
    ([1], [1])
])

def test_add(arr, sorted_arr):
    assert ss.selection_sort(arr) == sorted_arr
