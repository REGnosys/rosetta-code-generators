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

__all__ = ['SettlementOrigin']


class SettlementOrigin(BaseDataClass):
  """
  Defines the origin to the transfer as a reference for lineage purposes, whether it originated from trade level settlement terms or from payment terms on an economic payout.
  """
  commodityPayout: Optional[AttributeWithReference | CommodityPayout] = Field(None, description="Represents a reference to an Commodity Payout.")
  """
  Represents a reference to an Commodity Payout.
  """
  creditDefaultPayout: Optional[AttributeWithReference | CreditDefaultPayout] = Field(None, description="Represents a reference to a Credit Default Payout.")
  """
  Represents a reference to a Credit Default Payout.
  """
  fixedPricePayout: Optional[AttributeWithReference | FixedPricePayout] = Field(None, description="Represents a reference to a Fixed Price Payout")
  """
  Represents a reference to a Fixed Price Payout
  """
  forwardPayout: Optional[AttributeWithReference | ForwardPayout] = Field(None, description="Represents a reference to a Forward Payout.")
  """
  Represents a reference to a Forward Payout.
  """
  interestRatePayout: Optional[AttributeWithReference | InterestRatePayout] = Field(None, description="Represents a reference to an Interest Rate Payout.")
  """
  Represents a reference to an Interest Rate Payout.
  """
  optionPayout: Optional[AttributeWithReference | OptionPayout] = Field(None, description="Represents a reference to an Option Payout.")
  """
  Represents a reference to an Option Payout.
  """
  performancePayout: Optional[AttributeWithReference | PerformancePayout] = Field(None, description="Represents a reference to a Performance Payout.")
  """
  Represents a reference to a Performance Payout.
  """
  securityFinancePayout: Optional[AttributeWithReference | SecurityFinancePayout] = Field(None, description="Represents a reference to a Security Lending Payout.")
  """
  Represents a reference to a Security Lending Payout.
  """
  settlementTerms: Optional[AttributeWithReference | SettlementTerms] = Field(None, description="Represents a reference to settlement terms, which may have been specified at execution.")
  """
  Represents a reference to settlement terms, which may have been specified at execution.
  """
  
  @rosetta_condition
  def condition_0_(self):
    return self.check_one_of_constraint('commodityPayout', 'creditDefaultPayout', 'forwardPayout', 'interestRatePayout', 'optionPayout', 'securityFinancePayout', 'settlementTerms', 'performancePayout', 'fixedPricePayout', necessity=True)

from cdm.product.asset.CommodityPayout import CommodityPayout
from cdm.product.asset.CreditDefaultPayout import CreditDefaultPayout
from cdm.product.template.FixedPricePayout import FixedPricePayout
from cdm.product.template.ForwardPayout import ForwardPayout
from cdm.product.asset.InterestRatePayout import InterestRatePayout
from cdm.product.template.OptionPayout import OptionPayout
from cdm.product.template.PerformancePayout import PerformancePayout
from cdm.product.template.SecurityFinancePayout import SecurityFinancePayout
from cdm.product.common.settlement.SettlementTerms import SettlementTerms

SettlementOrigin.update_forward_refs()
