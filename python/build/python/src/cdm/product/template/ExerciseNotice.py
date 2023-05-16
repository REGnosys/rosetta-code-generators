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

__all__ = ['ExerciseNotice']


class ExerciseNotice(BaseDataClass):
  """
  Defines to whom and where notice of execution should be given. The exerciseNoticeGiver refers to one or both of the principal parties of the trade. If present the exerciseNoticeReceiver refers to a party, other than the principal party, to whom notice should be given.
  """
  businessCenter: AttributeWithMeta[BusinessCenterEnum] | BusinessCenterEnum = Field(..., description="Specifies the location where the exercise must be reported, e.g. where the exercise notice receiver is based.")
  """
  Specifies the location where the exercise must be reported, e.g. where the exercise notice receiver is based.
  """
  exerciseNoticeGiver: ExerciseNoticeGiverEnum = Field(..., description="Specifies the principal party of the trade that has the right to exercise.")
  """
  Specifies the principal party of the trade that has the right to exercise.
  """
  exerciseNoticeReceiver: Optional[AncillaryRoleEnum] = Field(None, description="Specifies the party to which notice of exercise should be given, e.g. by the buyer of the option. Although in many cases it is the buyer of the option who sends the exercise notice to the seller of the option, this component is reused, e.g. in case of OptionEarlyTermination, either or both parties have the right to exercise.")
  """
  Specifies the party to which notice of exercise should be given, e.g. by the buyer of the option. Although in many cases it is the buyer of the option who sends the exercise notice to the seller of the option, this component is reused, e.g. in case of OptionEarlyTermination, either or both parties have the right to exercise.
  """

from cdm.base.datetime.BusinessCenterEnum import BusinessCenterEnum
from cdm.product.template.ExerciseNoticeGiverEnum import ExerciseNoticeGiverEnum
from cdm.base.staticdata.party.AncillaryRoleEnum import AncillaryRoleEnum

ExerciseNotice.update_forward_refs()
