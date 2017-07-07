from lxml import etree


def parse_xml_by_field(field):
    fields = []
    tree = etree.parse('config.xml')
    values = tree.xpath('//' + field)
    for element in values:
        fields.append(element.get("name"))
    return fields


def parse_xml_by_fields(field1, field2):
    fields = []
    tree = etree.parse('config.xml')
    values = tree.xpath('//subreddit[@name=\'rangers\']/keyword')
    print(values)
    for element in values:
        fields.append(element.get("name"))
    return fields


def get_subreddits():
    return parse_xml_by_field("subreddit")


def get_subreddit_keywords(subreddit):
    return parse_xml_by_fields(subreddit, "keyword")

if __name__ == '__main__':
    print(parse_xml_by_field("subreddit"))
    print(get_subreddit_keywords("rangers"))
