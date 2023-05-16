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

__all__ = ['Collateral']


class Collateral(BaseDataClass):
  """
  A type for defining the obligations of the counterparty subject to credit support requirements.
  """
  collateralPortfolio: List[AttributeWithReference | CollateralPortfolio] = Field([], description="The collateral portfolios which contain the collateral which covers a trade. (NB: this can be provided by reference to a global key for each CollateralPortfolio object)")
  """
  The collateral portfolios which contain the collateral which covers a trade. (NB: this can be provided by reference to a global key for each CollateralPortfolio object)
  """
  independentAmount: Optional[IndependentAmount] = Field(None, description="Independent Amount is an amount that usually less creditworthy counterparties are asked to provide. It can either be a fixed amount or a percentage of the Transaction's value. The Independent Amount can be: (i) transferred before any trading between the parties occurs (as a deposit at a third party's account or with the counterparty) or (ii) callable after trading has occurred (typically because a downgrade has occurred). In situation (i), the Independent Amount is not included in the calculation of Exposure, but in situation (ii), it is included in the calculation of Exposure. Thus, for situation (ii), the Independent Amount may be transferred along with any collateral call. Independent Amount is a defined term in the ISDA Credit Support Annex. ('with respect to a party, the amount specified as such for that party in Paragraph 13; if no amount is specified, zero').")
  """
  Independent Amount is an amount that usually less creditworthy counterparties are asked to provide. It can either be a fixed amount or a percentage of the Transaction's value. The Independent Amount can be: (i) transferred before any trading between the parties occurs (as a deposit at a third party's account or with the counterparty) or (ii) callable after trading has occurred (typically because a downgrade has occurred). In situation (i), the Independent Amount is not included in the calculation of Exposure, but in situation (ii), it is included in the calculation of Exposure. Thus, for situation (ii), the Independent Amount may be transferred along with any collateral call. Independent Amount is a defined term in the ISDA Credit Support Annex. ('with respect to a party, the amount specified as such for that party in Paragraph 13; if no amount is specified, zero').
  """
  portfolioIdentifier: List[Identifier] = Field([], description="A list of identifiers pointing to the collateral portfolios which contain the collateral which covers a trade.")
  """
  A list of identifiers pointing to the collateral portfolios which contain the collateral which covers a trade.
  """
  
  @rosetta_condition
  def condition_0_Collateralchoice(self):
    return self.check_one_of_constraint('independentAmount', 'portfolioIdentifier', 'collateralPortfolio', necessity=False)

from cdm.event.common.CollateralPortfolio import CollateralPortfolio
from cdm.legaldocumentation.csa.IndependentAmount import IndependentAmount
from cdm.base.staticdata.identifier.Identifier import Identifier

Collateral.update_forward_refs()
