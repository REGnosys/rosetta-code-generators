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

__all__ = ['PrincipalPaymentSchedule']


class PrincipalPaymentSchedule(BaseDataClass):
  """
  Describe dates schedules for Principal Exchanges and related role of the parties when known.
  """
  finalPrincipalPayment: Optional[PrincipalPayment] = Field(None, description="Principal Payment at Trade maturity")
  """
  Principal Payment at Trade maturity
  """
  initialPrincipalPayment: Optional[PrincipalPayment] = Field(None, description="Principal Payment made at Trade inception.")
  """
  Principal Payment made at Trade inception.
  """
  intermediatePrincipalPayment: Optional[AdjustableRelativeOrPeriodicDates] = Field(None, description="Principal Payment as part of the Trade lifecycle e.g. as part of notional reset adjustements in a Cross Currency Swap with a varying notional leg.")
  """
  Principal Payment as part of the Trade lifecycle e.g. as part of notional reset adjustements in a Cross Currency Swap with a varying notional leg.
  """

from cdm.product.common.settlement.PrincipalPayment import PrincipalPayment
from cdm.base.datetime.AdjustableRelativeOrPeriodicDates import AdjustableRelativeOrPeriodicDates

PrincipalPaymentSchedule.update_forward_refs()
