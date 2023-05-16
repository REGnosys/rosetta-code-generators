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

__all__ = ['Resource']


class Resource(BaseDataClass):
  """
  Describes the resource that contains the media representation of a business event (i.e used for stating the Publicly Available Information). For example, can describe a file or a URL that represents the event. This type is an extended version of a type defined by RIXML (www.rixml.org).  Rosetta restricts the FpML implementation by not providing the ability to associated a document in hexadecimalBinary or base64Binary until such time that actual use cases will come up.
  """
  comments: Optional[str] = Field(None, description="Any additional comments that are deemed necessary. For example, which software version is required to open the document? Or, how does this resource relate to the others for this event?")
  """
  Any additional comments that are deemed necessary. For example, which software version is required to open the document? Or, how does this resource relate to the others for this event?
  """
  language: Optional[AttributeWithMeta[str] | str] = Field(None, description="Indicates the language of the resource, described using the ISO 639-2/T Code.")
  """
  Indicates the language of the resource, described using the ISO 639-2/T Code.
  """
  length: Optional[ResourceLength] = Field(None, description="Indicates the length of the resource. For example, if the resource were a PDF file, the length would be in pages.")
  """
  Indicates the length of the resource. For example, if the resource were a PDF file, the length would be in pages.
  """
  mimeType: Optional[AttributeWithMeta[str] | str] = Field(None, description="Indicates the type of media used to store the content. mimeType is used to determine the software product(s) that can read the content. MIME Types are described in RFC 2046.")
  """
  Indicates the type of media used to store the content. mimeType is used to determine the software product(s) that can read the content. MIME Types are described in RFC 2046.
  """
  name: Optional[str] = Field(None, description="The name of the resource.  It is specified as a NormalizedString in FpML.")
  """
  The name of the resource.  It is specified as a NormalizedString in FpML.
  """
  resourceId: AttributeWithMeta[str] | str = Field(..., description="The unique identifier of the resource within the event. FpML specifies this element of type resourceIdScheme but with no specified value.")
  """
  The unique identifier of the resource within the event. FpML specifies this element of type resourceIdScheme but with no specified value.
  """
  resourceType: Optional[AttributeWithMeta[ResourceTypeEnum] | ResourceTypeEnum] = Field(None, description="A description of the type of the resource, e.g. a confirmation.")
  """
  A description of the type of the resource, e.g. a confirmation.
  """
  sizeInBytes: Optional[Decimal] = Field(None, description="Indicates the size of the resource in bytes. It could be used by the end user to estimate the download time and storage needs.")
  """
  Indicates the size of the resource in bytes. It could be used by the end user to estimate the download time and storage needs.
  """
  string: Optional[str] = Field(None, description="Provides extra information as string. In case the extra information is in XML format, a CDATA section must be placed around the source message to prevent its interpretation as XML content.")
  """
  Provides extra information as string. In case the extra information is in XML format, a CDATA section must be placed around the source message to prevent its interpretation as XML content.
  """
  url: Optional[str] = Field(None, description="Indicates where the resource can be found, as a URL that references the information on a web server accessible to the message recipient.")
  """
  Indicates where the resource can be found, as a URL that references the information on a web server accessible to the message recipient.
  """
  
  @rosetta_condition
  def condition_0_ResourceChoice(self):
    """
    Choice rule to represent an FpML choice construct. Note that FpML also provides the ability to have hexadecimalBinary or base64Binary, which have not been implemented in Rosetta until we see actual use cases.
    """
    return self.check_one_of_constraint('string', 'url', necessity=False)

from cdm.legaldocumentation.common.ResourceLength import ResourceLength
from cdm.legaldocumentation.common.ResourceTypeEnum import ResourceTypeEnum

Resource.update_forward_refs()
