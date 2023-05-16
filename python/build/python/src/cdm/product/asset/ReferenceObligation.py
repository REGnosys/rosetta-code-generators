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

__all__ = ['ReferenceObligation']


class ReferenceObligation(BaseDataClass):
  """
  A class to specify the reference obligation that is associated with a credit derivative instrument.
  """
  guarantor: Optional[LegalEntity] = Field(None, description="The party that guarantees by way of a contractual arrangement to pay the debts of an obligor if the obligor is unable to make the required payments itself. ISDA 2003 Term: Guarantor.")
  """
  The party that guarantees by way of a contractual arrangement to pay the debts of an obligor if the obligor is unable to make the required payments itself. ISDA 2003 Term: Guarantor.
  """
  guarantorReference: Optional[str] = Field(None, description="A pointer style reference to a reference entity defined elsewhere in the document. Used when the reference entity is the guarantor.")
  """
  A pointer style reference to a reference entity defined elsewhere in the document. Used when the reference entity is the guarantor.
  """
  loan: Optional[Loan] = Field(None, description="Identifies the underlying asset when it is a loan.")
  """
  Identifies the underlying asset when it is a loan.
  """
  primaryObligor: Optional[LegalEntity] = Field(None, description="The entity primarily responsible for repaying debt to a creditor as a result of borrowing or issuing bonds. ISDA 2003 Term: Primary Obligor.")
  """
  The entity primarily responsible for repaying debt to a creditor as a result of borrowing or issuing bonds. ISDA 2003 Term: Primary Obligor.
  """
  primaryObligorReference: Optional[AttributeWithReference | LegalEntity] = Field(None, description="A pointer style reference to a reference entity defined elsewhere in the document. Used when the reference entity is the primary obligor.")
  """
  A pointer style reference to a reference entity defined elsewhere in the document. Used when the reference entity is the primary obligor.
  """
  security: Optional[Security] = Field(None, description="Identifies the underlying asset when it is a security, such as a bond or convertible bond. The security data type requires one or more productIdentifiers, specificaiton of the security type (e.g. debt), and includes optional attributes to specify a debt class, such as asset-backed, as well as seniority.")
  """
  Identifies the underlying asset when it is a security, such as a bond or convertible bond. The security data type requires one or more productIdentifiers, specificaiton of the security type (e.g. debt), and includes optional attributes to specify a debt class, such as asset-backed, as well as seniority.
  """
  standardReferenceObligation: Optional[bool] = Field(None, description="Indicates if the reference obligation is a Standard Reference Obligation. ISDA 2014 Term: Standard Reference Obligation.")
  """
  Indicates if the reference obligation is a Standard Reference Obligation. ISDA 2014 Term: Standard Reference Obligation.
  """
  
  @rosetta_condition
  def condition_0_AssetChoice(self):
    """
    Represents the choice in a CDS contract.
    """
    return self.check_one_of_constraint('security', 'loan', necessity=True)
  
  @rosetta_condition
  def condition_1_LegalEntityChoice(self):
    """
    Represents the choice in a CDS contract..
    """
    return self.check_one_of_constraint('primaryObligor', 'primaryObligorReference', necessity=False)

from cdm.base.staticdata.party.LegalEntity import LegalEntity
from cdm.base.staticdata.asset.common.Loan import Loan
from cdm.base.staticdata.asset.common.Security import Security

ReferenceObligation.update_forward_refs()
