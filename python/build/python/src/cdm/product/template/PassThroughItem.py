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

__all__ = ['PassThroughItem']


class PassThroughItem(BaseDataClass):
  """
  Class to represent a single pass through payment.
  """
  passThroughPercentage: Decimal = Field(..., description="Percentage of payments from the underlier which are passed through.")
  """
  Percentage of payments from the underlier which are passed through.
  """
  payerReceiver: PayerReceiver = Field(..., description="This attribute doesn't exists in the FpML construct, which makes use of the PayerReceiver.model group.")
  """
  This attribute doesn't exists in the FpML construct, which makes use of the PayerReceiver.model group.
  """

from cdm.base.staticdata.party.PayerReceiver import PayerReceiver

PassThroughItem.update_forward_refs()
