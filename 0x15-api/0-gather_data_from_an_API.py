#!/usr/bin/python3
"""retrieve employee ID"""

import requests


def main(arg):
    """request todos and retrieve data"""
    __url = requests.get(
             'https://jsonplaceholder.typicode.com/todos/?userId={id}'.format(
                                 id=arg)).json()
    __url_2 = requests.get(
                  'https://jsonplaceholder.typicode.com/users/{id}'.format(
                                  id=arg)).json()
    n_done = 0
    n_task = len(__url)
    for i in range(len(__url)):
        if __url[i]['completed'] is True:
            n_done += 1
    pron = "Employee {e_name} is done with tasks({n_done}/{n_task}):"
    print(pron.format(e_name=__url_2['name'], n_done=n_done, n_task=n_task))
    for i in range(len(__url)):
        if __url[i]['completed'] is True:
            print("\t {}".format(__url[i]['title']))


if __name__ == "__main__":
    from sys import argv
    main(argv[1])
