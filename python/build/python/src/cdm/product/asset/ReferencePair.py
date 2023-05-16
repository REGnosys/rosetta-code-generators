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

__all__ = ['ReferencePair']


class ReferencePair(BaseDataClass):
  entityType: AttributeWithMeta[EntityTypeEnum] | EntityTypeEnum = Field(..., description="Defines the reference entity types corresponding to a list of types in the ISDA First to Default documentation.")
  """
  Defines the reference entity types corresponding to a list of types in the ISDA First to Default documentation.
  """
  noReferenceObligation: Optional[bool] = Field(None, description="Used to indicate that there is no Reference Obligation associated with this Credit Default Swap and that there will never be one.")
  """
  Used to indicate that there is no Reference Obligation associated with this Credit Default Swap and that there will never be one.
  """
  referenceEntity: LegalEntity = Field(..., description="The corporate or sovereign entity on which you are buying or selling protection and any successor that assumes all or substantially all of its contractual and other obligations. It is vital to use the correct legal name of the entity and to be careful not to choose a subsidiary if you really want to trade protection on a parent company. Please note, Reference Entities cannot be senior or subordinated. It is the obligations of the Reference Entities that can be senior or subordinated. ISDA 2003 Term: Reference Entity.")
  """
  The corporate or sovereign entity on which you are buying or selling protection and any successor that assumes all or substantially all of its contractual and other obligations. It is vital to use the correct legal name of the entity and to be careful not to choose a subsidiary if you really want to trade protection on a parent company. Please note, Reference Entities cannot be senior or subordinated. It is the obligations of the Reference Entities that can be senior or subordinated. ISDA 2003 Term: Reference Entity.
  """
  referenceObligation: Optional[ReferenceObligation] = Field(None, description="The Reference Obligation is a financial instrument that is either issued or guaranteed by the reference entity. It serves to clarify the precise reference entity protection is being offered upon, and its legal position with regard to other related firms (parents/subsidiaries). Furthermore the Reference Obligation is ALWAYS deliverable and establishes the Pari Passu ranking (as the deliverable bonds must rank equal to the reference obligation). ISDA 2003 Term: Reference Obligation.")
  """
  The Reference Obligation is a financial instrument that is either issued or guaranteed by the reference entity. It serves to clarify the precise reference entity protection is being offered upon, and its legal position with regard to other related firms (parents/subsidiaries). Furthermore the Reference Obligation is ALWAYS deliverable and establishes the Pari Passu ranking (as the deliverable bonds must rank equal to the reference obligation). ISDA 2003 Term: Reference Obligation.
  """
  
  @rosetta_condition
  def condition_0_ReferenceChoice(self):
    """
    Choice rule to represent an FpML choice construct.
    """
    return self.check_one_of_constraint('referenceObligation', 'noReferenceObligation', necessity=True)

from cdm.base.staticdata.party.EntityTypeEnum import EntityTypeEnum
from cdm.base.staticdata.party.LegalEntity import LegalEntity
from cdm.product.asset.ReferenceObligation import ReferenceObligation

ReferencePair.update_forward_refs()
