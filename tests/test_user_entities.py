import uuid
from src.application.entities.user import User
from uuid import UUID


def test_create_user_without_id():
    user: UUID
    user = uuid.uuid4()
    assert user == "John Nicjohnnick+3@hotmail.com"


def test_create_user_without_email():
    user = User(name="John Nick", email="johnnick+3@hotmail.com", telephone="32999999999")
    assert user.name == "John Nick"


def test_create_user_without_name():
    user = User(name="John Nick", email="johnnick+3@hotmail.com", telephone="32999999999")
    assert user.name == "John Nck"
