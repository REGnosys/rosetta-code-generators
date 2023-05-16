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

__all__ = ['EquityCorporateEvents']


class EquityCorporateEvents(BaseDataClass):
  """
  A class for defining the merger events and their treatment.
  """
  shareForCombined: ShareExtraordinaryEventEnum = Field(..., description="2018 ISDA CDM Equity Confirmation for Security Equity Swap: Merger Event (S-F-C) shall occur if a Merger Event occurs and the consideration for the relevant Security consists solely of Combined Consideration. | The consideration paid for the original shares following the Merger Event consists of both cash/securities and new shares.")
  """
  2018 ISDA CDM Equity Confirmation for Security Equity Swap: Merger Event (S-F-C) shall occur if a Merger Event occurs and the consideration for the relevant Security consists solely of Combined Consideration. | The consideration paid for the original shares following the Merger Event consists of both cash/securities and new shares.
  """
  shareForOther: ShareExtraordinaryEventEnum = Field(..., description="2018 ISDA CDM Equity Confirmation for Security Equity Swap: Merger Event (S-F-O) shall occur if a Merger Event occurs and the consideration for the relevant Security consists solely of Other Consideration. | The consideration paid for the original shares following the Merger Event consists wholly of cash/securities other than new shares.")
  """
  2018 ISDA CDM Equity Confirmation for Security Equity Swap: Merger Event (S-F-O) shall occur if a Merger Event occurs and the consideration for the relevant Security consists solely of Other Consideration. | The consideration paid for the original shares following the Merger Event consists wholly of cash/securities other than new shares.
  """
  shareForShare: ShareExtraordinaryEventEnum = Field(..., description="2018 ISDA CDM Equity Confirmation for Security Equity Swap: Merger Event (S-F-S) shall occur if a Merger Event occurs and the consideration for the relevant Security consists solely of Combined Consideration. | The consideration paid for the original shares following the Merger Event consists wholly of new shares.")
  """
  2018 ISDA CDM Equity Confirmation for Security Equity Swap: Merger Event (S-F-S) shall occur if a Merger Event occurs and the consideration for the relevant Security consists solely of Combined Consideration. | The consideration paid for the original shares following the Merger Event consists wholly of new shares.
  """

from cdm.observable.event.ShareExtraordinaryEventEnum import ShareExtraordinaryEventEnum

EquityCorporateEvents.update_forward_refs()
