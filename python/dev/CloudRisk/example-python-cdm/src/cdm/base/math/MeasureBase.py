from __future__ import annotations
from typing import Optional
from pydantic import Field
from cdm.utils import *


__all__ = ['MeasureBase']


class MeasureBase(BaseDataClass):
    """
    Provides an abstract base class shared by Price and Quantity.
    """
    amount: float = Field(..., description="Specifies an amount to be qualified and used in a Price or Quantity definition.")
    """
    Specifies an amount to be qualified and used in a Price or Quantity definition.
    """
    unitOfAmount: UnitType = Field(..., description="Qualifies the unit by which the amount is measured.")
    """
    Qualifies the unit by which the amount is measured.
    """


from cdm.base.math.UnitType import UnitType

MeasureBase.update_forward_refs()

# EOF
