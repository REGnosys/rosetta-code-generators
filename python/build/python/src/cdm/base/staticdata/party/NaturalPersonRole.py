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

__all__ = ['NaturalPersonRole']


class NaturalPersonRole(BaseDataClass):
  """
  A class to specify the role(s) that natural person(s) may have in relation to the contract.
  """
  personReference: AttributeWithReference | NaturalPerson = Field(..., description="A reference to the natural person to whom the role refers to.")
  """
  A reference to the natural person to whom the role refers to.
  """
  role: List[AttributeWithMeta[NaturalPersonRoleEnum] | NaturalPersonRoleEnum] = Field([], description="FpML specifies a person role that is distinct from the party role.")
  """
  FpML specifies a person role that is distinct from the party role.
  """

from cdm.base.staticdata.party.NaturalPerson import NaturalPerson
from cdm.base.staticdata.party.NaturalPersonRoleEnum import NaturalPersonRoleEnum

NaturalPersonRole.update_forward_refs()
