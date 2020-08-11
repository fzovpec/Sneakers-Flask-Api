# Sneakers-Flask-Api
On desktop API. Makes it simplier to interact with the server, bots and another sneakers software

## API User Login

API makes it possible to login into the server using the on device app. Logining is required to do all the other operations, like executing bots in order to buy products. In order to login using the API you have to send a post request of the following form

```
{
  'type': 'login',
  'task': {
    'data': 'The data required by server to login. For more information read a server-side API
          README'
    }
}
```

After the first loggining the data gets saved to the config.json file.

If you want to execute the login with the json data saved on the device, then send a request of the following form

```
{
  'type': 'login',
  'task': {}  # IMPORTANT: in order to login using the config.json data leave the task dict empty 
}
```

## API interaction with the server
<b> The user should be logged in order to interact with this API. See API User Login </b>

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

## API interaction with the bots

In order to use the bots from the API, you need to send the post request of the following form:
```
{
  'type': 'use_bot',
  'task': {
    'bot_name': 'The name of the bot you want to execute. The bot should be listed in 
        the bots_list dictionary in the config.py file. More about that in the adding new bots section.
    'action_type': 'The type of the action you want to execute. Allowed actions - login, register, buy, 
        execute_whole_buying_process and another listed in the bot class definition. More about
        those actions is written in the adding bots section',
    'profiles_id': 'The id of the profile out of the user profiles list(in some particular shop). If not specified, then used 0 by default',
    'billing_id': 'The id of the user's billing information. 0 by default',
    'proxies_id': 'The id of the user's proxies. 0 by default',
    'item_id': 'Required if action_type == execute_whole_buying_process. Otherwise not required',
    'shipping_id': 'The id of the user's shipping data list. 0 by default'
  }
}
```
