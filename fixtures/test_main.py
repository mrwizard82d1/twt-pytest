import pytest
from main import UserManager


@pytest.fixture
def user_manager():
    """
    Creates a fresh instance of `UserManager` before each test.
    :return: A fresh instance of `UserManager`
    """
    return UserManager()


def test_add_user(user_manager):
    assert user_manager.add_user('john doe', 'john@example.com')
    assert user_manager.get_user('john doe') ==  'john@example.com'


def test_add_duplicate_user(user_manager):
    user_manager.add_user('john doe', 'john@example.com')
    with pytest.raises(ValueError):
        user_manager.add_user('john doe', 'john@example.com')
