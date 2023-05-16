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

__all__ = ['ExtendibleProvision']

from cdm.base.staticdata.party.BuyerSeller import BuyerSeller

class ExtendibleProvision(BuyerSeller):
  """
  A data defining:  an option to extend an existing swap transaction on the specified exercise dates for a term ending on the specified new termination date. As a difference from FpML, it extends the BuyerSeller class, which represents the BuyerSeller.model.
  """
  americanExercise: Optional[AmericanExercise] = Field(None, description="American exercise. FpML implementations consists in an exercise substitution group.")
  """
  American exercise. FpML implementations consists in an exercise substitution group.
  """
  bermudaExercise: Optional[BermudaExercise] = Field(None, description="Bermuda exercise. FpML implementations consists in an exercise substitution group.")
  """
  Bermuda exercise. FpML implementations consists in an exercise substitution group.
  """
  callingParty: Optional[CallingPartyEnum] = Field(None, description="")
  europeanExercise: Optional[EuropeanExercise] = Field(None, description="European exercise. FpML implementations consists in an exercise substitution group.")
  """
  European exercise. FpML implementations consists in an exercise substitution group.
  """
  exerciseNotice: Optional[ExerciseNotice] = Field(None, description="Definition of the party to whom notice of exercise should be given.")
  """
  Definition of the party to whom notice of exercise should be given.
  """
  extendibleProvisionAdjustedDates: Optional[ExtendibleProvisionAdjustedDates] = Field(None, description="The adjusted dates associated with an extendible provision. These dates have been adjusted for any applicable business day convention.")
  """
  The adjusted dates associated with an extendible provision. These dates have been adjusted for any applicable business day convention.
  """
  extensionPeriod: Optional[AdjustableRelativeOrPeriodicDates] = Field(None, description="The period within which notice can be given that the contract will be extended.")
  """
  The period within which notice can be given that the contract will be extended.
  """
  extensionTerm: Optional[RelativeDateOffset] = Field(None, description="The length of each extension period relative to the effective date of the preceding contract.")
  """
  The length of each extension period relative to the effective date of the preceding contract.
  """
  followUpConfirmation: Optional[bool] = Field(None, description="A flag to indicate whether follow-up confirmation of exercise (written or electronic) is required following telephonic notice by the buyer to the seller or seller's agent.")
  """
  A flag to indicate whether follow-up confirmation of exercise (written or electronic) is required following telephonic notice by the buyer to the seller or seller's agent.
  """
  noticeDeadlineDateTime: Optional[datetime] = Field(None, description="A specific date and time for the notice deadline")
  """
  A specific date and time for the notice deadline
  """
  noticeDeadlinePeriod: Optional[RelativeDateOffset] = Field(None, description="Defines the minimum period before a contract is scheduled to terminate that notice can be given that it will terminate beyond the scheduled termination date.")
  """
  Defines the minimum period before a contract is scheduled to terminate that notice can be given that it will terminate beyond the scheduled termination date.
  """
  singlePartyOption: Optional[PartyRole] = Field(None, description="If the ability to extend the contract is not available to both parties then this component specifies the buyer and seller of the option.")
  """
  If the ability to extend the contract is not available to both parties then this component specifies the buyer and seller of the option.
  """
  
  @rosetta_condition
  def condition_0_ExtendibleProvisionExerciseNoticeReceiverParty(self):
    def _then_fn0():
      return all_elements(self.exerciseNotice.exerciseNoticeReceiver, "=", AncillaryRoleEnum.EXERCISE_NOTICE_RECEIVER_PARTY_EXTENDIBLE_PROVISION)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.exerciseNotice.exerciseNoticeReceiver) is not None), _then_fn0, _else_fn0)

from cdm.product.template.AmericanExercise import AmericanExercise
from cdm.product.template.BermudaExercise import BermudaExercise
from cdm.product.template.CallingPartyEnum import CallingPartyEnum
from cdm.product.template.EuropeanExercise import EuropeanExercise
from cdm.product.template.ExerciseNotice import ExerciseNotice
from cdm.product.template.ExtendibleProvisionAdjustedDates import ExtendibleProvisionAdjustedDates
from cdm.base.datetime.AdjustableRelativeOrPeriodicDates import AdjustableRelativeOrPeriodicDates
from cdm.base.datetime.RelativeDateOffset import RelativeDateOffset
from cdm.base.staticdata.party.PartyRole import PartyRole
from cdm.base.staticdata.party.AncillaryRoleEnum import AncillaryRoleEnum

ExtendibleProvision.update_forward_refs()
