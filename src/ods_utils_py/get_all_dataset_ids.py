from ._requests_utils import *  # imports requests_get, requests_post, etc.
from ._config import get_base_url
import time

def get_all_dataset_ids(include_restricted: bool = True, max_datasets: int = None, cooldown: float = 1.0) -> [str]:
    """
    Retrieve all dataset ids

    Args:
        include_restricted: Determines whether datasets with restricted access should be included. Set this to False for
            retrieving only the datasets that are accessible by the public.
        max_datasets: Maximum number of dataset IDs to return. If None, all datasets are returned.
        cooldown: Sleep time in seconds between requests to avoid overloading the server. Defaults to 1.0.

    Returns: A sorted list of the ids of all datasets
    """
    base_url = get_base_url()
    batch_size = 100
    r = requests_get(url=f"{base_url}/datasets/?limit={batch_size}")
    r.raise_for_status()

    all_ids = []

    while True:
        if include_restricted:
            all_ids += [item['dataset_id'] for item in r.json().get('results', {})]
        else:
            all_ids += [item['dataset_id'] for item in r.json().get('results', {}) if not item['is_restricted']]
            
        # Check if we have reached the maximum number of datasets
        if max_datasets is not None and len(all_ids) >= max_datasets:
            all_ids = all_ids[:max_datasets]
            break

        next_request_url = r.json().get('next', None)

        if not next_request_url:
            break

        # Add cooldown between requests
        time.sleep(cooldown)
        
        r = requests_get(url=next_request_url)
        r.raise_for_status()

    all_ids.sort()

    return all_ids
