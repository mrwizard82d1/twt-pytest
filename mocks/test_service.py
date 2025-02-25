"""An example of mocking an entire class."""


from service import UserService, ApiClient


def test_get_username_with_mock(mocker):
    # Creates a mock `ApiClient`
    mock_api_client = mocker.Mock(spec=ApiClient)

    # Mock `get_user_data` to return a "fake" user
    mock_api_client.get_user_data.return_value = {'id': 1, 'name': 'Alice'}

    service = UserService(mock_api_client)  # Inject mock API client

    # Query the "service"
    result = service.get_username(1)

    # Assertions
    assert result == 'ALICE'  # Check if processing completed correctly
    mock_api_client.get_user_data.assert_called_once_with(1)  # Ensure API called correctly
