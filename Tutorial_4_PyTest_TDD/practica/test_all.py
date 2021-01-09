import pytest
from romanos import num_romano, romano_num
from fizzbuzz import fizzBuzz

@pytest.mark.parametrize("a,output",[(1,"I"),(2,"II"),(10,"X"),(1500,"MD"),(1556,"MDLVI")])
def test_num_romano(a,output):
    assert num_romano(a) == output


@pytest.mark.parametrize("a,output",[("I",1),("II",2),("X",10),("MD",1500),("MDLVI",1556)])
def test_romano_num(a,output):
    assert romano_num(a) == output

@pytest.mark.parametrize("a,output",
                                    [(1,['1']),
                                    (10,['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz']),
                                    (14,['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14']),
                                    (21,['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz', '16', '17', 'fizz', '19', 'buzz', 'fizz'])])
def test_fizzBuzz(a,output):
    assert fizzBuzz(a) == output