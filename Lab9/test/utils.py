# Panyawut Saengdaeng 653380138-3 Sec.1
from io import BytesIO
from requests.models import Response

def get_mock_currency_api_response():
    """
    Method to create a mock response from the Currency API
    """
    # Create a mock response object
    mock_api_response = Response()
    mock_api_response.status_code = 200

    # Mock the JSON response from the API
    mock_api_response._content = b'{ "base": "THB", "result": { "KRW": 38.69 } }'

    return mock_api_response


example = get_mock_currency_api_response().json()
print(type(example), example)
