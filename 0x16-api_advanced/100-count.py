#!/usr/bin/python3
"""recursive function that quries the REDDIT API"""
import requests


def count_words(subreddit, word_list, instances={}, after=None, count=0):
    """
    parse the title of all hot articles\
    and print a sorted count of given keywords
    """
    URL = "http://www.reddit.com/r/{}/hot.json?limit=100"
    URL = URL.format(subreddit)
    headers = {"User-Agent": "My User Agent 1.0"}
    params = {'after': after, 'count': count}
    response = requests.get(URL, headers=headers, params=params)

    if response.status_code == 200:
        response = response.json()['data']
        after = response.get('after')
        count += response.get('dist')
        for child in response.get('children'):
            title = child['data'].get('title').lower().split()
            for word in word_list:
                if word.lower() in title:
                    times = len([t for t in title if t == word.lower()])
                    if instances.get(word) is None:
                        instances[word] = times
                    else:
                        instances[word] += times
        if after is None:
            if len(instances) == 0:
                return
            instances = sorted(
                    instances.items(), key=lambda kv: (-kv[1], kv[0]))
            [print("{}: {}".format(k, v)) for k, v in instances]
        else:
            count_words(subreddit, word_list, instances, after, count)
