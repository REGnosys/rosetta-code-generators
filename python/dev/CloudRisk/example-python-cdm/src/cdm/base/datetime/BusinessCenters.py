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
from cdm.base.datetime.BusinessCenterEnum import BusinessCenterEnum

__all__ = ['BusinessCenters']


class BusinessCenters(BaseDataClass):
    """ A class for specifying the business day calendar location used in
        determining whether a day is a business day or not, either by specifying
        this business center by reference to an enumerated list that is
        maintained by the FpML standard, or by reference to such specification
        when it exists elsewhere as part of the instance document. This class
        corresponds to the FpML BusinessCentersOrReference.model.
    """

    businessCenter: Optional[List[BusinessCenterEnum]] = Field(
        None,
        description='A code identifying one or several business day calendar '
                    'location(s). The set of business day calendar locations '
                    'are specified by the business day calendar location '
                    'enumeration which is maintained by the FpML standard.'
    )
    """ (0..*) A code identifying one or several business day calendar
        location(s). The set of business day calendar locations are specified by
        the business day calendar location enumeration which is maintained by
        the FpML standard.
    """
    businessCentersReference: Optional[BusinessCenters] = Field(
        None,
        description='A reference to a financial business center location '
                    'specified elsewhere in the instance document.'
    )
    """ (0..1) A reference to a financial business center location specified
        elsewhere in the instance document.
    """

    @cdm_condition
    def condition_0_BusinessCentersChoice(self):
        """ Choice rule to represent an FpML choice construct. """
        return self.check_one_of_constraint(
            'businessCenter', 'businessCentersReference'
        )

# EOF
