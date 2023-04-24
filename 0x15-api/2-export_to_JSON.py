#!/usr/bin/python3
"""retrieve employee ID and save to csv file"""

import json
import requests


def main(arg):
    """request todos and retrieve data"""
    __url = requests.get(
             'https://jsonplaceholder.typicode.com/todos/?userId={id}'.format(
                                 id=arg)).json()
    __url_2 = requests.get(
                  'https://jsonplaceholder.typicode.com/users/{id}'.format(
                                  id=arg)).json()

    with open("{}.json".format(arg), 'w') as jsonFile:
        pack = []
        for i in range(len(__url)):
            pack.append({"task": __url[i]['title'],
                        "completed": __url[i]['completed'],
                         "username": __url_2['username']})
        __objs = {arg: pack}
        json.dump(__objs, jsonFile, sort_keys=False)


if __name__ == "__main__":
    from sys import argv
    main(argv[1])
