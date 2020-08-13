from botfather import BotFather


class TestBot:
    def __init__(self):
        pass

    @staticmethod
    def buy_item(item_link: str, billing_data=None, shipping_data=None, profile_data=None, proxies_data=None):
        print('Buying an item...')
        return True

    @staticmethod
    def register(billing_data=None, shipping_data=None, profile_data=None, proxies_data=None):
        print('Registered the user')
        return True

    @staticmethod
    def login(profiles_data=None):
        print('Logged the user')
        return True
