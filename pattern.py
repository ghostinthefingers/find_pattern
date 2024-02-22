from pwn import *
import sys
import logging

if len(sys.argv) < 2:
    logging.error('usage: python3 pattern.py 0xdeadbeef [n=8]')
    exit()

address = sys.argv[1]
n = int(sys.argv[2]) if len(sys.argv) > 2 else 8  # Default to n=8 if not provided

p = cyclic(20000, n=n)

if '0x' in address:
    address = address[2:]
    my_string = bytes.fromhex(address).decode('utf-8')
    my_string = my_string[::-1]
    print(f'padding is : {p.index(my_string.encode())}')
