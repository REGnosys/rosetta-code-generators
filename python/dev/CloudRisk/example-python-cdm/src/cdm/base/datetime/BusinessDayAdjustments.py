""" Basic date and time concepts: relative date, date range, offset, business
    centre etc.
"""
# An example of a file to be generated from a rosetta source. In this
# particluar case4, the example reflects the frequency data type from
# base-datetime-type.rosetta
from __future__ import annotations
from typing import List, Optional
from datetime import date
from pydantic import Field
from cdm.utils import *
from cdm.base.datetime.BusinessDayConventionEnum import BusinessDayConventionEnum

__all__ = ['BusinessDayAdjustments']


class BusinessDayAdjustments(BaseDataClass):
    """ A class defining the business day convention and financial business
        centers used for adjusting any relevant date if it would otherwise fall
        on a day that is not a business day in the specified business center.
    """

    businessDayConvention: BusinessDayConventionEnum = Field(
        ...,
        description='The convention for adjusting a date if it would otherwise '
                    'fall on a day that is not a business day.'
    )
    """ (1..1) The convention for adjusting a date if it would otherwise fall
        on a day that is not a business day.
    """
    businessCenters: Optional[BusinessCenters] = Field(
        None,
        description='The business center(s), specified either explicitly or by '
                    'reference to those specified somewhere else in the '
                    'instance document.'
    )
    """ (0..1) The business center(s), specified either explicitly or by
        reference to those specified somewhere else in the instance document.
    """


from cdm.base.datetime.BusinessCenters import BusinessCenters

BusinessDayAdjustments.update_forward_refs()

# EOF
