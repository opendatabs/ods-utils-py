import os
from dotenv import load_dotenv


def _get_api_key(env_file=".env"):

    # Load the environment variables from the specified .env file
    if not os.path.exists(env_file):
        raise FileNotFoundError(f"The .env file '{env_file}' does not exist.")

    load_dotenv(env_file)

    # Retrieve the API key from the environment variables
    api_key = os.getenv('API_KEY')
    if not api_key:
        raise ValueError("API key not found in the .env file. Please define it as 'API_KEY'.")

    return api_key


# Example of how to use the function
if __name__ == "__main__":
    try:
        api_key = _get_api_key()
        print(f"API Key: {api_key}")
    except (FileNotFoundError, ValueError) as e:
        print(e)
