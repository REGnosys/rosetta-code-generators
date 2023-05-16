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

__all__ = ['MarginCallBase']


class MarginCallBase(BaseDataClass):
  """
  Represents common attributes required for Issuance and Response to a Margin Call action as a result of a demand for delivery or return of collateral determined under a legal agreement such as a credit support document or equivalent.
  """
  agreementMinimumTransferAmount: Optional[Money] = Field(None, description="Specifies the collateral legal agreement minimum transfer amount in base currency.")
  """
  Specifies the collateral legal agreement minimum transfer amount in base currency.
  """
  agreementRounding: Optional[Money] = Field(None, description="Specifies the collateral legal agreement rounding in base currency.")
  """
  Specifies the collateral legal agreement rounding in base currency.
  """
  agreementThreshold: Optional[Money] = Field(None, description="Specifies the collateral legal agreement threshold amount in base currency.")
  """
  Specifies the collateral legal agreement threshold amount in base currency.
  """
  baseCurrencyExposure: Optional[MarginCallExposure] = Field(None, description="Represents the current mark to market value or IM calculation value of the trade portfolio as recorded by the principle (in base currency), to be referenced in a margin call.")
  """
  Represents the current mark to market value or IM calculation value of the trade portfolio as recorded by the principle (in base currency), to be referenced in a margin call.
  """
  callAgreementType: AgreementName = Field(..., description="Specifies the legal agreement type the margin call is generated from and governed by.")
  """
  Specifies the legal agreement type the margin call is generated from and governed by.
  """
  callIdentifier: Optional[Identifier] = Field(None, description="Represents a unique Identifier for a margin call message, that can be referenced throughout all points of the process.")
  """
  Represents a unique Identifier for a margin call message, that can be referenced throughout all points of the process.
  """
  clearingBroker: Optional[Party] = Field(None, description="Indicates the name of the Clearing Broker FCM/DCM.")
  """
  Indicates the name of the Clearing Broker FCM/DCM.
  """
  collateralPortfolio: Optional[AttributeWithReference | CollateralPortfolio] = Field(None, description="Represents attributes to define the details of collateral assets within a collateral portfolio to be used in margin call messaging and contribute to collateral balances e.g securities in a collateral account recorded by the principal as held or posted.")
  """
  Represents attributes to define the details of collateral assets within a collateral portfolio to be used in margin call messaging and contribute to collateral balances e.g securities in a collateral account recorded by the principal as held or posted.
  """
  independentAmountBalance: Optional[CollateralBalance] = Field(None, description="Represents additional credit support amount over and above mark to market value.")
  """
  Represents additional credit support amount over and above mark to market value.
  """
  instructionType: MarginCallInstructionType = Field(..., description="Identifies the enumeration values to specify the call notification type, direction, specific action type.")
  """
  Identifies the enumeration values to specify the call notification type, direction, specific action type.
  """
  party: List[Party] = Field([], description="Represents the parties to the margin call. The cardinality is optional to address the case where both parties of the event are specified and a third party if applicable.")
  """
  Represents the parties to the margin call. The cardinality is optional to address the case where both parties of the event are specified and a third party if applicable.
  """
  partyRole: List[PartyRole] = Field([], description="Represents the role each specified party takes in the margin call. further to the principal roles, payer and receiver.")
  """
  Represents the role each specified party takes in the margin call. further to the principal roles, payer and receiver.
  """
  regIMRole: Optional[RegIMRoleEnum] = Field(None, description="Indicates the role of the party in an regulatory initial margin call instruction (i.e Pledgor party or Secured party).")
  """
  Indicates the role of the party in an regulatory initial margin call instruction (i.e Pledgor party or Secured party).
  """
  regMarginType: RegMarginTypeEnum = Field(..., description="Identifies margin type and if related regulatory mandate")
  """
  Identifies margin type and if related regulatory mandate
  """
  
  @rosetta_condition
  def condition_0_RegIMRoleIMOnly(self):
    """
    Specifies a condition to ensure that RegIMRole (Pledgor or Secured Party)is only applicable if the Reg margin type is defined as RegIM (Regulatory Initial Margin).
    """
    def _then_fn0():
      return all_elements(self.regMarginType, "=", RegMarginTypeEnum.REG_IM)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.regIMRole) is not None), _then_fn0, _else_fn0)

from cdm.observable.asset.Money import Money
from cdm.event.common.MarginCallExposure import MarginCallExposure
from cdm.legaldocumentation.common.AgreementName import AgreementName
from cdm.base.staticdata.identifier.Identifier import Identifier
from cdm.base.staticdata.party.Party import Party
from cdm.event.common.CollateralPortfolio import CollateralPortfolio
from cdm.event.common.CollateralBalance import CollateralBalance
from cdm.event.common.MarginCallInstructionType import MarginCallInstructionType
from cdm.base.staticdata.party.PartyRole import PartyRole
from cdm.event.common.RegIMRoleEnum import RegIMRoleEnum
from cdm.event.common.RegMarginTypeEnum import RegMarginTypeEnum

MarginCallBase.update_forward_refs()
