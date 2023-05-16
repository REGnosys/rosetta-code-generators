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

__all__ = ['BrokerConfirmation']


class BrokerConfirmation(BaseDataClass):
  """
  Identifies the market sector in which the trade has been arranged.
  """
  brokerConfirmationType: AttributeWithMeta[BrokerConfirmationTypeEnum] | BrokerConfirmationTypeEnum = Field(..., description="The type of broker confirmation executed between the parties.")
  """
  The type of broker confirmation executed between the parties.
  """

from cdm.legaldocumentation.contract.BrokerConfirmationTypeEnum import BrokerConfirmationTypeEnum

BrokerConfirmation.update_forward_refs()
