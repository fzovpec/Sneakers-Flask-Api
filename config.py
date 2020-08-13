# Importing all the bots
from bots.nike import Bot
from bots.test_bot import TestBot

SERVER_ADDRESS = 'http://194.58.97.187/'

bots_list = {
    'nike': {
        'shop': 'nike',
        'bot_class': Bot,
    },
    'test': {
        'shop': 'test',
        'bot_class': TestBot
    }
}
