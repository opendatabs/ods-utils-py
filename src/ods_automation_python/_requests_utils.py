import requests
import urllib3, ssl

from ._config import _get_headers
from ._config import _get_proxies
from ._retry import retry

http_errors_to_handle = (ConnectionResetError, urllib3.exceptions.MaxRetryError, requests.exceptions.ProxyError,
                         requests.exceptions.HTTPError, ssl.SSLCertVerificationError)


@retry(http_errors_to_handle, tries=6, delay=5, backoff=1)
def requests_get(url: str, *args, **kwargs):
    r = requests.get(url=url, proxies=_get_proxies(), headers=_get_headers(), *args, **kwargs)
    r.raise_for_status()
    return r


@retry(http_errors_to_handle, tries=6, delay=5, backoff=1)
def requests_post(url: str, *args, **kwargs):
    r = requests.post(url=url, proxies=_get_proxies(), headers=_get_headers(), *args, **kwargs)
    r.raise_for_status()
    return r


@retry(http_errors_to_handle, tries=6, delay=5, backoff=1)
def requests_patch(url: str, *args, **kwargs):
    r = requests.patch(url=url, proxies=_get_proxies(), headers=_get_headers(), *args, **kwargs)
    r.raise_for_status()
    return r


@retry(http_errors_to_handle, tries=6, delay=5, backoff=1)
def requests_put(url: str, *args, **kwargs):
    r = requests.put(url=url, proxies=_get_proxies(), headers=_get_headers(), *args, **kwargs)
    r.raise_for_status()
    return r


@retry(http_errors_to_handle, tries=6, delay=5, backoff=1)
def requests_delete(url: str, *args, **kwargs):
    r = requests.delete(url=url, proxies=_get_proxies(), headers=_get_headers(), *args, **kwargs)
    r.raise_for_status()
    return r
