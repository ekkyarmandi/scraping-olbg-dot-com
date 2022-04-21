import argparse
import scraper
import json

from pprint import pprint


# load the parser
parser = argparse.ArgumentParser(description='OLBG.com scraping script')

# sub parser
parser.add_argument(
    'command',
    choices=['collect'],
    help='main commands'
)

parser.add_argument(
    '-u', '--url',
    help='source url'
)

parser.add_argument(
    '-o', '--output',
    default=None,
    help='output destination'
)

args = parser.parse_args()

if args.command == 'collect':
    result = scraper.parser(args.url)
    pprint(result,sort_dicts=False)

    if args.output != None:
        json.dump(
            result,
            open(args.output,'w',encoding='utf-8'),
            indent=4
        )