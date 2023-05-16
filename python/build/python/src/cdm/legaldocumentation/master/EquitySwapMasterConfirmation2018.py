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

__all__ = ['EquitySwapMasterConfirmation2018']

from cdm.legaldocumentation.master.EquityMasterConfirmation import EquityMasterConfirmation

class EquitySwapMasterConfirmation2018(EquityMasterConfirmation):
  """
  Specification for the General Terms and Relationship Supplement Elections as provided in the 2018 ISDA CDM Equity Confirmation for Security Equity Swap.
  """
  equityCashSettlementDates: PaymentDates = Field(..., description="The parameters used to generate the payment date schedule, relative to the equityCalculationPeriod. Part 1 Section 12, 'Definitions', of the 2018 ISDA CDM Equity Confirmation. Para 73: 'Equity Cash Settlement Date' means each date falling one Settlement Cycle after an Equity Valuation Date; provided that if any such date is not a Settlement Currency Business Day, then such date shall be adjusted per Following Day Adjustment.")
  """
  The parameters used to generate the payment date schedule, relative to the equityCalculationPeriod. Part 1 Section 12, 'Definitions', of the 2018 ISDA CDM Equity Confirmation. Para 73: 'Equity Cash Settlement Date' means each date falling one Settlement Cycle after an Equity Valuation Date; provided that if any such date is not a Settlement Currency Business Day, then such date shall be adjusted per Following Day Adjustment.
  """
  linearInterpolationElection: InterpolationMethodEnum = Field(..., description="Part 1 Section 3, 'Floating Obligations', of the 2018 ISDA CDM Equity Confirmation. Para 3.3, 'Linear Interpolation': If the initial Calculation Period is not equal to the Designated Maturity, then the Linear Interpolation Election shall be as specified in the Relationship Supplement, unless otherwise specified in the Transaction Supplement.")
  """
  Part 1 Section 3, 'Floating Obligations', of the 2018 ISDA CDM Equity Confirmation. Para 3.3, 'Linear Interpolation': If the initial Calculation Period is not equal to the Designated Maturity, then the Linear Interpolation Election shall be as specified in the Relationship Supplement, unless otherwise specified in the Transaction Supplement.
  """
  pricingMethodElection: PriceReturnTerms = Field(..., description="Part 1 Section 5, 'Pricing', of the 2018 ISDA CDM Equity Confirmation, Para 5.1, 'Determining Prices': Each price in relation to a Pricing Date shall be determined pursuant to the specified Pricing Method. The relevant price specified under the column header 'Price' for a corresponding Pricing Date specified under the column header 'Pricing Date' shall be determined using the corresponding method specified under the column header 'Pricing Method'. Pricing Method for the final Equity Valuation Date shall be specified by the Final EVD Pricing Election and Pricing Method for any other Equity Valuation Date shall be 'Securities Close Pricing (Official)'")
  """
  Part 1 Section 5, 'Pricing', of the 2018 ISDA CDM Equity Confirmation, Para 5.1, 'Determining Prices': Each price in relation to a Pricing Date shall be determined pursuant to the specified Pricing Method. The relevant price specified under the column header 'Price' for a corresponding Pricing Date specified under the column header 'Pricing Date' shall be determined using the corresponding method specified under the column header 'Pricing Method'. Pricing Method for the final Equity Valuation Date shall be specified by the Final EVD Pricing Election and Pricing Method for any other Equity Valuation Date shall be 'Securities Close Pricing (Official)'
  """
  settlementTerms: SettlementTerms = Field(..., description="Part 1 Section 8, 'Settlement', of the 2018 ISDA CDM Equity Confirmation for Security Equity Swap. All Settlements are in Cash.")
  """
  Part 1 Section 8, 'Settlement', of the 2018 ISDA CDM Equity Confirmation for Security Equity Swap. All Settlements are in Cash.
  """
  typeOfSwapElection: ReturnTypeEnum = Field(..., description="Part 1 Section 4, 'Dividend Obligations', of the 2018 ISDA CDM Equity Confirmation, Para 4.2 'Dividend Returns': The Type Of Swap Election shall be 'Total Return', unless otherwise specified (as alternative 'Price Return') in the Transaction Supplement.")
  """
  Part 1 Section 4, 'Dividend Obligations', of the 2018 ISDA CDM Equity Confirmation, Para 4.2 'Dividend Returns': The Type Of Swap Election shall be 'Total Return', unless otherwise specified (as alternative 'Price Return') in the Transaction Supplement.
  """
  valuationDates: ValuationDates = Field(..., description="The parameters used to generate the 'Equity Valuation Dates' schedule, including the Effective Date and Termination Date for the Swap.")
  """
  The parameters used to generate the 'Equity Valuation Dates' schedule, including the Effective Date and Termination Date for the Swap.
  """

from cdm.product.common.schedule.PaymentDates import PaymentDates
from cdm.observable.asset.InterpolationMethodEnum import InterpolationMethodEnum
from cdm.product.asset.PriceReturnTerms import PriceReturnTerms
from cdm.product.common.settlement.SettlementTerms import SettlementTerms
from cdm.product.asset.ReturnTypeEnum import ReturnTypeEnum
from cdm.observable.asset.ValuationDates import ValuationDates

EquitySwapMasterConfirmation2018.update_forward_refs()
