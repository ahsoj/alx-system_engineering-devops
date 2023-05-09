#!/use/bin/python3
"""return number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """"return number of subscribers or None"""
    URL = "https://www.reddit.com/r/{}/about/.json".format(subreddit)
    response = requests.get(URL)
    if response.status_code == 200:
        response = response.json()
        return (response['data']['subscribers'])
    return 0
