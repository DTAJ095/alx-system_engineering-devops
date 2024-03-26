#!/usr/bin/python3
"""
extend your Python script to export data in the JSON format
"""

import json
import requests
import sys

if __name__ == '__main__':
    endpoint = "https://jsonplaceholder.typicode.com/"
    data = {}
    users = requests.get(endpoint + "users").json()
    for user in users:
        records = []
        todos = requests.get(endpoint + "todos?userId={}"
                             .format(user.get('id'))).json()
        for task in todos:
            records.append({
                "username": user.get('username'),
                "task": task.get('title'),
                "completed": task.get('completed')
            })
        data["{}".format(user.get('id'))] = records

    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(data, json_file)
