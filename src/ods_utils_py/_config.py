"""
This module is responsible for loading environment variables from the .env file.
"""

import os

from dotenv import load_dotenv

# TODO: Once there are no credentials.py files in use anymore, only use this code instead of load_environment_variable
'''
if not os.path.exists(".env"):
    raise FileNotFoundError("The .env file does not exist.")
load_dotenv(".env")
'''

def load_environment_variable(key):
    if os.path.exists('.env'):
        load_dotenv('.env')
        value = os.getenv(key)
        return value

    elif os.path.exists('credentials.py'):
        try:
            import credentials

            if hasattr(credentials, key):
                return getattr(credentials, key)
        except Exception as e:
            print(f"Error loading environment.py: {e}")
            return None

    else:
        raise FileNotFoundError("The .env file does not exist. The file credentials.py is also not found.")

def _check_all_environment_variables_are_set():
    environment_variables = ["ODS_API_KEY",
                             "PROXY_USER",
                             "PROXY_PASSWORD",
                             "PROXY_ADDRESS",
                             "PROXY_PORT",
                             "ODS_DOMAIN",
                             "ODS_API_TYPE"]

    for environment_variable in environment_variables:
        ev = load_environment_variable(environment_variable)
        if not ev:
            raise ValueError(f"{environment_variable} not found in the .env file. "
                             f"Please define it as '{environment_variable}'.")
        if ev == "your_" + environment_variable.lower():
            raise ValueError(f"Please define the environment variable '{environment_variable}' in the .env file.")


def get_base_url() -> str:
    return _get_ods_url()

def _get_ods_url() -> str:
    """
    Constructs the ODS (Open Data Service) API URL based on environment variables.

    Returns:
        str: The constructed ODS API URL **without** trailing slash ('/'): https://<ODS_DOMAIN>/api/<ODS_API_TYPE>
    """
    _ods_domain = load_environment_variable('ODS_DOMAIN')
    _ods_api_type = load_environment_variable('ODS_API_TYPE')
    _url_no_prefix = f"{_ods_domain}/api/{_ods_api_type}".replace("//", "/")
    _url = "https://" + _url_no_prefix
    return _url

def _get_headers():
    _api_key = load_environment_variable('ODS_API_KEY')
    _headers = {'Authorization': f'apikey {_api_key}'}
    return _headers

def _get_proxies() -> dict[str, str]:
    proxy_user = load_environment_variable("PROXY_USER")
    proxy_password = load_environment_variable("PROXY_PASSWORD")
    proxy_address = load_environment_variable("PROXY_ADDRESS")
    proxy_port = load_environment_variable("PROXY_PORT")

    proxy = f"http://{proxy_user}:{proxy_password}@{proxy_address}:{proxy_port}/"
    proxies = {
        "http": proxy,
        "https": proxy,
    }
    return proxies
