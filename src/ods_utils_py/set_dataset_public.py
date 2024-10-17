from .get_uid_by_id import get_uid_by_id
from ._requests_utils import *  # imports requests_get, requests_post, etc.
from ._config import get_base_url

def set_dataset_public(dataset_id: int = None, dataset_uid: str = None, should_be_public: bool = True) -> None:
    """
    Used to publish or unpublish a dataset.

    Either `dataset_id` or `dataset_uid` can be used to specify the dataset.

    Args:
        should_be_public (bool, optional): Set True to publish the dataset, set False to unpublish the dataset
        dataset_id (int, optional): The unique integer identifier of the dataset.
        dataset_uid (str, optional): The unique string identifier (UID) of the dataset.
    """
    if dataset_id is not None and dataset_uid is not None:
        exit(f"Error: dataset_id ({dataset_id}) and dataset_uid ({dataset_uid}) can't both be specified.")
    if dataset_id is None and dataset_uid is None:
        exit("Error: dataset_id or dataset_uid have to be specified.")
    if dataset_id is not None:
        dataset_uid = get_uid_by_id(dataset_id)
    base_url = get_base_url()

    if should_be_public:
        r = requests_post(url=f"{base_url}/datasets/{dataset_uid}/publish/")
    else:
        r = requests_post(url=f"{base_url}/datasets/{dataset_uid}/unpublish/")

    r.raise_for_status()