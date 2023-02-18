from src.infra.repositories.user_repository import UserRepository
from src.application.entities.user import User


def test_create_user():
    user = User(name="John Nick", email="testando@gmail.com", telephone="32999999999", password="123456")
    assert user is not None


def test_create_user_bd():
    pass


def test_create_user_without_name():
    user = User(name="John Nick", email="johnnick+3@hotmail.com", telephone="32999999999")
    assert user.name == "John Nck"
