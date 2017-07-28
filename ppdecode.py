#!/usr/bin/env python

"""Usage:
    ppdecode.py [-aj] <proofpoint_url>
    ppdecode.py (-h | --help)
    ppdecode.py --version

Options:
    -h --help   Show this screen
    -a          Print all proofpoint parameters
    -j          Output results in json
    --version   
"""

version="0.2"

import urllib, urlparse, re, docopt, sys, string, json

def find_version(url):
    match = re.search(r'https://urldefense.proofpoint.com/(v[0-9])/', url)
    if match:
        return match.group(1)
    else:
        return None

def parse(url):
    parsed = urlparse.parse_qs(urlparse.urlparse(url)[4])
    parsed['decoded_url'] = urllib.unquote(parsed['u'][0].translate(string.maketrans("-_", '%/')))
    return parsed

def output(params, all=True, type="text"):
    res = params
    if all == False:
        res = {'decoded_url': params['decoded_url']}
    if type == "text":
        for k,v in res.iteritems():
            print "%s : %s" % (k,v)
    else:
        print json.dumps(res,sort_keys=True,indent=4)
            

def main():
    args = docopt.docopt(__doc__, version="ppdecode "+version)
    u = args['<proofpoint_url>']
    type = 'json' if args['-j'] else 'text'
    ver = find_version(u)
    if ver is None:
        sys.stderr.write("This does not appear to be a valid proofpoint url:\n\n%s\n\n" % u + __doc__)
        exit()
    else:
        if ver in ("v1","v2"):
            results = parse(u)
            results["version"] = ver
            output(results,args['-a'],type)
        else:
            sys.stderr.write("This script is unprepared to handle this version of proofpoint urls:\n\n%s\n\n" % u + __doc__)
            exit()


if __name__ == "__main__":
    main()
