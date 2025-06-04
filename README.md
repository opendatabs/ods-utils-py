# ods-utils-py
With `ods-utils-py`, the Automation API from Opendatasoft can be accessed directly from Python. A valid API key is required ([Create an API key](#set-up-api-key)). [The source code is publicly available on GitHub](https://github.com/opendatabs/ods-utils-py).

## Table of Contents

- [ods-utils-py](#ods-utils-py)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Requirements](#requirements)
  - [Getting Started](#getting-started)
    - [Set up API Key](#set-up-api-key)
    - [Set up Environment Variables](#set-up-environment-variables)
  - [Usage](#usage)
  - [Further Links](#further-links)
  - [License](#license)

---

## Installation

Installation via `pip`:

```bash
pip install ods-utils-py
```

---

## Requirements

- **Python Version:** 3.11 or higher
- **API Key:** A valid API key from Opendatasoft

---

## Getting Started

### Set up API Key

To use `ods-utils-py`, a valid API key from Opendatasoft is required.

[For OGD Basel, the API key can be created here](https://data.bs.ch/account/api-keys/).

For key creation on other platforms, click on the username button in the top right corner to open account settings. Under API Keys, custom keys with the appropriate permissions can be created.

The name should describe its purpose, for example, `"ods_utils_py - <Initial Key Name>"`

The API key requires the following 4 permissions:
- Browse all datasets
- Create new datasets
- Edit all datasets
- Publish own datasets

The API key is then required as an environment variable.

### Set up Environment Variables
Next, the environment variables must be defined. For this, add a `.env` file in the root directory with the following content. If a `.env` already exists, just append the following content:

```.env
ODS_API_KEY=your_ods_api_key

ODS_DOMAIN=data.bs.ch
ODS_API_TYPE=automation/v1.0
```

**Important:** Make sure to add `**/.env` to your .gitignore to not upload the credentials to the internet!  
*Note:* If you are behind a proxy, set `http_proxy` and `https_proxy` accordingly

## Usage

Here's a simple example to retrieve the number of datasets:

```python
import ods_utils_py as ods_utils

num_datasets = ods_utils.get_number_of_datasets()
print(f"We currently have {num_datasets} datasets.")
```

A list of all currently implemented functions can be found on [GitHub](https://github.com/opendatabs/ods-utils-py/tree/main/src/ods_utils_py).

If a desired function does not exist, it can be implemented via _requests_utils:

```python
import ods_utils_py as ods_utils

response = ods_utils._requests_utils.requests_get("https://www.example.com")
print(response.text)
```

*Note:* Most of these functions should eventually be integrated into `ods_utils_py` if they use the Automation API.

---

## Further Links
The complete documentation of the Automation API 1.0 can be found [here](https://help.opendatasoft.com/apis/ods-automation-v1/).

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file in the repository for the full license text.

---