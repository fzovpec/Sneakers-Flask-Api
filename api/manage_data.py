from user_data_dealers.profiles import ProfilesDealer
from user_data_dealers.billing import BillingDealer
from user_data_dealers.proxies import ProxiesDealer
from user_data_dealers.items import ItemsDealer
from user_data_dealers.tasks import TasksDealer
from user_data_dealers.shipping import ShippingDealer
from common_exceptions import IllegalApiDataManagerActionTypeException


class DataManager:
    def __init__(self):
        self.profiles = ProfilesDealer()
        self.billing = BillingDealer()
        self.items = ItemsDealer()
        self.proxies = ProxiesDealer()
        self.task = TasksDealer()
        self.shipping = ShippingDealer()

    def task_executor(self, task_description_json: dict, required_id=None):
        action_type = task_description_json['task']['action']
        if action_type == 'create':
            pass
        elif action_type == 'modify':
            pass
        elif action_type == 'get':
            pass
        elif action_type == 'delete':
            pass
        else:
            raise IllegalApiDataManagerActionTypeException(action_type)
