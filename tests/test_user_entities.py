from fastapi import HTTPException
from src.application.service.user_service import UserService
import unittest
from unittest.mock import MagicMock


class TestUserService(unittest.TestCase):

    def setUp(self):
        self.db = MagicMock()
        self.user_repo = MagicMock()
        self.db.session.query.return_value.filter_by.return_value.first.return_value = None
        self.user_service = UserService(self.db)

    def test_create_user_success(self):
        self.user_service.repository = self.user_repo
        user = MagicMock()
        user.email = "test@example.com"
        self.user_repo.select_user_by_email.return_value = None
        self.user_repo.insert_simple.return_value = user
        result = self.user_service.create_user(user)
        self.assertEqual(result, user)

    def test_create_user_already_exists(self):
        self.user_service.repository = self.user_repo
        user = MagicMock()
        user.email = "test@example.com"
        self.user_repo.select_user_by_email.return_value = user
        with self.assertRaises(HTTPException) as context:
            self.user_service.create_user(user)
        self.assertEqual(context.exception.status_code, 400)
        self.assertEqual(context.exception.detail, "User already exists")
