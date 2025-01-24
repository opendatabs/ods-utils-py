from .get_uid_by_id import get_uid_by_id
from ._requests_utils import *  # imports requests_get, requests_post, etc.
from ._config import get_base_url

def get_dataset_metadata(dataset_id: str = None, dataset_uid: str = None) -> str:

    if dataset_id is not None and dataset_uid is not None:
        exit(f"Error: dataset_id ({dataset_id}) and dataset_uid ({dataset_uid}) can't both be specified.")
    if dataset_id is None and dataset_uid is None:
        exit("Error: dataset_id or dataset_uid have to be specified.")
    if dataset_id is not None:
        dataset_uid = get_uid_by_id(dataset_id)
    base_url = get_base_url()

    r = requests_get(url=f"{base_url}/datasets/{dataset_uid}")
    r.raise_for_status()

    metadata = r.json()['metadata']

    return metadata
