from flask import Flask, request
from flask_restful import Resource, Api
from common_exceptions import IllegalApiTypeException

app = Flask(__name__)
api = Api(app)


class OnDeviceApi(Resource):
    def __init__(self):
        self.data_manager = ''
        self.use_bot = ''

    def post(self):
        task_description_json = request.get_json()
        if task_description_json['type'] == 'manage_data':
            pass

        elif task_description_json['type'] == 'use_bot':
            pass

        else:
            raise IllegalApiTypeException(task_description_json['type'])
