'''sort unit test'''
import pytest

from rosetta_dsl.test.semantic.sort_operator.SortTest import SortTest

def test_switch_passes():
    sort_test= SortTest()
    sort_test.validate_model()

if __name__ == "__main__":
    test_switch_passes()
