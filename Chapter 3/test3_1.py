import pytest
import fib_rec

@pytest.mark.parametrize("num, target", [
    (1, 1),
    (2, 2), 
    (3, 6),
    (4, 24),
    (5, 120)
])

def test_add(num, target):
    assert fib_rec.fib_recursion(num) == target
