# An example Web service

import requests

class ApiClient:
    """Simulates an external API client."""
    def get_user_data(self, user_id):
        response = requests.get(f'https://api.example.com/users/{user_id}')
        if response.status_code == 200:
            return response.json()

        raise ValueError('API request failed')


class UserService:
    """Uses APIClient to fetch user data and process it."""
    def __init__(self, api_client):
        self.api_client = api_client  # Dependency injection

    def get_username(self, user_id):
        """Fetches a user and returns the username in uppercase."""

        # Calls the client.
        user_data = self.api_client.get_user_data(user_id)

        # Processes the result
        return user_data['name'].upper()
