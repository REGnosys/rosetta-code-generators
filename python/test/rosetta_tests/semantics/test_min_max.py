'''min max unit tests'''
import pytest

from rosetta_dsl.test.semantic.min_max.MaxTest import MaxTest
from rosetta_dsl.test.semantic.min_max.MinTest import MinTest

def test_min_passes():
    min_test = MinTest(a=10)
    min_test.validate_model()

def test_min_fails ():
    min_test = MinTest(a=-1)
    with pytest.raises(Exception):
        min_test.validate_model()

def test_max_passes():
    max_test = MaxTest(a=1)
    max_test.validate_model()

def test_max_fails ():
    max_test = MaxTest(a=100)
    with pytest.raises(Exception):
        max_test.validate_model()

if __name__ == "__main__":
    test_min_passes()
    test_min_fails()