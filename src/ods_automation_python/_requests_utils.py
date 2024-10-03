import requests

from ._config import _get_ods_url
from ._config import _get_headers
from ._config import _get_proxies

base_url = _get_ods_url()

def get_base_url() -> str:
    return _get_ods_url()

def requests_get(url: str, *args, **kwargs):
    r = requests.get(url=url, proxies=_get_proxies(), headers=_get_headers(), *args, **kwargs)
    r.raise_for_status()
    return r

