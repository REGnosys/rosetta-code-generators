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

__all__ = ['DistributionAndInterestPayment']


class DistributionAndInterestPayment(BaseDataClass):
  """
  A class to specify the Distributions and Interest Payment provisions applicable to the Japanese Law ISDA 2016 CSA for Initial Margin and the New York Law ISDA 2016 CSA for Variation Margin. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n): Distributions and Interest Payment (IM). | ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (i): Distributions and Interest Payment (VM).
  """
  alternativeProvision: Optional[str] = Field(None, description="When the alternative provision clause is specified, it means that the ISDA CSA Japanese Law provisions specified in Paragraph 6(c)(ii) don't apply and are overwritten by this election. When it is not specified, it means that the ISDA CSA Japanese Law provisions specified in Paragraph 6(c)(ii) apply. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(iv): Alternative to Interest Amount (IM) and Interest Payment (IM). | ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (i)(iv): Alternative to Interest Amount (VM) and Interest Payment (VM).")
  """
  When the alternative provision clause is specified, it means that the ISDA CSA Japanese Law provisions specified in Paragraph 6(c)(ii) don't apply and are overwritten by this election. When it is not specified, it means that the ISDA CSA Japanese Law provisions specified in Paragraph 6(c)(ii) apply. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(iv): Alternative to Interest Amount (IM) and Interest Payment (IM). | ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (i)(iv): Alternative to Interest Amount (VM) and Interest Payment (VM).
  """
  dailyInterestCompounding: bool = Field(..., description="Daily interest compounding is applicable when True, and not applicable when False. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(iii): Other Interest Elections. | ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (i)(iii): Other Interest Elections.")
  """
  Daily interest compounding is applicable when True, and not applicable when False. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(iii): Other Interest Elections. | ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (i)(iii): Other Interest Elections.
  """
  interestAdjustment: InterestAdjustment = Field(..., description="To election to specify whether the Interest Adjustment is applicable and what its periodicity is. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(ii). | ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (i)(ii): Transfer of Interest Payment (VM) or application of Interest Amount (VM).")
  """
  To election to specify whether the Interest Adjustment is applicable and what its periodicity is. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(ii). | ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (i)(ii): Transfer of Interest Payment (VM) or application of Interest Amount (VM).
  """
  interestAmount: InterestAmount = Field(..., description="The application of Interest Amount with respect to the Delivery Amount and the Return Amount. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(ii).")
  """
  The application of Interest Amount with respect to the Delivery Amount and the Return Amount. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(ii).
  """
  interestPaymentNetting: bool = Field(..., description="The Interest Payment Netting is applicable when True. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(ii): Transfer of Interest Payment (IM) or application of Interest Amount (IM). | ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (i)(ii): Transfer of Interest Payment (VM) or application of Interest Amount (VM).")
  """
  The Interest Payment Netting is applicable when True. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(ii): Transfer of Interest Payment (IM) or application of Interest Amount (IM). | ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (i)(ii): Transfer of Interest Payment (VM) or application of Interest Amount (VM).
  """
  interestPaymentTransfer: bool = Field(..., description="The Interest Payment Transfer is applicable when True. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(ii): Transfer of Interest Payment (IM) or application of Interest Amount (IM). | ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (i)(ii): Transfer of Interest Payment (VM) or application of Interest Amount (VM).")
  """
  The Interest Payment Transfer is applicable when True. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(ii): Transfer of Interest Payment (IM) or application of Interest Amount (IM). | ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (i)(ii): Transfer of Interest Payment (VM) or application of Interest Amount (VM).
  """
  interestRate: List[EligibleCurrencyInterestRate] = Field([], description="The interest rate associated with initial or variation margin collateral, depending upon the type of credit agreement that this election is associated with. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(i): Interest Rate (IM). | ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (i)(i): Interest Rate (VM).")
  """
  The interest rate associated with initial or variation margin collateral, depending upon the type of credit agreement that this election is associated with. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(i): Interest Rate (IM). | ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (i)(i): Interest Rate (VM).
  """
  @rosetta_condition
  def cardinality_interestRate(self):
    return check_cardinality(self.interestRate, 1, None)
  
  negativeInterest: bool = Field(..., description="Negative Interest is applicable when True, and not applicable when False. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(iii): Other Interest Elections. | ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (i)(iii): Other Interest Elections.")
  """
  Negative Interest is applicable when True, and not applicable when False. ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(iii): Other Interest Elections. | ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (i)(iii): Other Interest Elections.
  """

from cdm.legaldocumentation.csa.InterestAdjustment import InterestAdjustment
from cdm.legaldocumentation.csa.InterestAmount import InterestAmount
from cdm.legaldocumentation.csa.EligibleCurrencyInterestRate import EligibleCurrencyInterestRate

DistributionAndInterestPayment.update_forward_refs()
