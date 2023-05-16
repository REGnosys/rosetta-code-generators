# pylint: disable=line-too-long, invalid-name, missing-function-docstring, missing-module-docstring, superfluous-parens
# pylint: disable=wrong-import-position, unused-import, unused-wildcard-import, wildcard-import, wrong-import-order, missing-class-docstring
from __future__ import annotations
from typing import List, Optional
from datetime import date
from datetime import time
from datetime import datetime
from decimal import Decimal
from pydantic import Field
from rosetta.runtime.utils import *

__all__ = ['LimitApplicable']


class LimitApplicable(BaseDataClass):
  amountRemaining: Optional[Decimal] = Field(None, description="The limit remaining for the limit level and limit type. This does not take into account any pending trades. While the attribute is of type integer in FpML and the CME schema, it has been specified to be of type number in the CDM to take into consideration java size limits as well as for consistency purposes with the way most monetary amounts are expressed.")
  """
  The limit remaining for the limit level and limit type. This does not take into account any pending trades. While the attribute is of type integer in FpML and the CME schema, it has been specified to be of type number in the CDM to take into consideration java size limits as well as for consistency purposes with the way most monetary amounts are expressed.
  """
  amountUtilized: Optional[Decimal] = Field(None, description="The limit utilised by all the cleared trades for the limit level and limit type. While the attribute is of type integer in FpML and the CME schema, it has been specified to be of type number in the CDM to take into consideration java size limits as well as for consistency purposes with the way most monetary amounts are expressed.")
  """
  The limit utilised by all the cleared trades for the limit level and limit type. While the attribute is of type integer in FpML and the CME schema, it has been specified to be of type number in the CDM to take into consideration java size limits as well as for consistency purposes with the way most monetary amounts are expressed.
  """
  clipSize: Optional[int] = Field(None, description="This element is required in FpML, optional in CDM for the purpose of accommodating the CME data representation while making reference to the FpML one.")
  """
  This element is required in FpML, optional in CDM for the purpose of accommodating the CME data representation while making reference to the FpML one.
  """
  currency: Optional[AttributeWithMeta[str] | str] = Field(None, description="The currency in which the applicable limit is denominated. The list of valid currencies is not presently positioned as an enumeration as part of the CDM because that scope is limited to the values specified by ISDA and FpML. As a result, implementers have to make reference to the relevant standard, such as the ISO 4217 standard for currency codes.")
  """
  The currency in which the applicable limit is denominated. The list of valid currencies is not presently positioned as an enumeration as part of the CDM because that scope is limited to the values specified by ISDA and FpML. As a result, implementers have to make reference to the relevant standard, such as the ISO 4217 standard for currency codes.
  """
  limitType: Optional[AttributeWithMeta[CreditLimitTypeEnum] | CreditLimitTypeEnum] = Field(None, description="Standard code to indicate which type of credit line is being referred to - i.e. IM, DV01, PV01, CS01, Notional, Clip Size, Notional, maximumOrderQuantity.")
  """
  Standard code to indicate which type of credit line is being referred to - i.e. IM, DV01, PV01, CS01, Notional, Clip Size, Notional, maximumOrderQuantity.
  """
  utilization: Optional[CreditLimitUtilisation] = Field(None, description="")
  velocity: Optional[Velocity] = Field(None, description="")
  
  @rosetta_condition
  def condition_0_LimitApplicableChoice(self):
    """
    Choice rule to represent an FpML choice construct.
    """
    return self.check_one_of_constraint('amountUtilized', 'utilization', necessity=False)

from cdm.event.workflow.CreditLimitTypeEnum import CreditLimitTypeEnum
from cdm.event.workflow.CreditLimitUtilisation import CreditLimitUtilisation
from cdm.event.workflow.Velocity import Velocity

LimitApplicable.update_forward_refs()
