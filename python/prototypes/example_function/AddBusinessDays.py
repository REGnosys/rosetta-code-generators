# pylint: disable=invalid-name, missing-module-docstring
import sys
import inspect
import datetime
from rosetta.runtime.func_proxy import replaceable, create_module_attr_guardian
from rosetta.runtime.utils import if_cond_fn, rosetta_resolve_attr
from cdm.base.datetime.BusinessCenterEnum import BusinessCenterEnum
from cdm.base.datetime.functions.IsBusinessDay import IsBusinessDay
from cdm.base.datetime.functions.AddDays import AddDays


@replaceable
def AddBusinessDays(originalDate: datetime.date, offsetBusinessDays: int,
                    businessCenters: list[BusinessCenterEnum] | None) -> datetime.date:
    ''' Returns a good business date that has been offset by the given number
        of business days given the supplied business centers. A negative value
        implies an earlier date (before the supplied originalDate), and a
        positive value a later date (after the supplied date).

        Parameters
        ----------
        originalDate : datetime.date
            date to be shifted. If not a good business day,
            a supplied shift of 0 will shift it to the next business day

        offsetBusinessDays : int
            number of business days to shift the original date

        businessCenters : list[BusinessCenterEnum] | None
            business centers to use in the shifting

        Returns
        -------
        shiftedDate : datetime.date

    '''
    self = inspect.currentframe()

    def _then_fn0():
        return -1

    def _else_fn0():
        return 1

    def _then_fn1():
        return rosetta_resolve_attr(self, "shift")

    def _else_fn1():
        return 0

    def _then_fn2():
        return 0

    def _else_fn2():
        return rosetta_resolve_attr(self, "offsetBusinessDays") - rosetta_resolve_attr(self, "newShift")

    def _then_fn3():
        return rosetta_resolve_attr(self, "originalDate")

    def _else_fn3():
        return AddBusinessDays(rosetta_resolve_attr(self, "shiftedByOne"), rosetta_resolve_attr(self, "newOffset"), rosetta_resolve_attr(self, "businessCenters"))

    isGoodBusinessDay = IsBusinessDay(rosetta_resolve_attr(self, "originalDate"), rosetta_resolve_attr(self, "businessCenters"))
    shift = if_cond_fn(((rosetta_resolve_attr(self, "offsetBusinessDays")) < 0), _then_fn0, _else_fn0)
    shiftedByOne = AddDays(rosetta_resolve_attr(self, "originalDate"), rosetta_resolve_attr(self, "shift"))
    isShiftedGood = IsBusinessDay(rosetta_resolve_attr(self, "shiftedByOne"), rosetta_resolve_attr(self, "businessCenters"))
    newShift = if_cond_fn((rosetta_resolve_attr(self, "isShiftedGood")), _then_fn1, _else_fn1)
    newOffset = if_cond_fn(((rosetta_resolve_attr(self, "offsetBusinessDays")) == 0), _then_fn2, _else_fn2)
    done = ((rosetta_resolve_attr(self, "offsetBusinessDays") == 0) and (rosetta_resolve_attr(ctx.f_locals, "isGoodBusinessDay") == True))
    newDate = if_cond_fn((rosetta_resolve_attr(self, "done")), _then_fn3, _else_fn3)
    shiftedDate = rosetta_resolve_attr(self, "newDate")
    return rosetta_resolve_attr(self, "shiftedDate")


sys.modules[__name__].__class__ = create_module_attr_guardian(sys.modules[__name__].__class__)

# EOF
