import unittest
import requests
from user_verification import UserVerification
from user_data_dealers.profiles import ProfilesDealer
from on_device_data_worker import JSONWorker


class ProfilesTest(unittest.TestCase):
    @staticmethod
    def initialize_the_session():
        session = requests.Session()
        user_verifyer = UserVerification()
        status, authentication_cookie = user_verifyer.verify_from_json(session=session)
        session.headers['X-CSRFToken'] = authentication_cookie

        return session

    def test_profile_data_creation(self):
        session = self.initialize_the_session()
        json_worker = JSONWorker()
        data = {
            "data": {
                "name": "test_name",
                "login": "ghe",
                "email": "1",
                "password": "1",
                "firstname": "1",
                "lastname": "1",
                "middlename": "1",
                "phone": "1",
                "product": json_worker.get_the_product_id_from_json(),
                "store": "Supreme"
            }
        }
        profile = ProfilesDealer()
        response, _ = profile.create_the_data(session=session, data=data)

        self.assertTrue(response)

    def ntest_profile_data_editing(self):
        session = self.initialize_the_session()

        json_worker = JSONWorker()
        pass

    def test_profile_data_getting(self):
        profile = ProfilesDealer()
        session = self.initialize_the_session()
        response, _ = profile.get_the_data(session=session)
        self.assertTrue(response)
