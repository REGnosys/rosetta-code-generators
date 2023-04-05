from __future__ import annotations
from typing import Optional
from pydantic import Field
from cdm.utils import *
from cdm.base.math.Quantity import Quantity


class Money(Quantity):
    """
    Defines a monetary amount in a specified currency.
    """
    
    @cdm_condition
    def condition_0_(self):
        return ((self.unitOfAmount.currency) is not None)

# EOF
