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

__all__ = ['DividendApplicability']


class DividendApplicability(BaseDataClass):
  """
  The parameters which define whether dividends are applicable
  """
  additionalDividends: Optional[bool] = Field(None, description="If present and true, then additional dividends are applicable.")
  """
  If present and true, then additional dividends are applicable.
  """
  allDividends: Optional[bool] = Field(None, description="Represents the European Master Confirmation value of 'All Dividends' which, when applicable, signifies that, for a given Ex-Date, the daily observed Share Price for that day is adjusted (reduced) by the cash dividend and/or the cash value of any non cash dividend per Share (including Extraordinary Dividends) declared by the Issuer. All Dividends in accordance with the ISDA 2002 Equity Derivatives Definitions.")
  """
  Represents the European Master Confirmation value of 'All Dividends' which, when applicable, signifies that, for a given Ex-Date, the daily observed Share Price for that day is adjusted (reduced) by the cash dividend and/or the cash value of any non cash dividend per Share (including Extraordinary Dividends) declared by the Issuer. All Dividends in accordance with the ISDA 2002 Equity Derivatives Definitions.
  """
  optionsExchangeDividends: Optional[bool] = Field(None, description="If present and true, then options exchange dividends are applicable.")
  """
  If present and true, then options exchange dividends are applicable.
  """


DividendApplicability.update_forward_refs()
