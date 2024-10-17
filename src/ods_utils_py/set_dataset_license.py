from .set_dataset_public import set_dataset_public
from .get_uid_by_id import get_uid_by_id
from ._requests_utils import *  # imports requests_get, requests_post, etc.
from ._config import get_base_url
from .get_dataset_license import _currently_valid_ids
import time

def set_dataset_license(license_id: str, dataset_id: int = None, dataset_uid: str = None, publish: bool = True) -> None:
    """
    Set the license identifier for a dataset. Either `dataset_id` or `dataset_uid` can be used to specify the
    dataset.

    Args:
        license_id (str): The license_id the dataset should be set to. Please refer to the documentation of
            get_dataset_license for the exact string required.
        dataset_id (int, optional): The unique integer identifier of the dataset.
        dataset_uid (str, optional): The unique string identifier (UID) of the dataset.
        publish (bool, optional): When set to true, the dataset is also published. This should only be disabled when making
            several changes. In this case, the dataset should be published when all changes are applied.
    """
    if dataset_id is not None and dataset_uid is not None:
        exit(f"Error: dataset_id ({dataset_id}) and dataset_uid ({dataset_uid}) can't both be specified.")
    if dataset_id is None and dataset_uid is None:
        exit("Error: dataset_id or dataset_uid have to be specified.")
    if dataset_id is not None:
        dataset_uid = get_uid_by_id(dataset_id)
    base_url = get_base_url()

    if license_id not in _currently_valid_ids:
        raise ValueError(f"Tried setting license id to {license_id}, which is not valid. Currently valid ids are: "
                         f"{_currently_valid_ids}")

    # TODO: This is a bit risky, as we download all metadata, change one field, and then upload the entire metadata json
    #  again. We could accidentally delete all metadata when we're not careful (e.g. when we have not received any
    #  metadata, but did not get an error). It would be a lot safer to update one field remotely. This has the potential
    #  to delete all metadata of a dataset! I just didn't manage to get it to work that way.
    r = requests_get(url=f"{base_url}/datasets/{dataset_uid}/metadata/")
    r.raise_for_status()

    updated_json = r.json()
    updated_json['internal']['license_id']['value'] = license_id

    # Wait for dataset to be idle before updating metadata
    while requests_get(url=f"{base_url}/datasets/{dataset_uid}/status").json()['status'] != "idle":
        time.sleep(3)

    r = requests_put(url=f"{base_url}/datasets/{dataset_uid}/metadata/", json=updated_json)
    r.raise_for_status()

    if publish:
        set_dataset_public(dataset_uid=dataset_uid)
