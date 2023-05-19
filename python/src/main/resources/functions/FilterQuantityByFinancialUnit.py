
def FilterQuantityByFinancialUnit(quantities, financialUnit):
    filteredQuantities = filter(lambda x: x.unitOfAmount.financialUnit == financialUnit, quantities)

    return filteredQuantities