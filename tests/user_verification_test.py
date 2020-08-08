import unittest
from config import SERVER_ADDRESS
from getmac import get_mac_address as gma
from user_verification import UserVerification
import requests


class UserVerificationTest(unittest.TestCase):
    def test_correct_user(self):
        # Initializing the session and data for request
        session = requests.Session()
        data = {
            "data": {
                "username": "root",
                "password": "password",
                "key": """1024 символа ключа кода""",
                "mac": str(gma()),
                "product_id": "<id>"
            }
        }

        # Testing
        user_verifyer = UserVerification('{}{}'.format(SERVER_ADDRESS, '/api/auth/keys/'))
        response = user_verifyer.verify(data=data, session=session)
        self.assertTrue(response)

    def test_other_users_key(self):
        pass

    def test_non_existing_key(self):
        pass

    def test_invalid_login(self):
        pass

    def test_invalid_password(self):
        pass
