import pytest
from main import UserManager


# Replace fixture with "global variable"
# @pytest.fixture
# def user_manager():
#     """
#     Creates a fresh instance of `UserManager` before each test.
#     :return: A fresh instance of `UserManager`
#     """
#     return UserManager()
user_manager = UserManager()


def test_add_user():
    assert user_manager.add_user('john doe', 'john@example.com')
    assert user_manager.get_user('john doe') ==  'john@example.com'


def test_add_duplicate_user():
    # Now the first line raises a `ValueError` because user, 'john doe',
    # was added by the previous test. (Tests run from top to bottom
    # of file.)
    user_manager.add_user('john doe', 'john@example.com')
    with pytest.raises(ValueError):
        user_manager.add_user('john doe', 'john@example.com')
