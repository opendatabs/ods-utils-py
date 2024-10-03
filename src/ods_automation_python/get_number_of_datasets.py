from ._requests_utils import *

__all__ = ["get_number_of_datasets"]

def get_number_of_datasets():
    print("Trying to receive count of all datasets")
    r = requests_get(url=f"{get_base_url()}/datasets/")
    print(r.json()['total_count'])
    pass
