#!/usr/bin/env python

# Make sure you have pysha3 installed
# pip install -U pysha3

import sha3, hashlib, sys

HASH_FUNCS = {
    'SHA-256': lambda x: hashlib.sha256(x).hexdigest(),
    'KECCAK-256': lambda x: sha3.keccak_256(x).hexdigest(),
}

def get_hashes(msg):
    for h in ['SHA-256', 'KECCAK-256']:
        out = '%s:%s' % (h, HASH_FUNCS[h](msg))
        print(out)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception('Usage: %s <msg>' % sys.argv[0])
    get_hashes('VISC:%s' % sys.argv[1]);
