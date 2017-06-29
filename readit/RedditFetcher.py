import calendar
import time

import requests


def get_page(url):
    # Having the User-Agent in the request prevents an overload
    page = requests.get(url, headers={'User-Agent': 'readitBot'})
    return str(page.text)


def get_new_posts(subreddit):
    url = "http://www.reddit.com/r/" + subreddit + "/new.json"
    return get_page(url)


def get_new_posts_multi(subreddit_array):
    return_array = []
    for item in subreddit_array:
        return_array.append(get_new_posts(str(item)))
    return return_array


if __name__ == '__main__':
    print("Main")
    print(calendar.timegm(time.gmtime()))
    #get_subreddits()
