from ._requests_utils import *
from ._config import get_base_url

__all__ = ["get_number_of_datasets"]

def get_number_of_datasets():
    r = requests_get(url=f"{get_base_url()}/datasets/")
    return r.json()['total_count']
