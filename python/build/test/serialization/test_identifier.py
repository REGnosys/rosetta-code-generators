import pytest
from cdm.base.staticdata.identifier.Identifier import Identifier
import sys,os
dirPath = os.path.dirname(__file__)
sys.path.append(os.path.join(dirPath))
from cdm_comparison_test import cdm_comparison_test_from_file

def test_identifier ():
	cdm_comparison_test_from_file(dirPath + '/json-samples/expected_Identifier.json', Identifier)

if __name__ == "__main__":
	test_identifier()