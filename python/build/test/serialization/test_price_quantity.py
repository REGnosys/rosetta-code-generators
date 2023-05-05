import pytest
from cdm.product.common.settlement.PriceQuantity import PriceQuantity
import sys,os
dirPath = os.path.dirname(__file__)
sys.path.append(os.path.join(dirPath))

from cdm_comparison_test import cdm_comparison_test_from_file

def test_price_quantity ():
	cdm_comparison_test_from_file(dirPath + '/json-samples/price_quantity.json', PriceQuantity)

if __name__ == "__main__":
	test_price_quantity()