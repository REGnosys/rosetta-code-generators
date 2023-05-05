import pytest
import datetime
from cdm.base.datetime.DateList import DateList
from cdm.utils import ConditionViolationError


def test_1_many_fail():
    dl = DateList(date=[])
    with pytest.raises(ConditionViolationError):
        dl.validate_conditions()


def test_1_many_fail_nopar():
    dl = DateList()
    with pytest.raises(ConditionViolationError):
        dl.validate_conditions()


def test_1_many_pass():
    dl = DateList(date=[datetime.date(2020, 1, 1)])
    dl.validate_conditions()


if __name__ == "__main__":
	test_1_many_pass()
	test_1_many_fail()
	test_1_many_fail_nopar()
	

# EOF


