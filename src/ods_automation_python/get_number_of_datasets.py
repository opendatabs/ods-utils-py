import requests
from ._config import _get_ods_url
from ._config import _get_api_key
from ._config import _get_proxies
__all__ = ["get_number_of_datasets"]

def get_number_of_datasets():
    print("Test")
    base_url = _get_ods_url()
    headers={'Authorization': f'apikey {_get_api_key()}'}
    r = requests.get(url=f"{base_url}/datasets/",
                 headers=headers,
                 proxies=_get_proxies())
    print(r.json()['total_count'])
    pass
