from pydantic import ValidationError
import pytest
from cdm.utils import ConditionViolationError
from cdm.base.math.UnitType import UnitType
from cdm.base.datetime.Frequency import Frequency
from cdm.base.datetime.PeriodExtendedEnum import PeriodExtendedEnum
from cdm.base.math.FinancialUnitEnum import FinancialUnitEnum
from cdm.base.math.CapacityUnitEnum import CapacityUnitEnum
from cdm.base.math.Quantity import Quantity
from cdm.base.math.MeasureBase import MeasureBase
from cdm.base.math.WeatherUnitEnum import WeatherUnitEnum


def test_UnitType_creation():
    ut = UnitType(currency='USD')
    assert ut.currency == 'USD'
    assert ut.capacityUnit is None
    assert ut.financialUnit is None


def test_UnitType_root_validator_multiple():
    ut = UnitType(financialUnit=FinancialUnitEnum.INDEX_UNIT,
                  currency='USD')
    with pytest.raises(ConditionViolationError):
        ut.validate_conditions()


def test_UnitType_root_validator_none():
    frq = Frequency(periodMultiplier=1, period=PeriodExtendedEnum.Y)
    ut = UnitType(frequency=frq)
    with pytest.raises(ConditionViolationError):
        ut.validate_conditions()


def test_UnitType_manipulation():
    frq = Frequency(periodMultiplier=1, period=PeriodExtendedEnum.Y)
    ut = UnitType(currency='USD', frequency=frq)
    ut.currency = None  # after this, the object is in an inconsistent state
    ut.capacityUnit = CapacityUnitEnum.BBL  # object is valid now
    ut.validate_conditions()


def test_UnitType_bad_field():
    frq = Frequency(periodMultiplier=1, period=PeriodExtendedEnum.Y)
    ut = UnitType(currency='USD', frequency=frq)
    ut.currency = None
    ut.capacityUnit = CapacityUnitEnum.BBL
    ut.weatherUnit = CapacityUnitEnum.BBL
    with pytest.raises(ConditionViolationError):
        ut.validate_conditions()


def test_UnitType_bad_choice_manipulation():
    frq = Frequency(periodMultiplier=1, period=PeriodExtendedEnum.Y)
    ut = UnitType(currency='USD', frequency=frq)
    ut.capacityUnit = CapacityUnitEnum.BBL
    with pytest.raises(ConditionViolationError):
        ut.validate_conditions()


def test_Quantity_condition():
    with pytest.raises(ValueError):
        q = Quantity(multiplier=-1.0)
        q.validate_conditions()


def test_MeasureBase():
    ua = UnitType(weatherUnit=WeatherUnitEnum.CPD)
    mb = MeasureBase(amount=1, unit=ua)
    mb.validate_conditions()


def test_MeasureBase_incomplete_unit():
    ua = UnitType()
    mb = MeasureBase(amount=1, unit=ua)
    with pytest.raises(ValueError):
        mb.validate_conditions()


if __name__ == '__main__':
    # test_Quantity_condition()
    test_MeasureBase_incomplete_unit()

# EOF
