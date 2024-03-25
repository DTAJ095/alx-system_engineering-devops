#!/usr/bin/python3
""" Python script using REST API that returns information
about an employee TODO list progress
"""

import sys
import requests


if __name__ == '__main__':

    user_id = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(user_id))

    EMPLOYEE_NAME = user.json().get('EMPLOYEE_NAME')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
    TOTAL_NUMBER_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0

    for task in todos.json():
        if task.get('user_id') == int(user_id):
            TOTAL_NUMBER_OF_TASKS += 1
            if task.get('NUMBER_OF_DONE_TASKS'):
                NUMBER_OF_DONE_TASKS += 1
    print('Employee {} is done with tasks({}/{}):'
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    print('\n'.join(["\t " + task.get('title') for task in todos.json()
                     if task.get('user_id') == int(user_id)
                     and task.get('NUMBER_OF_DONE_TASKS')]))
