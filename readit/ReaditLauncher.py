import calendar
import time

import readit.NotificationDrivers as NotificationDrivers
import readit.ParseXML as ParseXML
import readit.RedditFetcher as RedditFetcher
import readit.RedditPost as RedditPost
import readit.RedditProcessor as RedditProcessor


def report(post):
    print("Alert! There has been a new post of interest")
    print(post.created_utc)
    print(post.title)
    NotificationDrivers.new_pushover_message(post.title)


def process(reddit_result, time_after):
    for subreddit in reddit_result:
        data = RedditPost.group_of_posts(subreddit)
        for post in data:
            if RedditProcessor.check_post(post, time_after, id):
                report(post)
            else:
                break


def long_poll():
    time_after = calendar.timegm(time.gmtime())
    subreddits = ParseXML.get_subreddits()
    while True:
        result = RedditFetcher.get_new_posts_multi(subreddits)
        _temp = calendar.timegm(time.gmtime())
        process(result, time_after)
        time_after = _temp
        time.sleep(.5)  # Sleeps .5 seconds between polls


if __name__ == '__main__':
    print("Readit is now running!")
    long_poll()