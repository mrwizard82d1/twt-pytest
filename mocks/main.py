import requests


def get_weather(city):
    # This implementation makes a GET request to an external HTTPS
    # endpoint. However, I **do not** want to require access to this
    # endpoint in order to test this function. I will mock this
    # endpoint to avoid introduce this external dependency to my
    # test code (and to avoid the relatively slow performance of
    # an HTTPS call.
    response = requests.get(f'https://api.weather.com/v1/{city}')

    # The next code block contains the code we actually want to
    # unit test to ensure that **we** correctly handle different
    # HTTP status codes.
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError('Could not fetch weather data')
