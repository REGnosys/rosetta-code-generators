import pytest
from cdm.observable.asset.Money import Money
from cdm.base.math.UnitType import UnitType
from cdm.utils import ConditionViolationError


def test_Money_condition():
    ut = UnitType(currency='USD')
    my = Money(unit=ut, value=1)
    my.validate_conditions()

def test_Money_condition_failing():
    ut = UnitType()
    my = Money(value=1, unit=ut)
    with pytest.raises(ConditionViolationError):
        my.validate_conditions()

# EOF
