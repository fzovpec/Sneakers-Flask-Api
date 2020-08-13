from datetime import datetime
import time
from common_exceptions import IllegalArgumentsPassedToTheBotException


class BotFather:
    def __init__(self, bot_name: str, is_login_required: bool, login_instantly:bool, login_before:int):
        self.bot_name = bot_name
        self.is_login_required = is_login_required
        self.login_instantly = login_instantly
        self.login_before = login_before

    def check_the_arguments(self):
        if self.is_login_required and self.login_before:
            raise IllegalArgumentsPassedToTheBotException()

    def execute_login_task(self, task_time, login_data: dict):
        '''
            The wrapper for the logining function
            :param task_time: the approximate time of the task execution. Used only if login is not instant
            :param login_data: the data required for login. For example login and password
        '''
        if self.is_login_required:
            if self.login_instantly:
                self.login(login_data)

            elif not self.login_instantly and self.login_before:
                current_moment = datetime.now()
                datetime_login_before = datetime(year=current_moment.year, month=current_moment.month,
                                                 day=current_moment.day, second=self.login_before)
                print('Waiting to login...')
                self.wait_until_a_particular_moment(task_time - datetime_login_before)
                self.login(login_data)

    def register(self, billing_data=None, shipping_data=None, profile_data=None,
                 proxies_data=None):
        '''
            Wrapper for the function executing. The monitor sends a link and the item gets bought
            :param item_link - The link using which the item's getting bought
            :param billing_data, address_data, profile_data, proxies_data - user billing data.
             Provided only if required for item buying
        '''
        pass

    def buy_item(self, item_link: str, billing_data=None, shipping_data=None, profile_data=None,
                 proxies_data=None):
        '''
            The wrapper for buying item function. Should be overwritten by the bot. The arguments should be the same,
            even if some of them are not used
        '''
        pass

    def login(self, profiles_data):
        ''' The wrapper for the login function. Should be overwritten by the bot class. The arguments should remain
        the same'''
        pass

    @staticmethod
    def wait_until_a_particular_moment(datetime_wait_until):
        seconds_interval = (datetime_wait_until - datetime.now()).total_seconds()
        time.sleep(seconds_interval)
