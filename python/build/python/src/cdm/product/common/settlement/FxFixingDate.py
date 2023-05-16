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

__all__ = ['FxFixingDate']

from cdm.base.datetime.Offset import Offset

class FxFixingDate(Offset):
  """
  Extends the Offset structure to specify an FX fixing date as an offset to dates specified somewhere else in the document.
  """
  businessCenters: Optional[BusinessCenters] = Field(None, description="")
  businessCentersReference: Optional[AttributeWithReference | BusinessCenters] = Field(None, description="A reference to a set of financial business centers defined elsewhere in the document. This set of business centers is used to determine whether a particular day is a business day or not.")
  """
  A reference to a set of financial business centers defined elsewhere in the document. This set of business centers is used to determine whether a particular day is a business day or not.
  """
  businessDayConvention: Optional[BusinessDayConventionEnum] = Field(None, description="The convention for adjusting a date if it would otherwise fall on a day that is not a business day, as specified by an ISDA convention (e.g. Following, Precedent).")
  """
  The convention for adjusting a date if it would otherwise fall on a day that is not a business day, as specified by an ISDA convention (e.g. Following, Precedent).
  """
  dateRelativeToCalculationPeriodDates: Optional[DateRelativeToCalculationPeriodDates] = Field(None, description="The calculation period references on which settlements in non-deliverable currency are due and will then have to be converted according to the terms specified through the other parts of the nonDeliverableSettlement structure. Implemented for Brazilian-CDI swaps where it will refer to the termination date of the appropriate leg.")
  """
  The calculation period references on which settlements in non-deliverable currency are due and will then have to be converted according to the terms specified through the other parts of the nonDeliverableSettlement structure. Implemented for Brazilian-CDI swaps where it will refer to the termination date of the appropriate leg.
  """
  dateRelativeToPaymentDates: Optional[DateRelativeToPaymentDates] = Field(None, description="The payment date references on which settlements in non-deliverable currency are due and will then have to be converted according to the terms specified through the other parts of the nonDeliverableSettlement structure.")
  """
  The payment date references on which settlements in non-deliverable currency are due and will then have to be converted according to the terms specified through the other parts of the nonDeliverableSettlement structure.
  """
  dateRelativeToValuationDates: Optional[DateRelativeToValuationDates] = Field(None, description="The calculation period references on which settlements in non-deliverable currency are due and will then have to be converted according to the terms specified through the other parts of the nonDeliverableSettlement structure. Implemented for Brazilian-CDI swaps where it will refer to the termination date of the appropriate leg.")
  """
  The calculation period references on which settlements in non-deliverable currency are due and will then have to be converted according to the terms specified through the other parts of the nonDeliverableSettlement structure. Implemented for Brazilian-CDI swaps where it will refer to the termination date of the appropriate leg.
  """
  fxFixingDate: Optional[AdjustableOrRelativeDate] = Field(None, description="Describes the specific date when a non-deliverable forward or cash-settled option will 'fix' against a particular rate, which will be used to compute the ultimate cash settlement. This element should be omitted where a single, discrete fixing date cannot be identified e.g. on an american option, where fixing may occur at any date on a continuous range.  This attribute was formerly part of 'fxSettlementTerms', which is now being harmonised into a common 'CashSettlementTerms' that includes a 'ValuationDate'.")
  """
  Describes the specific date when a non-deliverable forward or cash-settled option will 'fix' against a particular rate, which will be used to compute the ultimate cash settlement. This element should be omitted where a single, discrete fixing date cannot be identified e.g. on an american option, where fixing may occur at any date on a continuous range.  This attribute was formerly part of 'fxSettlementTerms', which is now being harmonised into a common 'CashSettlementTerms' that includes a 'ValuationDate'.
  """
  
  @rosetta_condition
  def condition_0_BusinessCentersChoice(self):
    """
    condition to represent an FpML choice construct.
    """
    return self.check_one_of_constraint('businessCenters', 'businessCentersReference', necessity=False)
  
  @rosetta_condition
  def condition_1_DateChoice(self):
    """
    condition to represent an FpML choice construct.
    """
    return self.check_one_of_constraint('dateRelativeToPaymentDates', 'dateRelativeToCalculationPeriodDates', 'dateRelativeToValuationDates', 'fxFixingDate', necessity=True)

from cdm.base.datetime.BusinessCenters import BusinessCenters
from cdm.base.datetime.BusinessDayConventionEnum import BusinessDayConventionEnum
from cdm.product.common.schedule.DateRelativeToCalculationPeriodDates import DateRelativeToCalculationPeriodDates
from cdm.product.common.schedule.DateRelativeToPaymentDates import DateRelativeToPaymentDates
from cdm.product.common.schedule.DateRelativeToValuationDates import DateRelativeToValuationDates
from cdm.base.datetime.AdjustableOrRelativeDate import AdjustableOrRelativeDate

FxFixingDate.update_forward_refs()
