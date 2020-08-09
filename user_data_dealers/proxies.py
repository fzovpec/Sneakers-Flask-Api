from user_data_dealer import UserData


class ProxiesDealer(UserData):
    def __init__(self):
        super().__init__(server_data_dealer_url='http://194.58.97.187/api/data/proxies/')
