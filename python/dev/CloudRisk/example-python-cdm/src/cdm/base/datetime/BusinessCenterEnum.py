""" Basic date and time concepts: relative date, date range, offset, business
    centre etc.
"""
# An example of a file to be generated from a rosetta source. In this
# particluar case, the example reflects the first enum from
# base-math-enum.rosetta
from enum import Enum

__all__ = ['BusinessCenterEnum']


class BusinessCenterEnum(str, Enum):
    """The enumerated values to specify the business centers."""
    # [docReference ISDA FpML_Coding_Scheme schemeLocation
    # "http://www.fpml.org/coding-scheme/business-center-8-2"]

    AEAD = 'AEAD'
    """Abu Dhabi, United Arab Emirates"""
    AEDU = 'AEDU'
    """Dubai, United Arab Emirates"""
    AMYE = 'AMYE'
    """Yerevan, Armenia"""
    AOLU = 'AOLU'
    """Luanda, Angola"""
    ARBA = 'ARBA'
    """Buenos Aires, Argentina"""

# EOF
