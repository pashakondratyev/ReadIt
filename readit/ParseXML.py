import xml.etree.ElementTree

def parsexml(Field):
    values = []
    parsed = xml.etree.ElementTree.parse('../tests/config.xml').getroot()
    for fieldvalues in parsed.findall(Field):
        print(fieldvalues)

if __name__ == '__main__':
    parsexml("subreddits")