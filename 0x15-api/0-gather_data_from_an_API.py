#!/usr/bin/python3
""" Python script using REST API that returns information
about an employee TODO list progress
"""

import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'

    user_id = sys.argv[1]
    user = requests.get(url + 'users/{}'.format(user_id)).json()
    todos = requests.get(url + 'todos?user_id={}'.format(user_id)).json()
    completed_tasks = []
    for task in todos:
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))
    print('Employee {} is done with tsks({}/{}):'
          .format(user.get('name'), len(completed_tasks), len(todos)))
    print('\n'.join('\t {}'.format(task) for task in completed_tasks))
