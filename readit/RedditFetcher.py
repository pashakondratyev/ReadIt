import requests

import readit.ParseXML as px


def get_page(url):
    # Having the User-Agent in the request prevents an overload
    page = requests.get(url, headers={'User-Agent': 'readitBot'})
    return str(page.text)


def get_new_five_posts(subreddit):
    url = "http://www.reddit.com/r/" + subreddit + "/new.json?count=5"
    print(get_page(url))


def get_subreddits():
    subreddits = px.parse_xml_by_field("subreddit")
    for item in subreddits:
        get_new_five_posts(str(item))


if __name__ == '__main__':
    print("Main")
    get_subreddits()
