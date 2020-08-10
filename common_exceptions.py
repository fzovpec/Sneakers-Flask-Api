class DataException(Exception):
    def __init__(self, message):
        self.message = message


class IllegalArgumentsPassedToTheBotException(Exception):
    def __init__(self):
        self.message = 'Illegal arguments passed to the bot initializer'


class IllegalApiTypeException(Exception):
    def __init__(self, inputted_type):
        self.message = '{} is illegal type. Only \"manage_data\" and \"use_bot\" are legal ones'.format(inputted_type)


class IllegalApiDataManagerActionTypeException(Exception):
    def __init__(self, action_type):
        self.message = '{} is illegal action type. Only \"create\", \"modify\", \"get\" and \"delete\" are legal' \
                       ' ones'.format(action_type)


class IllegalApiDataManagerNameException(Exception):
    def __init__(self, data_manager):
        self.message = '{} is illegal data manager name. Only \"profiles\", \"billing\", \"items\", \"tasks\",' \
                       ' \"shipping\" and \"proxies\" are legal ones'.format(data_manager)
