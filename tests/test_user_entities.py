from src.infra.repositories.user_repository import UserRepository
from src.application.entities.user import User
from src.application.service.login_service import LoginService


def test_create_user():
    user = User(name="John Nick", email="testando@gmail.com", telephone="32999999999", password="123456")
    assert user is not None


def test_create_user_bd():
    pass


def test_authenticate_user():
    pass