# Importing all the bots
from bots.nike import Bot

SERVER_ADDRESS = 'http://194.58.97.187/'

bots = [
    {
        'bot_name': 'nike',
        'bot_class': Bot,
        'login': {
            'isRequired': True,
            'loginInstantly': True,
            'loginBefore': True
        }
    }
]