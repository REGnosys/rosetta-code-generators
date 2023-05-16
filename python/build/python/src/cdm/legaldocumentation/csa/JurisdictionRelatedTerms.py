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

__all__ = ['JurisdictionRelatedTerms']


class JurisdictionRelatedTerms(BaseDataClass):
  """
  A class to specify terms jurisdiction related terms.
  """
  belgianLawSecurityAgreement: Optional[bool] = Field(None, description="The qualification of whether the Belgian Law Security Agreement Addendum is deemed applicable by the parties (True) or not (False).")
  """
  The qualification of whether the Belgian Law Security Agreement Addendum is deemed applicable by the parties (True) or not (False).
  """
  exclusiveJurisdiction: Optional[bool] = Field(None, description="Classification of optional exclusive jurisdiction terms")
  """
  Classification of optional exclusive jurisdiction terms
  """
  frenchLawAddendum: Optional[FrenchLawAddendum] = Field(None, description="The French Law Addendum Provisions specific to the agreement.")
  """
  The French Law Addendum Provisions specific to the agreement.
  """
  japaneseSecuritiesProvisions: Optional[JapaneseSecuritiesProvisions] = Field(None, description="The Japanese Securities Provisions election.")
  """
  The Japanese Securities Provisions election.
  """
  juryWaiver: Optional[bool] = Field(None, description="The Jury Waiver conditions specific to the agreement.")
  """
  The Jury Waiver conditions specific to the agreement.
  """

from cdm.legaldocumentation.csa.FrenchLawAddendum import FrenchLawAddendum
from cdm.legaldocumentation.csa.JapaneseSecuritiesProvisions import JapaneseSecuritiesProvisions

JurisdictionRelatedTerms.update_forward_refs()
