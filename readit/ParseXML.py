from lxml import etree


def parse_xml_by_field(field):
    fields = []
    tree = etree.parse('config.xml')
    values = tree.xpath('//' + field)
    for element in values:
        fields.append(element.get("name"))
    return fields


def get_subreddits():
    return parse_xml_by_field("subreddit")

if __name__ == '__main__':
    print(parse_xml_by_field("subreddit"))
