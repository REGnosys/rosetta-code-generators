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

__all__ = ['SecurityFinancePayout']

from cdm.product.common.settlement.PayoutBase import PayoutBase

class SecurityFinancePayout(PayoutBase):
  """
  Security payout specification in case the product payout involves some form of security collateral, as in a securities financing transaction.
  """
  collateralProvisions: CollateralProvisions = Field(..., description="Specifies collateral provisions for a Security Finance transaction, including Collateral Type and Margin Percentage.")
  """
  Specifies collateral provisions for a Security Finance transaction, including Collateral Type and Margin Percentage.
  """
  dividendTerms: Optional[DividendTerms] = Field(None, description="Specifies the terms under which dividends received by the borrower are passed through to the lender.")
  """
  Specifies the terms under which dividends received by the borrower are passed through to the lender.
  """
  durationType: Duration = Field(..., description="Specifies the Duration Terms of the Security Finance transaction. e.g. Open or Term.")
  """
  Specifies the Duration Terms of the Security Finance transaction. e.g. Open or Term.
  """
  minimumFee: Optional[Money] = Field(None, description="A contractual minimum amount which the borrower will pay, regardless of the duration of the loan. A mechanism for making sure that a trade generates enough income.")
  """
  A contractual minimum amount which the borrower will pay, regardless of the duration of the loan. A mechanism for making sure that a trade generates enough income.
  """
  securityFinanceLeg: List[SecurityFinanceLeg] = Field([], description="Each SecurityLeg represent a buy/sell at different dates, typically 1 near leg and 1 far leg in a securities financing transaction.")
  """
  Each SecurityLeg represent a buy/sell at different dates, typically 1 near leg and 1 far leg in a securities financing transaction.
  """
  @rosetta_condition
  def cardinality_securityFinanceLeg(self):
    return check_cardinality(self.securityFinanceLeg, 1, None)
  
  securityInformation: Product = Field(..., description="Specifies the reference asset.  This is The base type which all products extend (similar to FpML model). Within SecurityPayout we include a condition which validates that the product must be a Security (see below condition 'ProductMustBeSecurity').")
  """
  Specifies the reference asset.  This is The base type which all products extend (similar to FpML model). Within SecurityPayout we include a condition which validates that the product must be a Security (see below condition 'ProductMustBeSecurity').
  """
  
  @rosetta_condition
  def condition_0_Quantity(self):
    """
    When there is an OptionPayout the quantity can be expressed as part of the payoutQuantity, or as part of the underlier in the case of a Swaption.  For all other payouts that extend PayoutBase the payoutQuantity is a mandatory attribute.
    """
    return ((self.priceQuantity) is not None)
  
  @rosetta_condition
  def condition_1_ProductMustBeSecurity(self):
    """
    Validates that the reference asset must be a security.
    """
    return ((self.securityInformation.security) is not None)

from cdm.product.template.CollateralProvisions import CollateralProvisions
from cdm.product.template.DividendTerms import DividendTerms
from cdm.product.template.Duration import Duration
from cdm.observable.asset.Money import Money
from cdm.product.template.SecurityFinanceLeg import SecurityFinanceLeg
from cdm.product.template.Product import Product

SecurityFinancePayout.update_forward_refs()
