

def FilterOpenTradeStates(tradeStates):
    openTradeStates = filter(lambda x: x.state.closedState == None, tradeStates)

    return openTradeStates