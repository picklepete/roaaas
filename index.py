#!/usr/bin/env python3

import json
import requests
from bs4 import BeautifulSoup
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-f', '--file', default='rules.json', dest='filename', help='Write index to file.', metavar='FILE')
(options, args) = parser.parse_args()

MEMORY_BETA_URL = 'https://memory-beta.fandom.com'
PAGE_URL = MEMORY_BETA_URL + '/wiki/Ferengi_Rules_of_Acquisition'


def index():
    """
    Responsible for reading the Memory Beta wiki entry for the
    rules of acquisition, iterating over the rules in their table,
    and writing them to a JSON file.
    """
    # Fetch the page containing the rules.
    response = requests.get(PAGE_URL, headers={'User-Agent': 'roa-api/v0.1'})
    if response.status_code != requests.codes.OK:
        raise RuntimeError('The page URL raised an invalid response code')

    # Our cache where we will store the rules.
    cache = {}

    # Parse the page content.
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table, iterate over the rows (ignoring the first, a header).
    table = soup.find('table', {'class': 'chart'})
    for row in table.findAll('tr')[1:]:
        id_column, rule_column, source_column = row.findAll('td')
        rule_id = str(id_column.text.strip())
        if source_column.find('a'):
            source = source_column.find('a')['href']
            if source.startswith('/'):
                source = MEMORY_BETA_URL + source
        else:
            source = source_column.text.strip()
        cache[rule_id] = {
            'source': source,
            'rule': rule_column.text.strip()
        }

    # Write the cache to the specified filename.
    with open(options.filename, 'w') as fs:
        fs.write(json.dumps(cache, indent=4))


if __name__ == '__main__':
    index()
