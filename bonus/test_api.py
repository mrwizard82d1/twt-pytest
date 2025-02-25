import pytest
from api import app  # Import the Flask app


@pytest.fixture
def client():
    """Provides a test client for the Flask app."""
    app.config['TESTING'] = True  # Enable testing code
    with app.test_client() as client:
        yield client  # Provide the test client instance


def test_add_user(client):
    """Test adding a new user."""
    response = client.post('/users', json={'id': 1, 'name': 'Alice'})

    assert response.status_code == 201
    assert response.json == {'id': 1, 'name': 'Alice'}


def test_get_user(client):
    """Test getting a user."""

    # First, add a user to my "database"
    client.post('/users', json={'id': 2, 'name': 'Bob'})

    # Then return the user that I just added
    response = client.get('/users/2')

    # Assert the correct data returned and correct calls made
    assert response.status_code == 200
    assert response.json == {'id': 2, 'name': 'Bob'}


def test_get_user_not_found(client):
    """Test retrieving a not-existing user."""
    response = client.get('/users/99')

    assert response.status_code == 404
    assert response.json == {'error': 'User not found'}


def test_add_duplicate_user(client):
    """Test adding a duplicate user."""
    client.post('/users', json={'id': 3, 'name': 'Charlie'})
    response = client.post('/users', json={'id': 3, 'name': 'Charlie'})

    assert response.status_code == 400
    assert response.json == {'error': 'User already exists'}
