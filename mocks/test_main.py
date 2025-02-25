from main import get_weather


def test_get_weather(mocker):
    # Mock `requests.get`
    mock_get = mocker.patch('main.requests.get')

    # Set return values of the mock
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'temperature': 25,
        'condition': 'sunny'
    }

    # Call function under test
    result = get_weather('Dubai')

    # Assertions

    # The first assertion tests that we receive what we set up
    assert result == {'temperature': 25, 'condition': 'sunny'}

    # The second assertion asserts that we only called the
    # API **exactly once** with the expected parameter.
    mock_get.assert_called_once_with('https://api.weather.com/v1/Dubai')
