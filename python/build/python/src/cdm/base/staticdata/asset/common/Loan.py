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

__all__ = ['Loan']

from cdm.base.staticdata.asset.common.ProductBase import ProductBase

class Loan(ProductBase):
  """
  Identifies a loan by referencing a product identifier and through an optional set of attributes.
  """
  borrower: List[LegalEntity] = Field([], description="Specifies the borrower. There can be more than one borrower. It is meant to be used in the event that there is no Bloomberg Id or the Secured List isn't applicable.")
  """
  Specifies the borrower. There can be more than one borrower. It is meant to be used in the event that there is no Bloomberg Id or the Secured List isn't applicable.
  """
  creditAgreementDate: Optional[date] = Field(None, description="Specifies the credit agreement date is the closing date (the date where the agreement has been signed) for the loans in the credit agreement. Funding of the facilities occurs on (or sometimes a little after) the Credit Agreement date. This underlier attribute is used to help identify which of the company's outstanding loans are being referenced by knowing to which credit agreement it belongs. ISDA Standards Terms Supplement term: Date of Original Credit Agreement.")
  """
  Specifies the credit agreement date is the closing date (the date where the agreement has been signed) for the loans in the credit agreement. Funding of the facilities occurs on (or sometimes a little after) the Credit Agreement date. This underlier attribute is used to help identify which of the company's outstanding loans are being referenced by knowing to which credit agreement it belongs. ISDA Standards Terms Supplement term: Date of Original Credit Agreement.
  """
  facilityType: Optional[AttributeWithMeta[str] | str] = Field(None, description="Specifies the type of loan facility (letter of credit, revolving, ...).")
  """
  Specifies the type of loan facility (letter of credit, revolving, ...).
  """
  lien: Optional[AttributeWithMeta[str] | str] = Field(None, description="Specifies the seniority level of the lien.")
  """
  Specifies the seniority level of the lien.
  """
  tranche: Optional[AttributeWithMeta[str] | str] = Field(None, description="Denotes the loan tranche that is subject to the derivative transaction. It will typically be referenced as the Bloomberg tranche number. ISDA Standards Terms Supplement term: Bloomberg Tranche Number.")
  """
  Denotes the loan tranche that is subject to the derivative transaction. It will typically be referenced as the Bloomberg tranche number. ISDA Standards Terms Supplement term: Bloomberg Tranche Number.
  """

from cdm.base.staticdata.party.LegalEntity import LegalEntity

Loan.update_forward_refs()
