# Neurelo SDK

The generated Neurelo Python SDK provides easy access to your Neurelo APIs for Python applications.

# Installation

- After the SDK .tgz file has been downloaded, move it to your project repository
- Run `pip install path/to/sdk-tgz`
- This will install the SDK to your available packages under the name `neurelo`
- It is recommended to use `pyenv` + `virtualenv` extension to have a clean way to install/uninstall packages

## Requirements

- No extra packages are required, `pip install` should take care of installing everything to get the SDK package working

# Usage

## Environment Configuration

It’s recommended to load the Neurelo API URL and token from env variables. The [python-dotenv](https://pypi.org/project/python-dotenv/) package can be used to load them from an `.env` file while working on a local environment.

```python
from dotenv import load_dotenv

load_dotenv()

NEURELO_API_HOST = os.getenv("NEURELO_API_HOST") or ""
NEURELO_API_KEY = os.getenv("NEURELO_API_KEY") or ""
```

## API Usage

The basic usage just requires a `Configuration` and `ApiClient` instance:

```python
from neurelo.configuration import Configuration
from neurelo.api_client import ApiClient

configuration = Configuration(
	host=NEURELO_API_HOST,
	api_key={'ApiKey': NEURELO_API_TOKEN}
)
api_client = ApiClient(configuration=configuration)
```

The access to each individual schema model API can reuse the `api_client`. Assuming the neurelo schema has a `User` object:

```python
from neurelo.api.user_api import UserApi

user_api = UserApi(api_client)
```

Some parameters are encapsulated within specific classes, when calling operations that require such parameters, an instance has to be created and used as the parameter value:

```python
from neurelo import models

payload = models.UserCreateInput(
  email=email,
  fullname=fullname,
  password=password,
)

user = user_api.create_one_user(payload)
```

All parameters for all operations have type hints, so it’s easy to figure out which model is required or if it can just be a raw value.
