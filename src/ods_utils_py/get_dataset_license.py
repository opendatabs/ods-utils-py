from .get_uid_by_id import get_uid_by_id
from ._requests_utils import *  # imports requests_get, requests_post, etc.
from ._config import get_base_url

# I found these manually, by changing it in ods, and retrieving through the API. Please adapt if an error occurs!
_currently_valid_ids = ['cc_by', 't2kf10u', '5sylls5', '4bj8ceb', 'hmpvfpp', 'ce0mv1b', 'vzo5u7j', 'r617wgj']

def get_dataset_license(dataset_id: int = None, dataset_uid: str = None,
                        no_license_default_value: str = "NO LICENSE") -> str:
    """
    Retrieve the license identifier for a dataset. Either `dataset_id` or `dataset_uid` can be used to specify the
    dataset.

    Args:
        dataset_id (int, optional): The unique integer identifier of the dataset.
        dataset_uid (str, optional): The unique string identifier (UID) of the dataset.
        no_license_default_value (str, optional): The default value to return if no license is found.

    Returns:
        str: The license identifier for the dataset. This could be:
            - The value of `no_license_default_value` if no license is set.
            - 'cc_by'   for 'CC BY 3.0 CH'
            - 't2kf10u' for 'CC BY 3.0 CH + OpenStreetMap'
            - '5sylls5' for 'CC BY 4.0'
            - '4bj8ceb' for 'CC0 1.0'
            - 'hmpvfpp' for 'Freie Nutzung. Kommerzielle Nutzung nur mit Bewilligung des Datenlieferanten zulässig.'
            - 'ce0mv1b' for 'Freie Nutzung. Quellenangabe ist Pflicht. Kommerzielle Nutzung nur mit Bewilligung des
                            Datenlieferanten zulässig.'
            - 'vzo5u7j' for 'GNU General Public License 3'
            - 'r617wgj' for 'Nutzungsbedingungen für Geodaten des Kantons Basel-Stadt'

    """
    global _currently_valid_ids
    if dataset_id is not None and dataset_uid is not None:
        exit(f"Error: dataset_id ({dataset_id}) and dataset_uid ({dataset_uid}) can't both be specified.")
    if dataset_id is None and dataset_uid is None:
        exit("Error: dataset_id or dataset_uid have to be specified.")
    if dataset_id is not None:
        dataset_uid = get_uid_by_id(dataset_id)
    base_url = get_base_url()

    if no_license_default_value in _currently_valid_ids:
        exit(f"Error: no_license_default_value ({no_license_default_value}) must not appear in {_currently_valid_ids}")

    r = requests_get(url=f"{base_url}/datasets/{dataset_uid}")

    if not r.ok:
        r.raise_for_status()

    lic_text = r.json()['metadata']['internal'].get('license_id', {}).get('value', no_license_default_value)


    if lic_text not in _currently_valid_ids and lic_text not in no_license_default_value:
        raise ValueError(f"Unknown license id {lic_text} received. Currently valid ids are: {_currently_valid_ids}")

    return lic_text
