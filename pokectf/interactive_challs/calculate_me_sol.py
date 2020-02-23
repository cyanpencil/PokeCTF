#!/usb/bin/env python

import string
import math
from bisect import bisect_right
from pwn import *

sh = remote("www.cyanpencil.xyz",5002)

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]


print(sh.recvuntil("..."))
print(sh.recvline())
while True:
    l = sh.recvline()
    print(l)
    ints = map(int, re.findall(r'\d+', l))
    if len(ints) == 0: continue
    if '+' in l: sh.sendline(str(ints[0] + ints[1]))
    if '-' in l: sh.sendline(str(ints[0] - ints[1]))
    if '*' in l: sh.sendline(str(ints[0] * ints[1]))
    if "square" in l: sh.sendline(str(math.ceil(math.sqrt(ints[0]))))
    if "prime" in l: sh.sendline(str(primes(12000)[bisect_right(primes(12000), ints[0])]))


