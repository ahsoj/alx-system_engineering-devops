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

    with open("todo_all_employees.json", 'w') as jsonFile:
        for i in range(len(__url)):
            username = __url_2[int(__url[i]['userId']) - 1]['username']
            json.dump({__url[i]['userId']: [{
                        "username": username,
                        "task": __url[i]['title'],
                        "completed": __url[i]['completed'],
                        }]}, jsonFile)


if __name__ == "__main__":
    main()
