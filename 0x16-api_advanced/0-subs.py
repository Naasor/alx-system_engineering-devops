#!/usr/bin/python3
"""A module that contains number_of_subscribers's function"""

import requests


def number_of_subscribers(subreddit):
    """A function that queries the Reddit API and returns the number of
    subscribers for a given subreddit.

    return: 0, If an invalid subreddit is given.
    """

    user_agent = 'MyRedditApp/1.0 by /u/Dredouane'

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': user_agent}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return 0

    json = r.json()

    # check if it is a subreddit.
    kind = json.get("kind")
    if kind != "t5":
        return 0

    # getting the data.
    data = json.get("data")

    number_of_subscribers = data.get("subscribers")
    return (number_of_subscribers)
