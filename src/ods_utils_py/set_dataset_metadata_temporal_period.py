from .set_dataset_public import set_dataset_public
from .get_uid_by_id import get_uid_by_id
from ._requests_utils import *  # imports requests_get, requests_post, etc.
from ._config import get_base_url
import time

def set_dataset_metadata_temporal_period(temporal_period: str | None,
                                         dataset_id: str = None, dataset_uid: str = None,
                                         publish: bool = True,
                                         should_override_remote_value: bool = True) -> None:
    """
    Set the temporal period for a dataset. Either `dataset_id` or `dataset_uid` can be used to specify the
    dataset.

    Args:
        temporal_period (str): The temporal period that should be set. Set it to None to delete it.
        dataset_id (str, optional): The unique integer identifier of the dataset.
        dataset_uid (str, optional): The unique string identifier (UID) of the dataset.
        publish (bool, optional): When set to true, the dataset is also published. This should only be disabled when
            making several changes. In this case, the dataset should be published when all changes are applied.
        should_override_remote_value (bool, optional): When turned off, fields that are locked will show the remote
            value that might be uploaded by the harvester. When turned on, the remote fields are kept, but the value
            that this script uploaded will be displayed.
    """
    if dataset_id is not None and dataset_uid is not None:
        exit(f"Error: dataset_id ({dataset_id}) and dataset_uid ({dataset_uid}) can't both be specified.")
    if dataset_id is None and dataset_uid is None:
        exit("Error: dataset_id or dataset_uid have to be specified.")
    if dataset_id is not None:
        dataset_uid = get_uid_by_id(dataset_id)
    base_url = get_base_url()

    r = requests_get(url=f"{base_url}/datasets/{dataset_uid}/metadata/")
    r.raise_for_status()

    updated_json = r.json()

    if temporal_period is None:
        updated_json['dcat'].pop('temporal', None)
    else:
        if 'dcat' not in updated_json:
            updated_json['dcat'] = {}

        if 'temporal' not in updated_json['dcat']:
            updated_json['dcat']['temporal'] = {}

        updated_json['dcat']['temporal']['override_remote_value'] = should_override_remote_value
        remote_value = updated_json['dcat']['temporal'].get('remote_value', None)
        updated_json['dcat']['temporal']['remote_value'] = remote_value
        updated_json['dcat']['temporal']['value'] = temporal_period


    # Wait for dataset to be idle before updating metadata
    while requests_get(url=f"{base_url}/datasets/{dataset_uid}/status").json()['status'] != "idle":
        time.sleep(3)

    r = requests_put(url=f"{base_url}/datasets/{dataset_uid}/metadata/", json=updated_json)
    r.raise_for_status()

    if publish:
        set_dataset_public(dataset_uid=dataset_uid)
