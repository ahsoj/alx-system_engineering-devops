#!/usr/bin/python3
"""retrieve employee ID and save to csv file"""

import requests
import csv


def main(arg):
    """request todos and retrieve data"""
    __url = requests.get(
             'https://jsonplaceholder.typicode.com/todos/?userId={id}'.format(
                                 id=arg)).json()
    __url_2 = requests.get(
                  'https://jsonplaceholder.typicode.com/users/{id}'.format(
                                  id=arg)).json()

    with open("{}.csv".format(arg), 'w', newline="") as csvFile:
        output = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        for i in range(len(__url)):
            __ = __url[i]
            output.writerow(
                     [__['userId'],
                      __url_2['name'],
                      __['completed'],
                      __['title']])


if __name__ == "__main__":
    from sys import argv
    main(argv[1])
