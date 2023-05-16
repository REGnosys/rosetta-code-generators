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

__all__ = ['InterestAmount']


class InterestAmount(BaseDataClass):
  """
  A class to specify the application of Interest Amount with respect to the Delivery Amount and the Return Amount. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(ii).
  """
  deliveryAmount: DeliveryAmount = Field(..., description="The application of Interest Amount with respect the Delivery Amount. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(ii).")
  """
  The application of Interest Amount with respect the Delivery Amount. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(ii).
  """
  returnAmount: ReturnAmount = Field(..., description="The application of Interest Amount with respect the Return Amount. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(ii).")
  """
  The application of Interest Amount with respect the Return Amount. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(ii).
  """

from cdm.legaldocumentation.csa.DeliveryAmount import DeliveryAmount
from cdm.legaldocumentation.csa.ReturnAmount import ReturnAmount

InterestAmount.update_forward_refs()
