import pytest

from fibonacci.naive import fibonacci_naive

# pytest fibonacci -v


@pytest.mark.parametrize('n, expected', [(0, 0), (1, 1), (2, 1), (20, 6765)])
def test_fibonacci(n: int, expected: int) -> None:
    res = fibonacci_naive(n)
    assert res == expected
