def check_contents(post):
    return False


def check_title(post):
    return False


def check_source(post):
    return False


def check_id(post, last_reddit_post_id):
    if int(post.id, 36) > last_reddit_post_id:
        return True


def check_post(post, last_reddit_post_id):
    return (check_contents(post) or
            check_title(post) or check_source(post) or check_id(post, last_reddit_post_id))
