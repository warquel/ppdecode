# ppdecode
Proofpoint URL Decoder

Just a quick and dirty proofpoint Follow Me URL rewrite decoder.

import ppdecode
url = <proofpoint url>
p = ppdecode.ppdecode(url)
print p.url
