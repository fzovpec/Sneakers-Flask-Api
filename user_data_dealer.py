from common_exceptions import DataException


class UserData:
    def __init__(self, get_data_url, modify_data_url, delete_data_url):
        self.get_data_url = get_data_url
        self.modify_data_url = modify_data_url
        self.delete_data_url = delete_data_url

    def get_the_data(self, data, session):
        '''
            Wrapper for all the function where the app should get some data from the server.
            Example: get all the tasks for some particular user or get his billing information for some
            particular shop
        '''
        response = session.post(self.get_data_url, json=data)
        status = self.response_handler(response)
        return status

    def modify_the_data(self, data, session, request_id):
        '''
            Wrapper for any modifying function.
            Example of usage: modify the users address information or billing information for some
            particular shop
            :param request_id: the modifying requires an id for modify the element. Can be get thought the
            get_the_data() method
        '''
        response = session.put('{}/{}'.format(self.get_data_url, request_id), json=data)
        status = self.response_handler(response)
        return status

    def delete_the_data(self, session, request_id):
        '''
            Wrapper for the deleting information data.
            Example of usage: deleting user's profile information for some particular shop or deleting
            the user's proxies information
        '''
        response = session.delete('{}/{}'.format(self.delete_data_url, request_id))
        status = self.response_handler(response)
        return status

    @staticmethod
    def response_handler(response):
        '''
            Handles the response of the server
            :param response: server response
            :return: True if successful, otherwise raises an Exception
        '''
        if response.status_code == 200:
            return True
        raise DataException(response.text)
