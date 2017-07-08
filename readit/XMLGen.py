from lxml import etree

prompt = "~"


def ask_keyword():
    print("Please subreddit_input a keyword you'd like to monitor.")
    print("If you are done just press enter.")
    keyword_name = input(prompt)
    if keyword_name is '':
        return None
    else:
        return etree.Element('keyword', name=keyword_name)


def ask_subreddit():
    print("Please subreddit_input subreddit you'd like to add.")
    print("If you are done adding subreddits just press enter.")
    subreddit_name = input(prompt)
    if subreddit_name is '':
        return None
    else:
        subreddit_xml = etree.Element('subreddit', name=subreddit_name)
        keyword = ask_keyword()
        while keyword is not None:
            subreddit_xml.append(keyword)
            keyword = ask_keyword()
        return subreddit_xml


def generate_xml():
    data = etree.Element('data')
    #Adds Subreddits:
    subreddits = etree.Element('subreddits')
    subreddit_input = ask_subreddit()
    while subreddit_input is not None:
        subreddits.append(subreddit_input)
        subreddit_input = ask_subreddit()
    data.append(subreddits)
    #Put more sources here
    return data


if __name__ == '__main__':
    print(etree.tostring(generate_xml(), pretty_print=True))