from cdm.base.math.FilterQuantityByFinancialUnit import FilterQuantityByFinancialUnit
from cdm.base.math.FilterQuantityByCurrencyExists import FilterQuantityByCurrencyExists
from cdm.base.math.FinancialUnitEnum import FinancialUnitEnum

def CashPriceQuantityNoOfUnitsTriangulation(quantity, price):

    notional = FilterQuantityByCurrencyExists(quantity)
    noOfUnits = FilterQuantityByFinancialUnit(quantity, FinancialUnitEnum.SHARE)

    if (len(price.amount) == 1):
        cashPrice = price.amount[0]
    else:
        cashPrice =None

    if cashPrice!=None and noOfUnits!=None and notional!=None:
        success = (cashPrice*noOfUnits==notional)

    return success
