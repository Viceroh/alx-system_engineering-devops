#!/usr/bin/python3
"""
2-recurse
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """recursive"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])

        if children:
            for child in children:
                title = child.get('data', {}).get('title')
                hot_list.append(title)

            after = data.get('after')
            if after:
                recurse(subreddit, hot_list, after)

            return hot_list
        else:
            return None
    else:
        return None
