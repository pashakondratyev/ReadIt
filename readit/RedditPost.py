import json


class RedditPost:

    # Takes the reddit post as JSON, and parses relevant information
    def __init__(self, post):
        data = post["data"]
        self.created_utc = data["created_utc"]
        self.title = data["title"]
        self.subreddit = data["subreddit"]
        self.likes = data["likes"]
        self.author = data["author"]
        self.permalink = data["permalink"]
        self.url = data["url"]
        self.id = data["id"]
        self.selftext = data["selftext"]
        self.score = data["score"]


# Takes JSON file of reddit posts and returns a list of post objects
def group_of_posts(json_posts):
    posts = []
    data = json.loads(json_posts)
    for post in data["data"]["children"]:
        posts.append(RedditPost(post))
    return posts
