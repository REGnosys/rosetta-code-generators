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

__all__ = ['AdditionalDisruptionEvents']


class AdditionalDisruptionEvents(BaseDataClass):
  """
  A type for defining the Additional Disruption Events.
  """
  changeInLaw: Optional[bool] = Field(None, description="2002 ISDA Equity Derivatives Definitions: Change in Law | 2018 ISDA CDM Equity Confirmation for Security Equity Swap: Change In Law | If true, then change in law is applicable.")
  """
  2002 ISDA Equity Derivatives Definitions: Change in Law | 2018 ISDA CDM Equity Confirmation for Security Equity Swap: Change In Law | If true, then change in law is applicable.
  """
  determiningParty: Optional[AncillaryRoleEnum] = Field(None, description="Specifies the party which determines additional disruption events.")
  """
  Specifies the party which determines additional disruption events.
  """
  failureToDeliver: Optional[bool] = Field(None, description="2002 ISDA Equity Derivatives Definitions: Failure to Deliver | Where the underlying is shares and the transaction is physically settled, then, if true, a failure to deliver the shares on the settlement date will not be an event of default for the purposes of the master agreement.")
  """
  2002 ISDA Equity Derivatives Definitions: Failure to Deliver | Where the underlying is shares and the transaction is physically settled, then, if true, a failure to deliver the shares on the settlement date will not be an event of default for the purposes of the master agreement.
  """
  foreignOwnershipEvent: Optional[bool] = Field(None, description="If true, then foreign ownership event is applicable.")
  """
  If true, then foreign ownership event is applicable.
  """
  hedgingDisruption: Optional[bool] = Field(None, description="2002 ISDA Equity Derivatives Definitions: Hedging Disruption | If true, then hedging disruption is applicable.")
  """
  2002 ISDA Equity Derivatives Definitions: Hedging Disruption | If true, then hedging disruption is applicable.
  """
  increasedCostOfHedging: Optional[bool] = Field(None, description="2002 ISDA Equity Derivatives Definitions: Increased Cost of Hedging | If true, then increased cost of hedging is applicable.")
  """
  2002 ISDA Equity Derivatives Definitions: Increased Cost of Hedging | If true, then increased cost of hedging is applicable.
  """
  increasedCostOfStockBorrow: Optional[bool] = Field(None, description="2002 ISDA Equity Derivatives Definitions: Increased Cost of Stock Borrow | If true, then increased cost of stock borrow is applicable.")
  """
  2002 ISDA Equity Derivatives Definitions: Increased Cost of Stock Borrow | If true, then increased cost of stock borrow is applicable.
  """
  initialStockLoanRate: Optional[Decimal] = Field(None, description="Specifies the initial stock loan rate for Increased Cost of Stock Borrow. A percentage of 5% is represented as 0.05.")
  """
  Specifies the initial stock loan rate for Increased Cost of Stock Borrow. A percentage of 5% is represented as 0.05.
  """
  insolvencyFiling: Optional[bool] = Field(None, description="2002 ISDA Equity Derivatives Definitions: Insolvency Filing | If true, then insolvency filing is applicable.")
  """
  2002 ISDA Equity Derivatives Definitions: Insolvency Filing | If true, then insolvency filing is applicable.
  """
  lossOfStockBorrow: Optional[bool] = Field(None, description="2002 ISDA Equity Derivatives Definitions: Loss of Stock Borrow | If true, then loss of stock borrow is applicable.")
  """
  2002 ISDA Equity Derivatives Definitions: Loss of Stock Borrow | If true, then loss of stock borrow is applicable.
  """
  maximumStockLoanRate: Optional[Decimal] = Field(None, description="Specifies the maximum stock loan rate for Loss of Stock Borrow. A percentage of 5% is represented as 0.05.")
  """
  Specifies the maximum stock loan rate for Loss of Stock Borrow. A percentage of 5% is represented as 0.05.
  """
  
  @rosetta_condition
  def condition_0_MaximumStockLoanRate(self):
    """
     FpML specifies the maximumStockLoanRate as a RestrictedPercentage, meaning that its value is comprised between 0 and 1.
    """
    def _then_fn0():
      return (all_elements(self.maximumStockLoanRate, ">=", 0) and all_elements(self.maximumStockLoanRate, "<=", 1))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.maximumStockLoanRate) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_InitialStockLoanRate(self):
    """
     FpML specifies the initialStockLoanRate as a RestrictedPercentage, meaning that its value is comprised between 0 and 1.
    """
    def _then_fn0():
      return (all_elements(self.initialStockLoanRate, ">=", 0) and all_elements(self.initialStockLoanRate, "<=", 1))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.initialStockLoanRate) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_DisruptionEventsDeterminingParty(self):
    def _then_fn0():
      return all_elements(self.determiningParty, "=", AncillaryRoleEnum.DISRUPTION_EVENTS_DETERMINING_PARTY)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.determiningParty) is not None), _then_fn0, _else_fn0)

from cdm.base.staticdata.party.AncillaryRoleEnum import AncillaryRoleEnum

AdditionalDisruptionEvents.update_forward_refs()
