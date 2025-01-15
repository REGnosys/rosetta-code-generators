'''Tests of the local registration of conditions'''

import datetime
from rosetta.runtime.utils import all_elements, any_elements, rosetta_count, rosetta_filter, rosetta_resolve_attr, \
    flatten_list, join, rosetta_attr_exists


def test_binary_operations():
    class T:
        def __init__(self):
            self.cleared = 'Y'
            self.counterparty1FinancialEntityIndicator = None
            self.counterparty1FinancialEntityIndicator = None
            self.actionType = "NEWT"
            self.eventType = "CLRG"
            self.originalSwapUTI = 1
            self.originalSwapUSI = 'OKI'
            self.openTradeStates = 2

    self = T()
    #equals
    res = all_elements(self.eventType,"=","CLRG")
    assert res
    res=self.eventType=="CLRG"
    assert res
    #not_equals
    res=any_elements(self.actionType,"<>","NEWT")
    assert not res
    res=self.actionType!="NEWT"
    assert not res
    #greaterthan
    res=all_elements(self.openTradeStates,">",1)
    assert res
def test_count_operation():
    class T:
        def __init__(self):
            self.tradeState=None
            self.openTradeStates = [self.tradeState , self.tradeState]
            self.closedTradeStates = 1

    self = T()
    res = rosetta_count(self.openTradeStates)
    assert res == 2

def test_sum_operation():
    class T:
        def __init__(self):
            self.tradeState=None
            self.openTradeStates = [self.tradeState , self.tradeState]
            self.closedTradeStates = 1

    self = T()
    res = sum(1 for ots in self.openTradeStates if ots is None)
    assert res==2

def test_filteroperation_currency():
    class T:
        def __init__(self):
            self.unit1 ={'currency':"USD"}
            self.quantity1={'unit':self.unit1}
            self.unit2 = {'currency': None}
            self.quantity2 = {'unit': self.unit2}
            self.quantities=[self.quantity1,self.quantity2]

    self = T()
    res = rosetta_filter(rosetta_resolve_attr(self, "quantities"), lambda item: rosetta_attr_exists(rosetta_resolve_attr(rosetta_resolve_attr(item, "unit"), "currency")))

    assert len(res)==1

def test_distinct_operation():
    class T:
        def __init__(self):
            None
            self.businessCenterEnums=["A","B","B","C"]
    self = T()
    res=set(rosetta_resolve_attr(self, "businessCenterEnums"))
    assert len(res)==3

def test_ascending_sort_operation():
    class T:
        def __init__(self):
            self.date1=datetime.date(2021, 2, 2)
            self.date2=datetime.date(2021,2,4)
            self.date3=datetime.date(2019,11,24)
            self.adjustedValuationDates=[self.date1,self.date2,self.date3]
    self = T()
    self.sortedAdjustedValuationDates = sorted(self.adjustedValuationDates)
    firstExpectedDate=datetime.date(2019,11,24)
    assert self.sortedAdjustedValuationDates[0] == firstExpectedDate

def test_descending_sort_operation():
    class T:
        def __init__(self):
            self.date1=datetime.date(2021, 2, 2)
            self.date2=datetime.date(2021,2,4)
            self.date3=datetime.date(2019,11,24)
            self.adjustedValuationDates=[self.date1,self.date2,self.date3]
    self = T()
    self.sortedAdjustedValuationDates = sorted(self.adjustedValuationDates, reverse=True)
    firstExpectedDate=datetime.date(2021,2,4)
    assert self.sortedAdjustedValuationDates[0] == firstExpectedDate

def test_last_operation():
    class T:
        def __init__(self):
            self.date1=datetime.date(2021, 2, 2)
            self.date2=datetime.date(2021,2,4)
            self.date3=datetime.date(2019,11,24)
            self.adjustedValuationDates=[self.date1,self.date2,self.date3]
    self = T()
    self.sortedAdjustedValuationDates = sorted(self.adjustedValuationDates, reverse=True)
    expectedLastDate=datetime.date(2019,11,24)
    assert self.sortedAdjustedValuationDates[-1] == expectedLastDate

def test_flatten_operation():
    class T:
        def __init__(self):
            self.date1=datetime.date(2021, 2, 2)
            self.date2=datetime.date(2021,2,4)
            self.date3=datetime.date(2019,11,24)
            self.date4=datetime.date(2024,4,15)
            self.adjustedValuationDates1=[self.date1,self.date2]
            self.adjustedValuationDates2= [self.date3, self.date4]
            self.adjustedValuationDates=[self.adjustedValuationDates1,self.adjustedValuationDates2]
    self = T()
    res = flatten_list(self.adjustedValuationDates)
    assert len(res)==4

def test_reverse_operation():
    class T:
        def __init__(self):
            self.businessCenters=['AEAB','BBBR','INKO']
    self = T()
    res = list(reversed(self.businessCenters))
    assert res[0]=='INKO'

def test_join_operation():
    class T:
        def __init__(self):
            self.businessCenters=['AEAB','BBBR','INKO']

    self=T()
    res=join(self.businessCenters,'CAVA')
    assert 'CAVA' in res



if __name__ == '__main__':
    test_binary_operations()
    test_join_operation()
    test_last_operation()
    test_sum_operation()
    test_ascending_sort_operation()
    test_descending_sort_operation()
    test_count_operation()
    test_distinct_operation()
    test_flatten_operation()
    test_reverse_operation()
    test_filteroperation_currency()
    print('...passed')
# EOF
