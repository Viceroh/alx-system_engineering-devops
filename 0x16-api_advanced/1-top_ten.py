#!/usr/bin/python3
"""Top Ten"""
import requests


def top_ten(subreddit):
    """
    get top 10 post title
    args:
        subreddit: the reddit name
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url)
    if (response.status_code != 200):
        print(None)
    data = response.json()["data"]["children"]
    for child in data[:10]:
        print(child["data"]["title"])
