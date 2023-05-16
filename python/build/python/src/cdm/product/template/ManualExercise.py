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

__all__ = ['ManualExercise']


class ManualExercise(BaseDataClass):
  """
  A class defining manual exercise, i.e. that the option buyer counterparty must give notice to the option seller of exercise.
  """
  exerciseNotice: Optional[ExerciseNotice] = Field(None, description="Definition of the party to whom notice of exercise should be given.")
  """
  Definition of the party to whom notice of exercise should be given.
  """
  fallbackExercise: Optional[bool] = Field(None, description="If fallback exercise is specified then the notional amount of the underlying swap, not previously exercised under the swaption, will be automatically exercised at the expiration time on the expiration date if at such time the buyer is in-the-money, provided that the difference between the settlement rate and the fixed rate under the relevant underlying swap is not less than one tenth of a percentage point (0.10% or 0.001). The term in-the-money is assumed to have the meaning defined in the 2000 ISDA Definitions, Section 17.4. In-the-money.")
  """
  If fallback exercise is specified then the notional amount of the underlying swap, not previously exercised under the swaption, will be automatically exercised at the expiration time on the expiration date if at such time the buyer is in-the-money, provided that the difference between the settlement rate and the fixed rate under the relevant underlying swap is not less than one tenth of a percentage point (0.10% or 0.001). The term in-the-money is assumed to have the meaning defined in the 2000 ISDA Definitions, Section 17.4. In-the-money.
  """
  
  @rosetta_condition
  def condition_0_ManualExerciseNoticeReceiverParty(self):
    def _then_fn0():
      return all_elements(self.exerciseNotice.exerciseNoticeReceiver, "=", AncillaryRoleEnum.EXERCISE_NOTICE_RECEIVER_PARTY_MANUAL)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.exerciseNotice.exerciseNoticeReceiver) is not None), _then_fn0, _else_fn0)

from cdm.product.template.ExerciseNotice import ExerciseNotice
from cdm.base.staticdata.party.AncillaryRoleEnum import AncillaryRoleEnum

ManualExercise.update_forward_refs()
