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

__all__ = ['CreditSupportProvider']


class CreditSupportProvider(BaseDataClass):
  """
  Identification of party specific Credit Support Providers applicable to the document.
  """
  creditSupportProviderElection: List[CreditSupportProviderElection] = Field([], description="The party election of Credit Support Provider(s), if any.")
  """
  The party election of Credit Support Provider(s), if any.
  """
  @rosetta_condition
  def cardinality_creditSupportProviderElection(self):
    return check_cardinality(self.creditSupportProviderElection, 2, 2)
  

from cdm.legaldocumentation.master.CreditSupportProviderElection import CreditSupportProviderElection

CreditSupportProvider.update_forward_refs()
