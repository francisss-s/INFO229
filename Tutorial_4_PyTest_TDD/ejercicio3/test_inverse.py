from revierte import inverse
import pytest
@pytest.mark.parametrize("n,output",[("Hola","aloH"),("Chao","oahC")])
def test_inverse(n,output):
    assert  inverse(n) == output