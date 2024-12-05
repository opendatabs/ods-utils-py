from ._requests_utils import *  # imports requests_get, requests_post, etc.
from ._config import get_base_url

def get_all_dataset_ids(include_restricted: bool = True) -> [str]:
    """
    Retrieve all dataset ids

    Args:
        include_restricted: Determines whether datasets with restricted access should be included. Set this to False for
            retrieving only the datasets that are accessible by the public.

    Returns: A list of the ids of all datasets
    """
    base_url = get_base_url()
    r = requests_get(url=f"{base_url}/datasets/?limit=50")
    r.raise_for_status()

    all_ids = []

    while True:
        if include_restricted:
            all_ids += [item['dataset_id'] for item in r.json().get('results', {})]
        else:
            all_ids += [item['dataset_id'] for item in r.json().get('results', {}) if not item['is_restricted']]

        next_request_url = r.json().get('next', None)

        if not next_request_url:
            break

        r = requests_get(url=next_request_url)
        r.raise_for_status()

    all_ids.sort()

    return all_ids
