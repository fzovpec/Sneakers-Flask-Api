import json


class JSONWorker:
    @staticmethod
    def get_the_data_from_json():
        with open('config.json', 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
        return data

    @staticmethod
    def set_the_data_to_json(data):
        with open('config.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(data))
