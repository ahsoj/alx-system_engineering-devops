#!/usr/bin/python3
"""return titles of top ten posts"""
import requests


def top_ten(subreddit):
    """return title of top_ten posts or None"""
    URL = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(URL, headers=headers)
    if response.status_code == 200:
        response = response.json()
        children = response['data']['children']
        for i in range(len(children) or 10):
            print(children[i]['data'].get('title'))
    else:
        print(None)
