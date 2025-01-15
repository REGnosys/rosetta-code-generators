'''switch unit tests'''
import pytest

from rosetta_dsl.test.semantic.switch_operator.SwitchTest import SwitchTest

def test_switch_passes():
    switch_test= SwitchTest(a=2)
    switch_test.validate_model()

def test_switch_fails ():
    switch_test = SwitchTest(a=-1)
    with pytest.raises(Exception):
        switch_test.validate_model()

if __name__ == "__main__":
    test_switch_passes()
    test_switch_fails()