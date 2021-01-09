import pytest
from primes import is_prime, sum_of_primes

#Si introducimos 1, entonces no debe ser un número primo.
def test_prime_number():
    assert is_prime(1) == False

def test_prime_number_2():
    assert is_prime(29)

def test_prime_other_number():
    assert is_prime(15) == False

@pytest.mark.parametrize("n,output",[([81,67,37,32,19,42,13,0,9,45],17),([13,40,60,64,29,72,61,19,49,94],17)])
def test_sum_primes(n,output):
    assert sum_of_primes(n) == output