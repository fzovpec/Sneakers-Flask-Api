import unittest
from config import bots_list


class UseBotTest(unittest.TestCase):
    def test_getting_bot_from_bot_list(self):
        bot = bots_list['test']['bot_class']()
        result = bot.buy_item('Example link')
        self.assertTrue(result)
