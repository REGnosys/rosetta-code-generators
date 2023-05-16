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

__all__ = ['CreditSupportDocument']


class CreditSupportDocument(BaseDataClass):
  """
  Identification of party specific Credit Support Documents applicable to the document.
  """
  creditSupportDocumentElection: List[CreditSupportDocumentElection] = Field([], description="The party election of Credit Support Document(s), if any.")
  """
  The party election of Credit Support Document(s), if any.
  """
  @rosetta_condition
  def cardinality_creditSupportDocumentElection(self):
    return check_cardinality(self.creditSupportDocumentElection, 2, 2)
  

from cdm.legaldocumentation.master.CreditSupportDocumentElection import CreditSupportDocumentElection

CreditSupportDocument.update_forward_refs()
