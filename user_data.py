class UserData:
    def __init__(self, get_data_url, modify_data_url, delete_data_url):
        self.get_data_url = get_data_url
        self.modify_data_url = modify_data_url
        self.delete_data_url = delete_data_url

    def get_the_data(self, data, session):
        response = session.post(self.get_data_url, json=data)
        status = self.response_handler(response)
        return status

    def modify_the_data(self, data, session, request_id):
        response = session.put('{}/{}'.format(self.get_data_url, request_id), json=data)
        status = self.response_handler(response)
        return status

    def delete_the_data(self, session, request_id):
        response = session.delete('{}/{}'.format(self.delete_data_url, request_id))
        status = self.response_handler(response)
        return status

    def response_handler(self, response):
        if response.status_code == 200:
            return True
        raise
