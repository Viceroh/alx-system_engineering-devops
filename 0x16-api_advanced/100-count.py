#!/usr/bin/python3
"""
3. Count it!
"""
import requests


def count_words(subreddit, word_list, after=None, count_dict={}):
    """Recursively counts occurrences of words in hot articles titles"""
    if after is None:
        url = 'https://api.reddit.com/r/{}/hot'.format(subreddit)
    else:
        url = 'https://api.reddit.com/r/{}/hot?after={}'.format(
            subreddit, after)

    response = requests.get(url, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get('data', {})
    children = data.get('children', [])
    for child in children:
        title = child.get('data', {}).get('title', '').lower()
        for word in word_list:
            if word.lower() in title.split():
                count_dict[word.lower()] = count_dict.get(word.lower(), 0) + 1

    after = data.get('after')
    if after:
        return count_words(subreddit, word_list, after, count_dict)
    else:
        sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))
