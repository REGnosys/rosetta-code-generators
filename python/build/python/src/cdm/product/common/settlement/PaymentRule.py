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

__all__ = ['PaymentRule']


class PaymentRule(BaseDataClass):
  """
  A class defining the payment calculation rule. As of FpML 5.10, percentage rule is the only calculation rule that has been specified as part of the standard.
  """
  percentageRule: Optional[PercentageRule] = Field(None, description="This attribute is not present as part of the FpML construct, as the payment rule is specialised by means of runtime type extension through the xsi:type.")
  """
  This attribute is not present as part of the FpML construct, as the payment rule is specialised by means of runtime type extension through the xsi:type.
  """

from cdm.product.common.settlement.PercentageRule import PercentageRule

PaymentRule.update_forward_refs()
