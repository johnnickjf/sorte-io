from src.application.entities.user import User


def test_create_user_without_id():
    user = User(name="John Nick", email="johnnick+3@hotmail.com", telephone="32999999999")
    assert user.name == "John Nick" + " johnnick+3@hotmail.com"


def test_create_user_without_email():
    user = User(name="John Nick", email="johnnick+3@hotmail.com", telephone="32999999999")
    assert user.name == "John Nick"


def test_create_user_without_name():
    user = User(name="John Nick", email="johnnick+3@hotmail.com", telephone="32999999999")
    assert user.name == "John Nck"
