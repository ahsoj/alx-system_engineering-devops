#!/usr/bin/python3
"""retrieve employee ID"""

import request


if __name__ == "__main__":
    import sys
    _id = sys.argv[1]
    __url = requests.get(
             'https://jsonplaceholder.typicode.com/todos/?userId={id}'.format(
                                 id=_id)).json()
    __url_2 = requests.get(
                  'https://jsonplaceholder.typicode.com/users/{id}'.format(
                                  id=_id)).json()
    n_done = 0
    n_task = len(__url)
    for i in range(len(__url)):
        if __url[i]['completed'] is True:
            n_done += 1
    pron = "Employee {e_name} is done with tasks({n_done}/{n_task}):"
    print(pron.format(e_name=__url_2['name'], n_done=n_done, n_task=n_task))
    for i in range(len(__url)):
        print("\t {}".format(__url[i]['title']))
