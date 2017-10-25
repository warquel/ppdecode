# ppdecode
Proofpoint URL Decoder

## Installation

```
pip install git+https://github.com/warquel/ppdecode.git
```

Just a quick and simple proofpoint Follow Me URL rewrite decoder.

```
Usage: ppdecode [-h] [-j] [-a] [-v] URL

Decode Proofpoint URLDefense encoded URL.

positional arguments:
  URL            Proofpoint encoded URL.

optional arguments:
  -h, --help     show this help message and exit
  -j, --json     Output JSON rather than text.
  -a, --all      Print all Proofpoint parameters.
  -v, --version  show program's version number and exit
```

The ppdecode function is also importable into other code:

```
import ppdecode

results = ppdecode.ppdecode(url)
```
