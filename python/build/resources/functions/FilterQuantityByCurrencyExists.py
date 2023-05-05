

def FilterQuantityByCurrencyExists(quantities):
    filteredQuantities = filter(lambda x: x.unitOfAmount.currency != None, quantities)

    return filteredQuantities
