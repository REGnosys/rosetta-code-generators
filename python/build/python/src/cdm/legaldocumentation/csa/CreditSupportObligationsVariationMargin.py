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

__all__ = ['CreditSupportObligationsVariationMargin']


class CreditSupportObligationsVariationMargin(BaseDataClass):
  """
  A class to specify the Credit Support Obligations applicable to the Variation Margin Credit Support Annex and which are common among the English, Japanese and New York governing laws. ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (c): Credit Support Obligations.
  """
  fxHaircut: Optional[str] = Field(None, description="The alternative definition for FX haircut percentage that applies to each party (as the pledgor/chargor/obligor) and item of Eligible Collateral unless this item is denominated in a Major Currency or in the Base Currency. ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (c)(v)(B): FX Haircut Percentage.")
  """
  The alternative definition for FX haircut percentage that applies to each party (as the pledgor/chargor/obligor) and item of Eligible Collateral unless this item is denominated in a Major Currency or in the Base Currency. ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (c)(v)(B): FX Haircut Percentage.
  """
  ineligibleCreditSupport: Optional[IneligibleCreditSupport] = Field(None, description="The parties to which the provisions of Paragraph 11(g) of the ISDA 2016 Credit Support Annex for Variation Margin will apply to. ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (c)(iii): Legally Ineligible Credit Support (VM).")
  """
  The parties to which the provisions of Paragraph 11(g) of the ISDA 2016 Credit Support Annex for Variation Margin will apply to. ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (c)(iii): Legally Ineligible Credit Support (VM).
  """
  majorCurrency: List[AttributeWithMeta[str] | str] = Field([], description="The additional currencies that are specified as Major Currency for the purpose of applying the FX Haircut Percentage. ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (c)(v)(B): FX Haircut Percentage.")
  """
  The additional currencies that are specified as Major Currency for the purpose of applying the FX Haircut Percentage. ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (c)(v)(B): FX Haircut Percentage.
  """

from cdm.legaldocumentation.csa.IneligibleCreditSupport import IneligibleCreditSupport

CreditSupportObligationsVariationMargin.update_forward_refs()
