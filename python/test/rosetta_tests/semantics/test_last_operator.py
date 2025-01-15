'''last unit test'''
import pytest

from rosetta_dsl.test.semantic.last_operator.LastTest import LastTest

def test_last_passes():
    last = 5
    last_test = LastTest(aValue=2, bValue=3, cValue=last, target=last)
    last_test.validate_model()

if __name__ == "__main__":
    test_last_passes()
