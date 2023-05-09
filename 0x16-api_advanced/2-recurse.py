#!/usr/bin/python3
"""recursive functions"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """return list of containing titles of host articles"""
    URL = "https://www.reddit.com/r/{}/hot/.json?after={}?count={}?limit=100"
    URL = URL.format(subreddit, after, count)
    headers = {"User-Agent": "My User Agent 1.0"}
    response = requests.get(URL, headers=headers)

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
