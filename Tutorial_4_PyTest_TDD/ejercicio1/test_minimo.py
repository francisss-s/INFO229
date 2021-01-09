from minimo import get_min
import pytest


@pytest.mark.parametrize("values, output",[([1,2,3,4,5],1),([50,3,512,42],3),([50,123,532.,100],50)])
def test_get_min(values,output):
    assert get_min(values) == output
