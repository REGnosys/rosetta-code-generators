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

__all__ = ['CreditDefaultPayout']

from cdm.product.common.settlement.PayoutBase import PayoutBase

class CreditDefaultPayout(PayoutBase):
  """
   The credit default payout specification provides the details necessary for determining when a credit payout will be triggered as well as the parameters for calculating the payout and the settlement terms. The associated globalKey denotes the ability to associate a hash value to the CreditDefaultPayout instantiations for the purpose of model cross-referencing, in support of functionality such as the event effect and the lineage.
  """
  generalTerms: GeneralTerms = Field(..., description="The specification of the non-monetary terms for the Credit Derivative Transaction, including the buyer and seller and selected items from the ISDA 2014 Credit Definition article II, such as the reference obligation and related terms.")
  """
  The specification of the non-monetary terms for the Credit Derivative Transaction, including the buyer and seller and selected items from the ISDA 2014 Credit Definition article II, such as the reference obligation and related terms.
  """
  protectionTerms: List[ProtectionTerms] = Field([], description="Specifies the terms for calculating a payout to protect the buyer of the swap in the case of a qualified credit event. These terms include the applicable credit events, the reference obligation, and in the case of a CDS on mortgage-backed securities, the floatingAmountEvents.")
  """
  Specifies the terms for calculating a payout to protect the buyer of the swap in the case of a qualified credit event. These terms include the applicable credit events, the reference obligation, and in the case of a CDS on mortgage-backed securities, the floatingAmountEvents.
  """
  transactedPrice: Optional[TransactedPrice] = Field(None, description="The qualification of the price at which the contract has been transacted, in terms of market fixed rate, initial points, market price and/or quotation style. In FpML, those attributes are positioned as part of the fee leg.")
  """
  The qualification of the price at which the contract has been transacted, in terms of market fixed rate, initial points, market price and/or quotation style. In FpML, those attributes are positioned as part of the fee leg.
  """
  
  @rosetta_condition
  def condition_0_FpML_cd_12(self):
    """
    FpML validation rule cd-12 - If referencePrice exists, referencePrice must be greater or equal to 0
    """
    def _then_fn0():
      return all_elements(self.generalTerms.referenceInformation.referencePrice.value, ">=", 0)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.generalTerms.referenceInformation.referencePrice) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_Quantity(self):
    """
    When there is an OptionPayout the quantity can be expressed as part of the payoutQuantity, or as part of the underlier in the case of a Swaption.  For all other payouts that extend PayoutBase the payoutQuantity is a mandatory attribute.
    """
    return ((self.priceQuantity) is not None)

from cdm.product.asset.GeneralTerms import GeneralTerms
from cdm.product.asset.ProtectionTerms import ProtectionTerms
from cdm.observable.asset.TransactedPrice import TransactedPrice

CreditDefaultPayout.update_forward_refs()
