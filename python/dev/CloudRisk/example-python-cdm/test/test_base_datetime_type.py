import pytest
from cdm.utils import ConditionViolationError
from cdm.base.datetime.AdjustableDates import AdjustableDates
from cdm.base.datetime.BusinessDayAdjustments import BusinessDayAdjustments
from cdm.base.datetime.BusinessDayConventionEnum import BusinessDayConventionEnum


def test_AdjustableDates_creation():
    bd = BusinessDayAdjustments(
        businessDayConvention=BusinessDayConventionEnum.FOLLOWING)
    dt = AdjustableDates(unadjustedDate=['2022-05-11'], dateAdjustments=bd)
    assert dt.adjustedDate is None


def test_AdjustableDates_bad_cardinality():
    bd = BusinessDayAdjustments(
        businessDayConvention=BusinessDayConventionEnum.FOLLOWING)
    ad = AdjustableDates(unadjustedDate=[], dateAdjustments=bd)
    ad.validate_conditions()

# EOF
