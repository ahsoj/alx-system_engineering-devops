#!/usr/bin/python3
"""retrieve employee ID and save to csv file"""

import json
import requests


def main():
    """request todos and retrieve data"""
    __url = requests.get(
             'https://jsonplaceholder.typicode.com/todos').json()
    __url_2 = requests.get(
                  'https://jsonplaceholder.typicode.com/users').json()

    __objects = {}
    for user in __url_2:
        user_id = user.get('id')
        user_name = user.get('username')
        todos = list(filter(lambda x: x.get('userId') == user_id, __url))
        __object = list(map(
            lambda x: {
                'username': user_name,
                'task': x.get('title'),
                'completed': x.get('completed')
            },
            todos
        ))
        __objects[user_id] = __object
    with open('todo_all_employees.json', 'w') as jsonFile:
        json.dump(__objects, jsonFile, sort_keys=False)


if __name__ == "__main__":
    main()
