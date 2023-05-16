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

__all__ = ['Tranche']


class Tranche(BaseDataClass):
  """
  The class to represent a CDS Tranche.
  """
  attachmentPoint: Decimal = Field(..., description="Lower bound percentage of the loss that the Tranche can endure, expressed as a decimal. An attachment point of 5% would be represented as 0.05. The difference between Attachment and Exhaustion points is called the width of the Tranche.")
  """
  Lower bound percentage of the loss that the Tranche can endure, expressed as a decimal. An attachment point of 5% would be represented as 0.05. The difference between Attachment and Exhaustion points is called the width of the Tranche.
  """
  exhaustionPoint: Decimal = Field(..., description="Upper bound percentage of the loss that the Tranche can endure, expressed as a decimal. An exhaustion point of 5% would be represented as 0.05. The difference between Attachment and Exhaustion points is call the width of the Tranche.")
  """
  Upper bound percentage of the loss that the Tranche can endure, expressed as a decimal. An exhaustion point of 5% would be represented as 0.05. The difference between Attachment and Exhaustion points is call the width of the Tranche.
  """
  incurredRecoveryApplicable: Optional[bool] = Field(None, description="Outstanding Swap Notional Amount is defined at any time on any day, as the greater of: (a) Zero; If Incurred Recovery Amount Applicable: (b) The Original Swap Notional Amount minus the sum of all Incurred Loss Amounts and all Incurred Recovery Amounts (if any) determined under this Confirmation at or prior to such time.Incurred Recovery Amount not populated: (b) The Original Swap Notional Amount minus the sum of all Incurred Loss Amounts determined under this Confirmation at or prior to such time.")
  """
  Outstanding Swap Notional Amount is defined at any time on any day, as the greater of: (a) Zero; If Incurred Recovery Amount Applicable: (b) The Original Swap Notional Amount minus the sum of all Incurred Loss Amounts and all Incurred Recovery Amounts (if any) determined under this Confirmation at or prior to such time.Incurred Recovery Amount not populated: (b) The Original Swap Notional Amount minus the sum of all Incurred Loss Amounts determined under this Confirmation at or prior to such time.
  """
  
  @rosetta_condition
  def condition_0_AttachmentPoint(self):
    """
    FpML definition associated with the attachmentPoint element specifies that a schema facet to constraint the value between 0 to 1 will be introduced in FpML 4.3.
    """
    return (all_elements(self.attachmentPoint, ">=", 0.0) and all_elements(self.attachmentPoint, "<=", 1.0))
  
  @rosetta_condition
  def condition_1_ExhaustionPoint(self):
    """
    FpML definition associated with the exhaustionPoint element specifies that a schema facet to constraint the value between 0 to 1 will be introduced in FpML 4.3.
    """
    return (all_elements(self.exhaustionPoint, ">=", 0.0) and all_elements(self.exhaustionPoint, "<=", 1.0))
  
  @rosetta_condition
  def condition_2_AttachmentPointLessThanExhaustionPoint(self):
    """
    FpML validation rule cd-40 - Context: Tranche (complex type) attachmentPoint must be less or equal to exhaustionPoint.
    """
    return all_elements(self.attachmentPoint, "<=", self.exhaustionPoint)


Tranche.update_forward_refs()
