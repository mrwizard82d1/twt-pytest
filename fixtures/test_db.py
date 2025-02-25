import pytest
from db import Database


@pytest.fixture
def db():
    """
    Provides a fresh instance of the `Database` class and cleans up
    after each test.

    This implementation, using `yield` to return the fixture, is more
    robust than previous usages of `pytest.fixture`.
    """

    database = Database()
    # Return the test database (a fixture instance)
    yield database
    # Clean the database when test finished.
    # Not necessary for an in-memory database, but useful for
    # real databases.
    database.data.clear()  # Clear the database


def test_add_user(db):
    db.add_user(1, 'Alice')
    assert db.get_user(1) == 'Alice'


def test_add_duplicate_user(db):
    db.add_user(1, 'Alice')
    with pytest.raises(ValueError, match='User already exists'):
        db.add_user(1, 'Bob')


def test_delete_user(db):
    db.add_user(2, 'Bob')
    db.delete_user(2)
    assert db.get_user(2) is None
