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

__all__ = ['ExecutionLocation']


class ExecutionLocation(BaseDataClass):
  """
  A class to specify execution location terms of a Security Agreement
  """
  dutyPayer: Optional[str] = Field(None, description="The payer of documentary duty")
  """
  The payer of documentary duty
  """
  dutyPayerLanguage: Optional[str] = Field(None, description="Bespoke terms specific to the payment of documentary duty")
  """
  Bespoke terms specific to the payment of documentary duty
  """
  dutyPaymentDate: Optional[date] = Field(None, description="The date that documentary duty will be paid")
  """
  The date that documentary duty will be paid
  """
  dutyPaymentLanguage: Optional[str] = Field(None, description="Bespoke terms specific to the date that documentary duty will be paid")
  """
  Bespoke terms specific to the date that documentary duty will be paid
  """
  executionLocation: ExecutionLocationEnum = Field(..., description="The execution location of the agreement")
  """
  The execution location of the agreement
  """
  otherLanguage: Optional[str] = Field(None, description="Bespoke execution location language to be included when specified.")
  """
  Bespoke execution location language to be included when specified.
  """
  
  @rosetta_condition
  def condition_0_DutyPayerLanguage(self):
    """
    A data rule to enforce that Duty Payer Language should only be specified when required
    """
    def _then_fn0():
      return ((self.dutyPayerLanguage) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.dutyPayer, "=", "Specify"), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_DutyPaymentLanguage(self):
    """
    A data rule to enforce that Duty Payment Language should be absent when a Duty Payment date is provided
    """
    def _then_fn0():
      return ((self.dutyPaymentLanguage) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.dutyPaymentDate) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_OtherLanguage(self):
    """
    A data rule to enforce that bespoke execution language must be included if non-standard execution language is specified.
    """
    def _then_fn0():
      return ((self.otherLanguage) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.executionLocation, "=", ExecutionLocationEnum.OTHER_LOCATION), _then_fn0, _else_fn0)

from cdm.legaldocumentation.common.ExecutionLocationEnum import ExecutionLocationEnum

ExecutionLocation.update_forward_refs()
