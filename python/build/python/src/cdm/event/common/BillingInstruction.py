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

__all__ = ['BillingInstruction']


class BillingInstruction(BaseDataClass):
  """
  Specifies the instructions for creation of a Security Lending billing invoice.
  """
  billingEndDate: date = Field(..., description="The ending date of the period described by this invoice")
  """
  The ending date of the period described by this invoice
  """
  billingRecordInstruction: List[BillingRecordInstruction] = Field([], description="Instructions for creating the billing records contained within the invoice")
  """
  Instructions for creating the billing records contained within the invoice
  """
  @rosetta_condition
  def cardinality_billingRecordInstruction(self):
    return check_cardinality(self.billingRecordInstruction, 1, None)
  
  billingStartDate: date = Field(..., description="The starting date of the period described by this invoice")
  """
  The starting date of the period described by this invoice
  """
  billingSummary: List[BillingSummaryInstruction] = Field([], description="The billing summaries contained within the invoice")
  """
  The billing summaries contained within the invoice
  """
  receivingParty: Party = Field(..., description="The party receiving the invoice")
  """
  The party receiving the invoice
  """
  sendingParty: Party = Field(..., description="The party issuing the invoice")
  """
  The party issuing the invoice
  """

from cdm.event.common.BillingRecordInstruction import BillingRecordInstruction
from cdm.event.common.BillingSummaryInstruction import BillingSummaryInstruction
from cdm.base.staticdata.party.Party import Party

BillingInstruction.update_forward_refs()
