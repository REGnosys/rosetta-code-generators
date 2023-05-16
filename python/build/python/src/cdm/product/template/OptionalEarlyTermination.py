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

__all__ = ['OptionalEarlyTermination']


class OptionalEarlyTermination(BaseDataClass):
  """
  A data defining:  an early termination provision where either or both parties have the right to exercise.
  """
  americanExercise: Optional[AmericanExercise] = Field(None, description="American exercise. FpML implementations consists in an exercise substitution group.")
  """
  American exercise. FpML implementations consists in an exercise substitution group.
  """
  bermudaExercise: Optional[BermudaExercise] = Field(None, description="Bermuda exercise. FpML implementations consists in an exercise substitution group.")
  """
  Bermuda exercise. FpML implementations consists in an exercise substitution group.
  """
  calculationAgent: Optional[CalculationAgent] = Field(None, description="The ISDA Calculation Agent responsible for performing duties associated with an optional early termination.")
  """
  The ISDA Calculation Agent responsible for performing duties associated with an optional early termination.
  """
  cashSettlement: Optional[SettlementTerms] = Field(None, description="If specified, this means that cash settlement is applicable to the transaction and defines the parameters associated with the cash settlement procedure. If not specified, then physical settlement is applicable.")
  """
  If specified, this means that cash settlement is applicable to the transaction and defines the parameters associated with the cash settlement procedure. If not specified, then physical settlement is applicable.
  """
  europeanExercise: Optional[EuropeanExercise] = Field(None, description="European exercise. FpML implementations consists in an exercise substitution group.")
  """
  European exercise. FpML implementations consists in an exercise substitution group.
  """
  exerciseNotice: List[ExerciseNotice] = Field([], description="Definition of the party to whom notice of exercise should be given.")
  """
  Definition of the party to whom notice of exercise should be given.
  """
  followUpConfirmation: Optional[bool] = Field(None, description="A flag to indicate whether follow-up confirmation of exercise (written or electronic) is required following telephonic notice by the buyer to the seller or seller's agent.")
  """
  A flag to indicate whether follow-up confirmation of exercise (written or electronic) is required following telephonic notice by the buyer to the seller or seller's agent.
  """
  mutualEarlyTermination: Optional[bool] = Field(None, description="Used for specifying whether the Mutual Early Termination Right that is detailed in the Master Confirmation will apply.")
  """
  Used for specifying whether the Mutual Early Termination Right that is detailed in the Master Confirmation will apply.
  """
  optionalEarlyTerminationAdjustedDates: Optional[OptionalEarlyTerminationAdjustedDates] = Field(None, description="An early termination provision to terminate the trade at fair value where one or both parties have the right to decide on termination.")
  """
  An early termination provision to terminate the trade at fair value where one or both parties have the right to decide on termination.
  """
  singlePartyOption: Optional[BuyerSeller] = Field(None, description="If optional early termination is not available to both parties then this component specifies the buyer and seller of the option. In FpML, this attribute is of type SinglePsrtyOption, which actually consists of the BuyerSeller.model.")
  """
  If optional early termination is not available to both parties then this component specifies the buyer and seller of the option. In FpML, this attribute is of type SinglePsrtyOption, which actually consists of the BuyerSeller.model.
  """
  
  @rosetta_condition
  def condition_0_ExerciseChoice(self):
    """
    condition to represent an FpML choice construct.
    """
    return self.check_one_of_constraint('americanExercise', 'bermudaExercise', 'europeanExercise', necessity=False)
  
  @rosetta_condition
  def condition_1_OptionalEarlyTerminationExerciseNoticeReceiverParty(self):
    def _then_fn0():
      return contains(self.exerciseNotice.exerciseNoticeReceiver, AncillaryRoleEnum.EXERCISE_NOTICE_RECEIVER_PARTY_OPTIONAL_EARLY_TERMINATION)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.exerciseNotice.exerciseNoticeReceiver) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_MandatoryEarlyTerminationCalculationAgent(self):
    def _then_fn0():
      return all_elements(self.calculationAgent.calculationAgentParty, "=", AncillaryRoleEnum.CALCULATION_AGENT_OPTIONAL_EARLY_TERMINATION)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.calculationAgent.calculationAgentParty) is not None), _then_fn0, _else_fn0)

from cdm.product.template.AmericanExercise import AmericanExercise
from cdm.product.template.BermudaExercise import BermudaExercise
from cdm.observable.asset.CalculationAgent import CalculationAgent
from cdm.product.common.settlement.SettlementTerms import SettlementTerms
from cdm.product.template.EuropeanExercise import EuropeanExercise
from cdm.product.template.ExerciseNotice import ExerciseNotice
from cdm.product.template.OptionalEarlyTerminationAdjustedDates import OptionalEarlyTerminationAdjustedDates
from cdm.base.staticdata.party.BuyerSeller import BuyerSeller
from cdm.base.staticdata.party.AncillaryRoleEnum import AncillaryRoleEnum

OptionalEarlyTermination.update_forward_refs()
