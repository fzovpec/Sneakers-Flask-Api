from common_exceptions import DataException
from on_device_data_worker import JSONWorker
from config import SERVER_ADDRESS


class UserVerification:
    def __init__(self, verification_url='{}{}'.format(SERVER_ADDRESS, '/api/auth/keys/')):
        self.verification_url = verification_url
        self.json_data = JSONWorker()

    def verify(self, session, data):
        '''
            The function which verifies the user and verifies if the user can have access to the product
        '''
        response = session.post(self.verification_url, json=data)
        status = self.response_handler(response)
        self.json_data.set_the_data_to_json(data)

        return status, response.cookies['csrftoken']

    def verify_from_json(self, session):
        data = self.json_data.get_the_data_from_json()
        response = session.post(self.verification_url, json=data)
        status = self.response_handler(response)

        return status, response.cookies['csrftoken']

    def verify_existing_session(self, session):
        response = session.get(self.verification_url)
        if response.text == '"True"':
            return True
        return False

    @staticmethod
    def response_handler(response):
        if response.status_code == 200:
            return True
        raise DataException(response.text)
