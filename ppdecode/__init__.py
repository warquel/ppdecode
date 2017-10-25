#!/usr/bin/env python
"""Parser for Proofpoint URLDefense encoded URLs. Now importable and python 2/3 compatible."""

import argparse
import json
import re
import sys
if sys.version_info[0] < 3:
    from urlparse import parse_qs, unquote, urlparse
    import string
else:
    from urllib.parse import parse_qs, unquote, urlparse

valid_versions = ['v1', 'v2']


def find_version(url):
    """Detect the version of the Proofpoint URL."""
    match = re.search(r'https://urldefense.proofpoint.com/(?P<version>v[0-9])/', url)

    return match.group('version')


def ppdecode(url, return_all=False):
    """Parse the query and extract the decoded URL."""
    try:
        version = find_version(url)
    except AttributeError:
        raise RuntimeError('This does not appear to be a valid proofpoint url: {}'.format(url))
    else:
        if version not in valid_versions:
            raise RuntimeError('Ppdecode is unprepared to handle this version of proofpoint urls: {}'.format(url))
    parsed_url = urlparse(url)
    query_components = parse_qs(parsed_url.query)
    if sys.version_info[0] < 3:
        translated_url = query_components['u'][0].translate(string.maketrans('-_', '%/'))
    else:
        translated_url = query_components['u'][0].translate(str.maketrans('-_', '%/'))
    decoded_url = unquote(translated_url)
    query_components['decoded_url'] = decoded_url
    query_components['proofpoint_version'] = version

    return query_components


def main():
    """Run main function."""
    parser = argparse.ArgumentParser(description='Decode Proofpoint URLDefense encoded URL.')
    parser.add_argument('url', metavar='URL', help='Proofpoint encoded URL.')
    parser.add_argument('-j', '--json', help='Output JSON rather than text.', action='store_true')
    parser.add_argument('-a', '--all', help='Print all Proofpoint parameters.', action='store_true')
    parser.add_argument('-v', '--version', action='version', version='Version 1.0.0')
    args, _ = parser.parse_known_args()

    try:
        results = ppdecode(args.url)
    except RuntimeError as e:
        sys.exit(e)

    if not args.all:
        results = {'decoded_url': results['decoded_url']}
    if args.json:
        print(json.dumps(results, sort_keys=True, indent=4))
    else:
        for key, value in results.items():
            print('{} : {}'.format(key, value))

if __name__ == '__main__':
    main()
