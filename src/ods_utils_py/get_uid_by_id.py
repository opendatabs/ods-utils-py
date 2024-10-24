from ._requests_utils import *  # imports requests_get, requests_post, etc.
from ._config import get_base_url

def get_uid_by_id(ods_id: str) -> str:
    base_url = get_base_url()
    params = {'dataset_id': ods_id}

    response = requests_get(url=f"{base_url}/datasets/", params=params)
    dataset_uid = response.json()['results'][0]['uid']
    return dataset_uid
