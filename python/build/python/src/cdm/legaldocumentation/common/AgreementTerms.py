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

__all__ = ['AgreementTerms']


class AgreementTerms(BaseDataClass):
  """
  Specification of the content of a legal agreement.
  """
  agreement: Agreement = Field(..., description="Specification of the standard set of terms that define a legal agreement.")
  """
  Specification of the standard set of terms that define a legal agreement.
  """
  clauseLibrary: Optional[bool] = Field(None, description="Specification of whether the agreement terms have been negotiated using the clause library methodology.")
  """
  Specification of whether the agreement terms have been negotiated using the clause library methodology.
  """
  counterparty: List[Counterparty] = Field([], description="Specification of the roles of the counterparties to the agreement.")
  """
  Specification of the roles of the counterparties to the agreement.
  """
  @rosetta_condition
  def cardinality_counterparty(self):
    return check_cardinality(self.counterparty, 2, 2)
  

from cdm.legaldocumentation.common.Agreement import Agreement
from cdm.base.staticdata.party.Counterparty import Counterparty

AgreementTerms.update_forward_refs()
