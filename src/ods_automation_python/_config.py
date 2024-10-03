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
                             "PROXY_PORT"]

    for environment_variable in environment_variables:
        ev = os.getenv(environment_variable)
        if not ev:
            raise ValueError(f"{environment_variable} not found in the .env file. "
                             f"Please define it as '{environment_variable}'.")

def _get_api_key():
    return os.getenv('API_KEY')

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

# Example of how to use the function
if __name__ == "__main__":
    try:
        api_key = _get_api_key()
        print(f"API Key: {api_key}")
    except (FileNotFoundError, ValueError) as e:
        print(e)
