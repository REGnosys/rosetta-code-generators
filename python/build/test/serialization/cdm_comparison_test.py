import json
from pathlib import Path
import sys,os
dirPath = os.path.dirname(__file__)
sys.path.append(os.path.join(dirPath))

from dict_comp import dict_comp
from cdm.version import __build_time__

def cdm_comparison_test_from_file(path, className):
    print('testing: ' + path + ' with className: ' + className.__name__ + ' using CDM built at: ' + __build_time__)
    jsonStr = Path(path).read_text()
    cdm_comparison_test_from_string(jsonStr, className)

def cdm_comparison_test_from_string(jsonStr, className):
    cdmObject     = className.parse_raw(jsonStr)
    jsonDataOut   = cdmObject.json(exclude_none=True, indent=4)
    origDict      = json.loads(jsonStr)
    generatedDict = json.loads(jsonDataOut)    
    assert dict_comp(origDict, generatedDict), f"Failed corrected dict comparison"
    print('passed: dicts matched')