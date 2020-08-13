from config import bots_list
from common_exceptions import IllegalApiBotManagerActionTypeException
from api.manage_data import DataManager
import warnings


class BotManager:
    def __init__(self):
        self.bot_list = bots_list
        self.data_manager = DataManager()

    def execute_the_bot_task(self, task_description_json, user_session):
        bot_name = task_description_json['task']['bot_name']
        bot = self.bot_list[bot_name]['bot_class']()
        shop_name = self.bot_list[bot_name]['shop']
        action_type = task_description_json['task']['action_type']
        profiles_idx, billing_idx, shipping_idx, proxies_idx, items_idx = \
            self.get_the_idx_for_the_data_types(task_description_json)

        profiles, billing, shipping, proxies, items = self.get_the_users_data(user_session=user_session,
                                                                              shop_name=shop_name,
                                                                              profile_idx=profiles_idx,
                                                                              billing_idx=billing_idx,
                                                                              shipping_idx=shipping_idx,
                                                                              items_idx=items_idx,
                                                                              proxies_idx=proxies_idx)

        if action_type == 'buy':
            item_link = task_description_json['task']['item_link']
            self.buy(bot, item_link=item_link, profiles=profiles, billing=billing, shipping=shipping, proxies=proxies)
        elif action_type == 'register':
            self.register(bot, profiles=profiles, billing=billing, shipping=shipping, proxies=proxies)
        elif action_type == 'login':
            self.login(bot, profiles=profiles)
        elif action_type == 'execute_whole_buying_process':
            self.execute_the_bot_task(bot, user_session=user_session)
        else:
            raise IllegalApiBotManagerActionTypeException(action_type)

    def get_the_users_data(self, user_session, profile_idx, shop_name, billing_idx, shipping_idx, proxies_idx, items_idx):
        ''' The function which gets the data for the bot execution, data like profiles or billing user data '''
        profiles = self.data_manager.profiles.get_the_data(session=user_session)
        billing = self.data_manager.billing.get_the_data(session=user_session)
        shipping = self.data_manager.shipping.get_the_data(session=user_session)
        proxies = self.data_manager.proxies.get_the_data(session=user_session)
        items = self.data_manager.items.get_the_data(session=user_session)
        # Getting the right data by the idx
        profiles = self.get_the_right_data_by_id(data_id=profile_idx, data=profiles, shop_name=shop_name)
        billing = self.get_the_right_data_by_id(data_id=billing_idx, data=billing, shop_name=shop_name)
        shipping = self.get_the_right_data_by_id(data_id=shipping_idx, data=shipping, shop_name=shop_name)
        proxies = self.get_the_right_data_by_id(data_id=proxies_idx, data=proxies, shop_name=shop_name)
        items = self.get_the_right_data_by_id(data_id=items_idx, data=items, shop_name=shop_name)

        return profiles, billing, shipping, proxies, items

    @staticmethod
    def get_the_right_data_by_id(data_id, shop_name, data):
        ''' Getting one instance by id of  the needed data with the correct shop '''
        data_with_correct_shop = []
        for instance in data:
            if instance['shop']['name'] == shop_name:
                data_with_correct_shop.append(instance)
        try:
            return data_with_correct_shop[data_id]
        except IndexError:
            warnings.warn('The data by the index {} doesn\'t exist'.format(data_id))
            return None

    @staticmethod
    def get_the_idx_for_the_data_types(task_description_json):
        profiles_idx = task_description_json['task']['profiles_id']
        billing_idx = task_description_json['task']['billing_id']
        shipping_idx = task_description_json['task']['shipping_id']
        proxies_idx = task_description_json['task']['proxies_id']
        items_idx = task_description_json['task']['item_id']

        return profiles_idx, billing_idx, shipping_idx, proxies_idx, items_idx

    @staticmethod
    def buy(bot, item_link, profiles=None, billing=None, shipping=None, proxies=None):
        bot.buy_item(item_link=item_link, billing_data=billing, profile_data=profiles, proxies_data=proxies,
                     shipping_data=shipping)

    @staticmethod
    def register(bot, profiles=None, billing=None, shipping=None, proxies=None):
        bot.register(billing_data=billing, shipping_data=shipping, profile_data=profiles, proxies_data=proxies)

    @staticmethod
    def login(bot, profiles):
        bot.login(profiles_data=profiles)

    def execute_whole_buying_process(self, bot, profiles, billing, shipping, proxies, items):
        pass
