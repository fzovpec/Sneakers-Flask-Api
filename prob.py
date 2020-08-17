import json
import requests


session = requests.Session()

data = {
    'type': 'login',
    'task': {
    }
}

response = session.post('http://127.0.0.1:5000/', json=data)
json_data = json.loads(response.text)

data = session.post('http://127.0.0.1:5000/', json={
    'type': 'manage_data',
    'access_token': json_data['access_token'],
    'task': {
      'data_manager': 'profiles',
      'action_type': 'get',
    }
})

print(data.text)
