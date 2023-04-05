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
from cdm.base.datetime.PeriodExtendedEnum import PeriodExtendedEnum

__all__ = ['Frequency']


class Frequency(BaseDataClass):
    """ A class for defining a date frequency, e.g. one day, three months,
        through the combination of an integer value and a standardized period
        value that is specified as part of an enumeration.
    """

    periodMultiplier: int = Field(
        ...,
        description='A time period multiplier, e.g. 1, 2, or 3. If the period '
                    'value is T (Term) then period multiplier must contain the '
                    'value 1.'
    )
    """ A time period multiplier, e.g. 1, 2, or 3. If the period value is T
       (Term) then period multiplier must contain the value 1.
    """
    period: PeriodExtendedEnum = Field(
        ...,
        description='A time period, e.g. a day, week, month, year or term of '
                    'the stream.'
    )
    """ A time period, e.g. a day, week, month, year or term of  the stream.
    """

# EOF
