'''
This module is responsible for loading environment variables from the .env file.
'''
import os

from dotenv import load_dotenv

load_dotenv(".env")
if not os.path.exists(".env"):
    raise FileNotFoundError("The .env file does not exist.")

def _check_all_environment_variables_are_set():
    environment_variables = ["API_KEY",
                             "PROXY_USER",
                             "PROXY_PASSWORD",
                             "PROXY_ADDRESS",
                             "PROXY_PORT",
                             "ODS_DOMAIN",
                             "ODS_API_TYPE"]

    for environment_variable in environment_variables:
        ev = os.getenv(environment_variable)
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
    _ods_domain = os.getenv('ODS_DOMAIN')
    _ods_api_type = os.getenv('ODS_API_TYPE')
    _url_no_prefix = f"{_ods_domain}/api/{_ods_api_type}".replace("//", "/")
    _url = "https://" + _url_no_prefix
    return _url

def _get_headers():
    _api_key = os.getenv('API_KEY')
    _headers = {'Authorization': f'apikey {_api_key}'}
    return _headers

def _get_proxies() -> dict[str, str]:
    proxy_user = os.getenv("PROXY_USER")
    proxy_password = os.getenv("PROXY_PASSWORD")
    proxy_address = os.getenv("PROXY_ADDRESS")
    proxy_port = os.getenv("PROXY_PORT")

    proxy = f"http://{proxy_user}:{proxy_password}@{proxy_address}:{proxy_port}/"
    proxies = {
        "http": proxy,
        "https": proxy,
    }
    return proxies
