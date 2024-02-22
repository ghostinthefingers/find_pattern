from pwn import *
import sys
import logging

if len(sys.argv) < 3:
    logging.error('usage: python3 pattern.py <address> <n>')
    exit()

address = sys.argv[1]
n = int(sys.argv[2])

p = cyclic(20000, n=n)

if '0x' in address:
    address = address[2:]
    my_string = bytes.fromhex(address).decode('utf-8')
    my_string = my_string[::-1]
    print(f'padding is : {p.index(my_string.encode())}')
