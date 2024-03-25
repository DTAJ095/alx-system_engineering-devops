#!/usr/bin/python3
""" Export data in the csv format """

import csv
import requests
import sys


if __name__ == '__main__':
    url = url = 'https://jsonplaceholder.typicode.com/'

    user_id = sys.argv[1]
    user = requests.get(url + 'users/{}'.format(user_id)).json()
    todos = requests.get(url + 'todos?user_id={}'.format(user_id)).json()
    with open("{}.csv".format(user_id), 'w', newline='') as csvfile:
        _writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            _writer.writerow([int(user_id), user.get('username'),
                              task.get('completed'), task.get('title')])
