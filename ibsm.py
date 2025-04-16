from sys import argv
from base64 import b64decode as de, b64encode as en
def main(save_code: str):
    print(save_code)
    with open('save_code.tmp.txt', 'w') as f:
        f.write(save_code)
    d = de(save_code)
    with open('save_code_d.tmp.txt', 'wb') as f:
        f.write(d)
    d = d.decode()
    print(d)
    sp = d.split(',')
    print(sp)
    joined = ','.join(sp)
    e = joined.encode()
    e = en(e)
    print(e.decode()==save_code)
    with open('save_code_e.tmp.txt', 'wb') as f:
        f.write(e)

if __name__ == "__main__":
    # Entry point for the script
    main(argv[1])