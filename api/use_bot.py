from config import bots_list
from common_exceptions import IllegalApiBotManagerActionTypeException


class BotManager:
    def __init__(self):
        self.bot_list = bots_list

    def execute_the_bot_task(self, task_description_json):
        bot_name = task_description_json['task']['bot_name']
        bot = self.bot_list[bot_name]['bot_class']
        action_type = task_description_json['task']['action_type']
        if action_type == 'buy':
            self.buy(bot)
        elif action_type == 'register':
            self.register(bot)
        elif action_type == 'login':
            self.login(bot)
        elif action_type == 'execute_whole_buying_process':
            self.execute_the_bot_task(bot)
        else:
            raise IllegalApiBotManagerActionTypeException(action_type)

    def buy(self, bot):
        pass

    def register(self, bot):
        pass

    def login(self, bot):
        pass

    def execute_whole_buying_process(self, bot):
        pass
