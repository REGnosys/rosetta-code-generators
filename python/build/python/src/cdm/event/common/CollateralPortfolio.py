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

__all__ = ['CollateralPortfolio']


class CollateralPortfolio(BaseDataClass):
  """
  Represents common attributes to define the details of collateral assets, to be used in margin call messaging and contribute to collateral balances e.g securities in a collateral account.
  """
  collateralBalance: List[CollateralBalance] = Field([], description="Represents the populated or calculated collateral aggregate balance amount for the collateral portfolio.")
  """
  Represents the populated or calculated collateral aggregate balance amount for the collateral portfolio.
  """
  collateralPosition: List[CollateralPosition] = Field([], description="Specifies the individual components of the collateral positions in the collateral portfolio.")
  """
  Specifies the individual components of the collateral positions in the collateral portfolio.
  """
  legalAgreement: Optional[AttributeWithReference | LegalAgreement] = Field(None, description=" The specification of a legal agreement between two parties governing the collateral relationship such as Credit Support Agreement or Collateral Transfer Agreement etc. (NB: this can be provided by reference to a global key for each LegalAgreement object).")
  """
   The specification of a legal agreement between two parties governing the collateral relationship such as Credit Support Agreement or Collateral Transfer Agreement etc. (NB: this can be provided by reference to a global key for each LegalAgreement object).
  """
  portfolioIdentifier: Optional[Identifier] = Field(None, description="Specifies a unique identifier for a set of collateral positions in a portfolio.")
  """
  Specifies a unique identifier for a set of collateral positions in a portfolio.
  """

from cdm.event.common.CollateralBalance import CollateralBalance
from cdm.event.common.CollateralPosition import CollateralPosition
from cdm.legaldocumentation.common.LegalAgreement import LegalAgreement
from cdm.base.staticdata.identifier.Identifier import Identifier

CollateralPortfolio.update_forward_refs()
