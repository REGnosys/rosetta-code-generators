from cdm.base.staticdata.asset.common.SecurityTypeEnum import SecurityTypeEnum
from cdm.base.staticdata.asset.common.FundProductTypeEnum import FundProductTypeEnum

def Qualify_AssetClass_Equity(underlier):

    is_product = False
    if (underlier.security.securityType == SecurityTypeEnum.EQUITY) or \
            (underlier.security.securityType == SecurityTypeEnum.FUND and underlier.security.fundType == FundProductTypeEnum.EXCHANGE_TRADED_FUND) \
            or (underlier.security.securityType == SecurityTypeEnum.FUND and underlier.security.fundType == FundProductTypeEnum.MUTUAL_FUND) \
            or (underlier.security.securityType == SecurityTypeEnum.WARRANT) \
            or (underlier.index != None) \
            or (underlier.basket != None and SecurityTypeEnum.EQUITY in underlier.basket.basketConstituent.security.securityType)\
            or (SecurityTypeEnum.FUND in underlier.basket.basketConstituent.security.securityType and FundProductTypeEnum.EXCHANGE_TRADED_FUND in underlier.basket.basketConstituent.security.fundType )\
            or (SecurityTypeEnum.FUND in underlier.basket.basketConstituent.security.securityType and FundProductTypeEnum.MUTUAL_FUND in underlier.basket.basketConstituent.security.fundType)\
            or (SecurityTypeEnum.WARRANT in underlier.basket.basketConstituent.security.securityType)\
            or (underlier.basket.basketConstituent.index != None):
        is_product = True

    return is_product