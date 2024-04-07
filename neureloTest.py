from neurelo.configuration import Configuration
from neurelo.api_client import ApiClient

configuration = Configuration(
	host=NEURELO_API_HOST,
	api_key={'ApiKey': NEURELO_API_KEY}
)

api_client = ApiClient(configuration=configuration)