from cdm.observable.asset.PriceTypeEnum import PriceTypeEnum
from cdm.observable.common.CashPriceQuantityNoOfUnitsTriangulation import CashPriceQuantityNoOfUnitsTriangulation

def mapping(element):
    if (PriceTypeEnum.CASH_PRICE in element.priceQuantity.price.priceExpression.priceType):
        return CashPriceQuantityNoOfUnitsTriangulation(element.priceQuantity.quantity, element.priceQuantity.price)
    else:
        return True



def PriceQuantityTriangulation(tradeLots):
    if(len(tradeLots)>0):
        tradeLots = map(lambda x: mapping(x), tradeLots)
        success = True

        for elem in tradeLots:
            if(elem!=True):
                success=False
    else:
        success = True
    return success