from enum import Enum

all = ['ExpirationTimeTypeEnum']
	  
class ExpirationTimeTypeEnum(Enum):
    """
    The time of day at which the equity option expires, for example the official closing time of the exchange.
    """
    AS_SPECIFIED_IN_MASTER_CONFIRMATION = "AS_SPECIFIED_IN_MASTER_CONFIRMATION"
    """
    The time is determined as provided in the relevant Master Confirmation.
    """
    CLOSE = "CLOSE"
    """
    The official closing time of the exchange on the valuation date.
    """
    DERIVATIVES_CLOSE = "DERIVATIVES_CLOSE"
    """
    The official closing time of the derivatives exchange on which a derivative contract is listed on that security underlyer.
    """
    OSP = "OSP"
    """
    The time at which the official settlement price is determined.
    """
    OPEN = "OPEN"
    """
    The official opening time of the exchange on the valuation date.
    """
    SPECIFIC_TIME = "SPECIFIC_TIME"
    """
    The time specified in the element equityExpirationTime or valuationTime (as appropriate)
    """
    XETRA = "XETRA"
    """
    The time at which the official settlement price (following the auction by the exchange) is determined by the exchange.
    """
