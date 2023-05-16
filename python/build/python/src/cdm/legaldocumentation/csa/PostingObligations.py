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

__all__ = ['PostingObligations']


class PostingObligations(BaseDataClass):
  """
  A class to specify the collateral posting obligations of the security provider or security providers as specified in the corresponding agreement, for example, the New York Law ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (ii).
  """
  partyElection: List[PostingObligationsElection] = Field([], description="The specification of the collateral posting obligations for the security provider party(ies), for example, as specified under the terms of the ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (ii).")
  """
  The specification of the collateral posting obligations for the security provider party(ies), for example, as specified under the terms of the ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (ii).
  """
  @rosetta_condition
  def cardinality_partyElection(self):
    return check_cardinality(self.partyElection, 1, 2)
  
  securityProvider: str = Field(..., description="The security provider party(ies) to which the posting obligations apply to, which can be either one of the parties to the legal agreement, or both of those.")
  """
  The security provider party(ies) to which the posting obligations apply to, which can be either one of the parties to the legal agreement, or both of those.
  """

from cdm.legaldocumentation.csa.PostingObligationsElection import PostingObligationsElection

PostingObligations.update_forward_refs()
