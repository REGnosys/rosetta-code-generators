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

__all__ = ['BaseAndEligibleCurrency']


class BaseAndEligibleCurrency(BaseDataClass):
  """
  The base and eligible currency(ies) for the document as specified by the parties to the agreement.
  """
  baseCurrency: AttributeWithMeta[str] | str = Field(..., description="The base currency for the document as elected by the parties to the agreement. The list of valid currencies is not presently positioned as an enumeration as part of the CDM because that scope is limited to the values specified by ISDA and FpML. As a result, implementers have to make reference to the relevant standard, such as the ISO 4217 standard for currency codes.")
  """
  The base currency for the document as elected by the parties to the agreement. The list of valid currencies is not presently positioned as an enumeration as part of the CDM because that scope is limited to the values specified by ISDA and FpML. As a result, implementers have to make reference to the relevant standard, such as the ISO 4217 standard for currency codes.
  """
  eligibleCurrency: List[AttributeWithMeta[str] | str] = Field([], description="The list of eligible currencies, in addition to the base currency, for the document as elected by the parties to the agreement.")
  """
  The list of eligible currencies, in addition to the base currency, for the document as elected by the parties to the agreement.
  """


BaseAndEligibleCurrency.update_forward_refs()
