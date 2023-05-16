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

__all__ = ['NaturalPerson']


class NaturalPerson(BaseDataClass):
  """
  A class to represent the attributes that are specific to a natural person.
  """
  contactInformation: Optional[ContactInformation] = Field(None, description="The contact information for such person, when different from the contact information associated with the party.")
  """
  The contact information for such person, when different from the contact information associated with the party.
  """
  dateOfBirth: Optional[date] = Field(None, description="The natural person's date of birth.")
  """
  The natural person's date of birth.
  """
  firstName: Optional[str] = Field(None, description="The natural person's first name. It is optional in FpML.")
  """
  The natural person's first name. It is optional in FpML.
  """
  honorific: Optional[str] = Field(None, description="An honorific title, such as Mr., Ms., Dr. etc.")
  """
  An honorific title, such as Mr., Ms., Dr. etc.
  """
  initial: List[str] = Field([], description="The natural person's middle initial(s). If a middle initial is provided then a name should be absent.")
  """
  The natural person's middle initial(s). If a middle initial is provided then a name should be absent.
  """
  middleName: List[str] = Field([], description="The natural person's middle name(s). If a middle name is provided then an initial should be absent.")
  """
  The natural person's middle name(s). If a middle name is provided then an initial should be absent.
  """
  personId: List[AttributeWithMeta[PersonIdentifier] | PersonIdentifier] = Field([], description="The identifier associated with a person, e.g. the internal identification code.")
  """
  The identifier associated with a person, e.g. the internal identification code.
  """
  suffix: Optional[str] = Field(None, description="Name suffix, such as Jr., III, etc.")
  """
  Name suffix, such as Jr., III, etc.
  """
  surname: Optional[str] = Field(None, description="The natural person's surname.")
  """
  The natural person's surname.
  """
  
  @rosetta_condition
  def condition_0_NameOrIdChoice(self):
    return ((((self.firstName) is not None) and ((self.surname) is not None)) or ((self.personId) is not None))
  
  @rosetta_condition
  def condition_1_NaturalPersonChoice(self):
    """
    Choice rule to represent an FpML choice construct.
    """
    return self.check_one_of_constraint('middleName', 'initial', necessity=False)

from cdm.base.staticdata.party.ContactInformation import ContactInformation
from cdm.base.staticdata.party.PersonIdentifier import PersonIdentifier

NaturalPerson.update_forward_refs()
