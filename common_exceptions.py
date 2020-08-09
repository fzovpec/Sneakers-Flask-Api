class DataException(Exception):
    def __init__(self, message):
        self.message = message


class IllegalArgumentsPassedToTheBotException(Exception):
    def __init__(self):
        self.message = 'Illegal arguments passed to the bot initializer'
