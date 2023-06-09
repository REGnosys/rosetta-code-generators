import pytest
from cdm.base.staticdata.party.Party import Party
import sys,os
dirPath = os.path.dirname(__file__)
sys.path.append(os.path.join(dirPath))
from cdm_comparison_test import cdm_comparison_test_from_file

def test_party (version="4_0_0"):
	cdm_comparison_test_from_file(dirPath + '/cdm_samples/' + version + '/original_Party.json', Party)

if __name__ == "__main__":
	version = sys.argv[1] if len(sys.argv) > 1 else '3_3_2'
	test_party(version)