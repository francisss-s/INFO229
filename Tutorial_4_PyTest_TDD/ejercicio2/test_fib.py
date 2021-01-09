import pytest
from fib import fibonacci

@pytest.mark.parametrize("n,output",[(0,0),(1,1),(2,1),(3,2),(4,3),(5,5),(6,8),(10,55),(15,610),(20,6765)])
def test_fibonacci(n,output):
    assert fibonacci(n) == output