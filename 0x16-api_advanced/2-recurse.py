#!/usr/bin/python3
"""recursive functions"""
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """return list of containing titles of host articles"""
    URL = "https://www.reddit.com/r/{}/hot/.json?limit=100"
    URL = URL.format(subreddit)
    headers = {"User-Agent": "My User Agent 1.0"}
    params = {'after': after, 'count': count}
    response = requests.get(URL, headers=headers, params=params)

    if response.status_code == 200:
        response = response.json()
        after = response['data'].get('after')
        count += response['data'].get('dist')
        for child in response['data']['children']:
            hot_list.append(child['data'].get('title'))
        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        return hot_list
    else:
        return None
