import requests


def get_page(url):
    page = requests.get(url)
    return str(page.text)


def get_new_five_posts(subreddit):
    url = "http://www.reddit.com/r/" + subreddit + "/new.json?count=5"
    print(get_page(url))


if __name__ == '__main__':
    print("Main")
    get_new_five_posts("rangers")
