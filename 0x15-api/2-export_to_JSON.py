#!/usr/bin/python3
""" Python script to export data in the JSON format. """

import json
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]
    user = requests.get(url + 'users/{}'.format(user_id)).json()
    todos = requests.get(url + 'todos?user_id={}'.format(user_id)).json()
    records = []
    for task in todos:
        records.append({
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': user.get('username')})
        data = {'{}'.format(user_id): records}
        with open('{}.json'.format(user_id), 'w') as json_file:
            json.dump(data, json_file)
