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

__all__ = ['CoveredTransactions']


class CoveredTransactions(BaseDataClass):
  """
  Specification of Transactions covered by the legal agreement.
  """
  additionalObligations: List[AdditionalObligations] = Field([], description="The party specific additional obligations applicable to the document.")
  """
  The party specific additional obligations applicable to the document.
  """
  @rosetta_condition
  def cardinality_additionalObligations(self):
    return check_cardinality(self.additionalObligations, 0, 2)
  
  bespokeCoveredTransactions: List[str] = Field([], description="Covered Transactions when not expressed using the ISDA taxonomy.")
  """
  Covered Transactions when not expressed using the ISDA taxonomy.
  """
  @rosetta_condition
  def cardinality_bespokeCoveredTransactions(self):
    return check_cardinality(self.bespokeCoveredTransactions, 1, None)
  
  coveredTransactions: List[ProductTaxonomy] = Field([], description="Covered Transactions when expressed using the ISDA taxonomy.")
  """
  Covered Transactions when expressed using the ISDA taxonomy.
  """
  @rosetta_condition
  def cardinality_coveredTransactions(self):
    return check_cardinality(self.coveredTransactions, 1, None)
  
  exposure: Optional[str] = Field(None, description="The bespoke definition of exposure for Covered Transactions as part of the agreement.")
  """
  The bespoke definition of exposure for Covered Transactions as part of the agreement.
  """
  inclusionDate: date = Field(..., description="Includes any Transaction specified below that is entered into on or after the specified date.")
  """
  Includes any Transaction specified below that is entered into on or after the specified date.
  """

from cdm.legaldocumentation.csa.AdditionalObligations import AdditionalObligations
from cdm.base.staticdata.asset.common.ProductTaxonomy import ProductTaxonomy

CoveredTransactions.update_forward_refs()
