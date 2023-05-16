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

__all__ = ['NotDomesticCurrency']


class NotDomesticCurrency(BaseDataClass):
  """
  A class to specify the ISDA 2003 Term: Not Domestic Currency.
  """
  applicable: bool = Field(..., description="Indicates whether the Not Domestic Currency provision is applicable.")
  """
  Indicates whether the Not Domestic Currency provision is applicable.
  """
  currency: Optional[AttributeWithMeta[str] | str] = Field(None, description="An explicit specification of the domestic currency. The list of valid currencies is not presently positioned as an enumeration as part of the CDM because that scope is limited to the values specified by ISDA and FpML. As a result, implementers have to make reference to the relevant standard, such as the ISO 4217 standard for currency codes.")
  """
  An explicit specification of the domestic currency. The list of valid currencies is not presently positioned as an enumeration as part of the CDM because that scope is limited to the values specified by ISDA and FpML. As a result, implementers have to make reference to the relevant standard, such as the ISO 4217 standard for currency codes.
  """


NotDomesticCurrency.update_forward_refs()
