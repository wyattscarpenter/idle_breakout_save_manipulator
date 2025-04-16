#!/usr/bin/env python3

from sys import argv, stderr
from base64 import b64decode as de, b64encode as en


DEBUG = False

def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, file=stderr, **kwargs)

def main(save_code: str):
    print()
    dprint(save_code)
    with open('save_code.tmp.txt', 'w') as f:
        f.write(save_code)
    d = de(save_code)
    with open('save_code_d.tmp.txt', 'wb') as f:
        f.write(d)
    d = d.decode()
    dprint(d)
    sp = d.split(',')
    dprint(sp)
    sp[0] = "420"
    joined = ','.join(sp)
    e = joined.encode()
    e = en(e).decode()
    dprint(e==save_code)
    print(e)
    with open('save_code_e.tmp.txt', 'w') as f:
        f.write(e)

if __name__ == "__main__":
    # Entry point for the script
    main(argv[1])