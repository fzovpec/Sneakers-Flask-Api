from config import bots_list
from common_exceptions import IllegalApiBotManagerActionTypeException
from api.manage_data import DataManager


class BotManager:
    def __init__(self):
        self.bot_list = bots_list
        self.data_manager = DataManager()

    def execute_the_bot_task(self, task_description_json, user_session):
        bot_name = task_description_json['task']['bot_name']
        bot = self.bot_list[bot_name]['bot_class']
        action_type = task_description_json['task']['action_type']
        if action_type == 'buy':
            self.buy(bot, user_session)
        elif action_type == 'register':
            self.register(bot, user_session)
        elif action_type == 'login':
            self.login(bot, user_session)
        elif action_type == 'execute_whole_buying_process':
            self.execute_the_bot_task(bot, user_session)
        else:
            raise IllegalApiBotManagerActionTypeException(action_type)

    def get_the_users_data(self, user_session):
        profiles = self.data_manager.profiles.get_the_data(session=user_session)
        billing = self.data_manager.billing.get_the_data(session=user_session)
        shipping = self.data_manager.shipping.get_the_data(session=user_session)
        pass

    def get_the_right_data_by_id(self, data_array, shop_name):
        pass

    def buy(self, bot, user_session):
        pass

    def register(self, bot, user_session):
        pass

    def login(self, bot, user_session):
        pass

    def execute_whole_buying_process(self, bot, user_session):
        pass
