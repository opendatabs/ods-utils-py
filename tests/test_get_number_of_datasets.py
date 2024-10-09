import os
os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Changing the directory before the ods_utils import is crucial!
#  Without that, ods_utils looks for an .env file in the 'tests' folder.
#  With it, ods_utils looks for an .env file in the parent folder of 'tests',
#  where .env should be located when developing code.


import src.ods_utils_py as ods_utils

def test_get_number_of_datasets_returns_int():
    result = ods_utils.get_number_of_datasets()
    assert type(result) == int
