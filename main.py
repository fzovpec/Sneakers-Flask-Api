from flask import Flask, request
from flask_restful import Resource, Api
from common_exceptions import IllegalApiTypeException
from user_verification import UserVerification
from common_exceptions import DataException, CannotLogUsingJSONException
import requests

app = Flask(__name__)
api = Api(app)


class OnDeviceApi(Resource):
    def __init__(self):
        self.data_manager = ''
        self.use_bot = ''
        self.user_verification = UserVerification()
        self.session = requests.Session()

    def post(self):
        task_description_json = request.get_json()
        if task_description_json['type'] == 'login':
            self.verify_the_user(task_dictionary=task_description_json['task'])
            return {'Result': 'Successfully logged in'}

        elif task_description_json['type'] == 'manage_data':
            pass

        elif task_description_json['type'] == 'use_bot':
            pass

        else:
            raise IllegalApiTypeException(task_description_json['type'])

    def verify_the_user(self, task_dictionary):
        ''' User verification using the data dictionary or data stored on the json file '''
        try:
            data = task_dictionary['data']
            self.user_verification.verify(session=self.session, data=data)
        except KeyError:
            # yeah, I know
            try:
                self.user_verification.verify_from_json(session=self.session)
            except DataException as ex:
                raise CannotLogUsingJSONException(ex.message)
