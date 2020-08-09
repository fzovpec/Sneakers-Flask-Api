from common_exceptions import DataException


class UserVerification:
    def __init__(self, verification_url):
        self.verification_url = verification_url

    def verify(self, session, data):
        '''
            The function which verifies the user and verifies if the user can have access to the product
        '''
        response = session.post(self.verification_url, json=data)
        status = self.response_handler(response)

        return status, response.cookies['csrftoken']

    @staticmethod
    def response_handler(response):
        if response.status_code == 200:
            return True
        raise DataException(response.text)
