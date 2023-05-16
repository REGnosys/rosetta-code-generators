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

__all__ = ['MessageInformation']


class MessageInformation(BaseDataClass):
  """
  This class corresponds to the components of the FpML MessageHeader.model.
  """
  copyTo: List[AttributeWithMeta[str] | str] = Field([], description="A unique identifier (within the specified coding scheme) giving the details of some party to whom a copy of this message will be sent for reference.")
  """
  A unique identifier (within the specified coding scheme) giving the details of some party to whom a copy of this message will be sent for reference.
  """
  messageId: AttributeWithMeta[str] | str = Field(..., description="A unique identifier assigned to the message.")
  """
  A unique identifier assigned to the message.
  """
  sentBy: Optional[AttributeWithMeta[str] | str] = Field(None, description="The identifier for the originator of a message instance.")
  """
  The identifier for the originator of a message instance.
  """
  sentTo: List[AttributeWithMeta[str] | str] = Field([], description="The identifier(s) for the recipient(s) of a message instance.")
  """
  The identifier(s) for the recipient(s) of a message instance.
  """


MessageInformation.update_forward_refs()
