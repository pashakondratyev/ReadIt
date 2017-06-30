import time

import readit.NotificationDrivers as NotificationDrivers
import readit.ParseXML as ParseXML
import readit.RedditFetcher as RedditFetcher
import readit.RedditPost as RedditPost
import readit.RedditProcessor as RedditProcessor


def process(subreddits, last_reddit_post_id):
    reddit_result = RedditFetcher.get_new_posts_multi(subreddits)
    for subreddit in reddit_result:
        data = RedditPost.group_of_posts(subreddit)
        for post in data:
            if int(post.id, 36) > last_reddit_post_id:
                last_reddit_post_id = int(post.id, 36)
            if RedditProcessor.check_post(post, last_reddit_post_id):
                report(post)
            else:
                break
    return last_reddit_post_id


def report(post):
    print("Alert! There has been a new post of interest")
    print(post.created_utc)
    print(post.title)
    NotificationDrivers.new_pushover_message(post.title)


def long_poll():
    subreddits = ParseXML.get_subreddits()
    last_reddit_post_id = process(subreddits, 0)
    while True:
        process(subreddits, last_reddit_post_id)
        time.sleep(.5)  # Sleeps .5 seconds between polls


if __name__ == '__main__':
    print("Readit is now running!")
    long_poll()