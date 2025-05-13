"""
This module provides utility functions for making HTTP requests with retry functionality.
It wraps the requests library methods with custom error handling and configuration.
"""

from functools import wraps
import time
import logging

# Source: https://github.com/saltycrane/retry-decorator/blob/master/retry_decorator.py
# BSD license: https://github.com/saltycrane/retry-decorator/blob/master/LICENSE
def retry(ExceptionToCheck, tries=4, delay=3, backoff=2, logger=None):
    """Retry calling the decorated function using an exponential backoff.

    https://www.saltycrane.com/blog/2009/11/trying-out-retry-decorator-python/
    original from: https://wiki.python.org/moin/PythonDecoratorLibrary#Retry

    :param ExceptionToCheck: the exception to check. may be a tuple of
        exceptions to check
    :type ExceptionToCheck: Exception or tuple
    :param tries: number of times to try (not retry) before giving up
    :type tries: int
    :param delay: initial delay between retries in seconds
    :type delay: int
    :param backoff: backoff multiplier e.g. value of 2 will double the delay
        each retry
    :type backoff: int
    :param logger: logger to use. If None, print
    :type logger: logging.Logger instance
    """
    def deco_retry(f):

        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except ExceptionToCheck as e:
                    msg = "%s, Retrying in %d seconds..." % (str(e), mdelay)
                    if logger:
                        logger.warning(msg)
                    else:
                        print(msg)
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return f(*args, **kwargs)

        return f_retry  # true decorator

    return deco_retry

##################################################################
##################################################################
##################################################################
import requests
import urllib3, ssl

from ._config import _get_headers

http_errors_to_handle = (ConnectionResetError, urllib3.exceptions.MaxRetryError, requests.exceptions.ProxyError,
                         requests.exceptions.HTTPError, ssl.SSLCertVerificationError)


@retry(http_errors_to_handle, tries=6, delay=5, backoff=1)
def requests_get(url: str, *args, **kwargs):
    r = requests.get(url=url, headers=_get_headers(), *args, **kwargs)
    r.raise_for_status()
    return r


@retry(http_errors_to_handle, tries=6, delay=5, backoff=1)
def requests_post(url: str, *args, **kwargs):
    r = requests.post(url=url, headers=_get_headers(), *args, **kwargs)
    r.raise_for_status()
    return r


@retry(http_errors_to_handle, tries=6, delay=5, backoff=1)
def requests_patch(url: str, *args, **kwargs):
    r = requests.patch(url=url, headers=_get_headers(), *args, **kwargs)
    r.raise_for_status()
    return r


@retry(http_errors_to_handle, tries=6, delay=5, backoff=1)
def requests_put(url: str, *args, **kwargs):
    r = requests.put(url=url, headers=_get_headers(), *args, **kwargs)
    r.raise_for_status()
    return r


@retry(http_errors_to_handle, tries=6, delay=5, backoff=1)
def requests_delete(url: str, *args, **kwargs):
    r = requests.delete(url=url, headers=_get_headers(), *args, **kwargs)
    r.raise_for_status()
    return r
