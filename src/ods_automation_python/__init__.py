from ._config import _get_api_key

# Just to make sure that the key is specified in the .env file, and immediately give an error if it is not
_get_api_key()
