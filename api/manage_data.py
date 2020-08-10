from user_data_dealers.profiles import ProfilesDealer
from user_data_dealers.billing import BillingDealer
from user_data_dealers.proxies import ProxiesDealer
from user_data_dealers.items import ItemsDealer
from user_data_dealers.tasks import TasksDealer
from user_data_dealers.shipping import ShippingDealer
from common_exceptions import IllegalApiDataManagerActionTypeException, IllegalApiDataManagerNameException


class DataManager:
    def __init__(self):
        self.profiles = ProfilesDealer()
        self.billing = BillingDealer()
        self.items = ItemsDealer()
        self.proxies = ProxiesDealer()
        self.tasks = TasksDealer()
        self.shipping = ShippingDealer()

    def task_executor(self, task_description_json: dict, session):
        '''
            The function which executes any data managing request, like create a shop profile for the user
            :param task_description_json: the dict of the task description. See README for more information
            :param session: session used by the user
            :return: True if successful, otherwise raises an exception
        '''
        data_manager = task_description_json['task']['data_manager']  # The object which should be managing the data
        action_type = task_description_json['task']['action_type']  # The type of the action which should be executed
        task_data = task_description_json['task']  # The data for the data manager

        if data_manager == 'profiles':
            # Managing user profiles action
            self.execute_action(object_for_execution=self.profiles, action_type=action_type, task_data=task_data,
                                session=session)
        elif data_manager == 'billing':
            # Managing user billing action
            self.execute_action(object_for_execution=self.billing, action_type=action_type, task_data=task_data,
                                session=session)
        elif data_manager == 'items':
            # Managing user items action
            self.execute_action(object_for_execution=self.items, action_type=action_type, task_data=task_data,
                                session=session)
        elif data_manager == 'tasks':
            # Managing user tasks action
            self.execute_action(object_for_execution=self.tasks, action_type=action_type, task_data=task_data,
                                session=session)
        elif data_manager == 'shipping':
            # Managing user shopping action
            self.execute_action(object_for_execution=self.shipping, action_type=action_type, task_data=task_data,
                                session=session)
        elif data_manager == 'proxies':
            # Managing user proxies action
            self.execute_action(object_for_execution=self.proxies, action_type=action_type, task_data=task_data,
                                session=session)
        else:
            raise IllegalApiDataManagerNameException(data_manager)

        return True

    def execute_action(self, action_type: str, object_for_execution: object, task_data: dict, session):
        '''
            :param action_type: type of the action, like create, modify
            :param object_for_execution: object which should be executed
            :param task_data: the data for the task, see README for more information
        '''
        if action_type == 'create':
            data = task_data['data']
            object_for_execution.create_the_data(data=data, session=session)
        elif action_type == 'modify':
            data = task_data['data']
            required_id = task_data['required_id']
            object_for_execution.modify_the_data(data=data, session=session)
        elif action_type == 'get':
            object_for_execution.get_the_data(session=session)
        elif action_type == 'delete':
            required_id = task_data['required_id']
            object_for_execution.delete_the_data(session=session, required_id=required_id)
            pass
        else:
            raise IllegalApiDataManagerActionTypeException(action_type)