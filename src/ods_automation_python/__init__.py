from ._config import get_api_key

# Just to make sure that the key is specified in the .env file, and immediately give an error if it is not
get_api_key()