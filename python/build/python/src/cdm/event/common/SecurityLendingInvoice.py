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

__all__ = ['SecurityLendingInvoice']


class SecurityLendingInvoice(BaseDataClass):
  """
  Specifies the information required for inclusion in a securities lending billing invoice.
  """
  billingEndDate: date = Field(..., description="The ending date of the period described by this invoice")
  """
  The ending date of the period described by this invoice
  """
  billingRecord: List[BillingRecord] = Field([], description="The billing records contained within the invoice")
  """
  The billing records contained within the invoice
  """
  @rosetta_condition
  def cardinality_billingRecord(self):
    return check_cardinality(self.billingRecord, 1, None)
  
  billingStartDate: date = Field(..., description="The starting date of the period described by this invoice")
  """
  The starting date of the period described by this invoice
  """
  billingSummary: List[BillingSummary] = Field([], description="The billing summaries contained within the invoice")
  """
  The billing summaries contained within the invoice
  """
  @rosetta_condition
  def cardinality_billingSummary(self):
    return check_cardinality(self.billingSummary, 1, None)
  
  receivingParty: Party = Field(..., description="The party receiving the invoice")
  """
  The party receiving the invoice
  """
  sendingParty: Party = Field(..., description="The party issuing the invoice")
  """
  The party issuing the invoice
  """

from cdm.event.common.BillingRecord import BillingRecord
from cdm.event.common.BillingSummary import BillingSummary
from cdm.base.staticdata.party.Party import Party

SecurityLendingInvoice.update_forward_refs()
