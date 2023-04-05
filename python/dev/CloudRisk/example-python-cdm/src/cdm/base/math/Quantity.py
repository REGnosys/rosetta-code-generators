from __future__ import annotations
from typing import Optional
from pydantic import Field
from cdm.utils import *
from cdm.base.math.MeasureBase import MeasureBase

class Quantity(MeasureBase):
    """
    Specifies a quantity to be associated to a financial product, for example a trade amount or a cashflow amount resulting from a trade.
    """
    multiplier: Optional[float] = Field(None,description = "Defines the number to be multiplied by the amount to derive a total quantity.")
    """
    Defines the number to be multiplied by the amount to derive a total quantity.
    """
    multiplierUnit: Optional[UnitType] = Field(None,description = "Qualifies the multiplier with the applicable unit.  For example in the case of the Coal (API2) CIF ARA (ARGUS-McCloskey) Futures Contract on the CME, where the unitOfAmount would be contracts, the multiplier would 1,000 and the mulitiplier Unit would be 1,000 MT (Metric Tons).")
    """
    Qualifies the multiplier with the applicable unit.  For example in the case of the Coal (API2) CIF ARA (ARGUS-McCloskey) Futures Contract on the CME, where the unitOfAmount would be contracts, the multiplier would 1,000 and the mulitiplier Unit would be 1,000 MT (Metric Tons).
    """
    
    @cdm_condition
    def condition_0_Quantity_multiplier(self):
        """
        Requires that the multiplier must be positive.
        """
        return if_cond(((self.multiplier) is not None), '(self.multiplier >= 0.0)', 'True', self)

from cdm.base.math.UnitType import UnitType

Quantity.update_forward_refs()

# EOF
