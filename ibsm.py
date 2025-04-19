#!/usr/bin/env python3

from itertools import zip_longest
from sys import argv, stderr
from base64 import b64decode as de, b64encode as en


DEBUG = False

def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, file=stderr, **kwargs)

save_key = ["level", "money", "gold", "gold at next reset"]

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
    def x(s:str, i=1_000_000_000):
      return str(float(s)*i)
    sp[0] = "420"
    sp[1] = x(sp[1], 1_000)
    sp[2] = x(sp[2], 1_000_000_000_1_000_000_000)
    sp[-5] = x(sp[-5]) # this is skill points
    for key, value in zip_longest(save_key, sp):
        print(f"{key or "???"}: {float(value) if value != '' else 0:,}")
        print(f"{key or "???"}: {float(value) if value != '' else 0:,}", file=open("save_code_expanded.tmp.txt", "a"))
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