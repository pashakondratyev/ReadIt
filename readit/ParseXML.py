from lxml import etree


def parse_xml_by_field(Field):
    fields = []
    tree = etree.parse('config.xml')
    values = tree.xpath('//' + Field)
    for element in values:
        fields.append(element.get("name"))
    return fields

if __name__ == '__main__':
    print(parse_xml_by_field("subreddit"))
