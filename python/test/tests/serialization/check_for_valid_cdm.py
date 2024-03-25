'''find all valid and invalid CDM files (.json) by recursing a directory'''
import sys
import os
import glob
import json
from pathlib import Path
from pydantic import ValidationError
from cdm.event.common.TradeState import TradeState
from cdm.version import __build_time__, __version__
from dict_comp import dict_comp

def cdm_comparison_test_from_file(file_name, class_name):
    '''loads the json from a file and runs the comparison'''
    json_str  = Path(file_name).read_text()
    json_dict = json.loads (json_str)
    try:
        cdm_object = class_name.model_validate_json(json_str)
        json_data_out = cdm_object.json(exclude_defaults=True, indent=4)
        generated_dict = json.loads(json_data_out)
        if dict_comp(json_dict, generated_dict):
            return True
    except ValidationError:
        pass
    return False

if __name__ == "__main__":
    valid_files = []
    invalid_files = []
    file_loc = '.' if (len(sys.argv)<2) else sys.argv[1]
    print('checking files using cdm version: ', __version__, ' built at:',__build_time__)
    for dir_name, subdir_list, file_list in os.walk(file_loc):
        cdm_files = glob.glob(dir_name + os.sep + '*.json')
        print('in dir:', dir_name, ' found # files:', len(cdm_files))
        for cdm in cdm_files:
            if cdm_comparison_test_from_file(cdm,TradeState):
                valid_files.append (cdm)
            else:
                invalid_files.append(cdm)
    print('valid files')
    for cdm in valid_files:
        print (cdm)
    print('invalid files')
    for cdm in invalid_files:
        print (cdm)
