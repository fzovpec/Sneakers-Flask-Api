import unittest
import requests
from user_verification import UserVerification
from user_data_dealers.billing import BillingDealer
from on_device_data_worker import JSONWorker


class BillingDealerTest(unittest.TestCase):
    @staticmethod
    def initialize_the_session():
        session = requests.Session()
        user_verifyer = UserVerification()
        status, authentication_cookie = user_verifyer.verify_from_json(session=session)
        session.headers['X-CSRFToken'] = authentication_cookie

        return session

    def test_billing_data_getting(self):
        billing = BillingDealer()
        session = self.initialize_the_session()
        response, _ = billing.get_the_data(session=session)
        self.assertTrue(response)

    def test_billing_data_creation(self):
        billing = BillingDealer()
        session = self.initialize_the_session()

        json_worker = JSONWorker()
        data = {
            "data": {
                "name": "VISA",
                "number": "1",
                "cvv": "2",
                "expdate": "222/22",
                "holder_name": "Misce",
                "product": json_worker.get_the_product_id_from_json(),
                "store": "Supreme"
            }
        }
        response, _ = billing.create_the_data(data=data, session=session)

        self.assertTrue(response)
