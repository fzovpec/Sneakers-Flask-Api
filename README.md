# Sneakers-Flask-Api
On desktop API. Makes it simplier to interact with the server, bots and another sneakers software

## API interaction with the server
<b> The user should be logged in order to interact with this API. See user login section </b>

API makes it simplier to interact with the server from the app. Currently supports data management with user's profiles, proxies, billing information, items, tasks, shipping data. Can be modified or added some data managers in the <i>manage_data.py</i> file

The data managers themselves support creation, modyfing, getting and deletion of the user's info

To use it as a local web server API, send a post request to the server of the following form:
```
{
  'type': 'manage_data',
  'task': {
      'data_manager': 'The data manager needed for the task execution. Currently suppored data 
               managers are: profiles, billing, items, tasks, shipping, proxies'
      'action_type': 'What exactly you want a data manager to do. Currently supported - create,
              modify, get and delete
      'required_id': 'The id which is required for the modifying, deleting and getting the data 
               in some cases. If not used should be set to None'
      'data': 'The dictionary of data, which should be created according to the server API (Read server-side API README)
   }
}
```
Example of interaction with the API
```
{
  'type': 'manage_data',
  'task': {
      'data_manager': 'profiles'
      'action_type': 'create'
      'required_id': None
      'data': {
            'data': {
              'name': 'profile',
              'login': 'login',
              'email': 'email',
              'password': 'password',
              'firstname': 'name',
              'lastname': 'lastname',
              'middlename': 'middlename',
              'phone': '+223 12 322 32 21',
              'product': 'wr2eduh-2312i-231nf',
              'store': 'supreme'
           }
       }
   }
}
```
