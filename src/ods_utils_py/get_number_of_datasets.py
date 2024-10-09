from ._requests_utils import *  # imports requests_get, requests_post, etc.
from ._config import get_base_url

def get_number_of_datasets() -> int:
    """
    Get the number of all datasets on the account. This includes all datasets, including unpublished and private ones.

    Returns: Number of all datasets
    """
    base_url = get_base_url()
    r = requests_get(url=f"{base_url}/datasets/")
    return r.json()['total_count']
