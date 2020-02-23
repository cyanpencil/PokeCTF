#!/usb/bin/env python

import random
import time
import math
import sys
from bisect import bisect_right

def myprint(string):
    print(string, flush=True)

def read_timeout():
    import sys, select
    i, o, e = select.select( [sys.stdin], [], [], 5 )
    if (i):
        return float(sys.stdin.readline().strip())
    return -1

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def chall_plus():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    myprint(str(a) + " + " + str(b) + " = ?")
    c = int(read_timeout())
    if c == a + b: return True
    myprint("WRONG!")
    exit()

def chall_minus():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    myprint(str(a) + " - " + str(b) + " = ?")
    c = int(read_timeout())
    if c == a - b: return True
    myprint("WRONG!")
    exit()

def chall_times():
    a = random.randint(1, 30)
    b = random.randint(1, 30)
    myprint(str(a) + " * " + str(b) + " = ?")
    c = int(read_timeout())
    if c == a * b: return True
    myprint("WRONG!")
    exit()

def chall_sqrt():
    a = random.randint(1, 1024)
    myprint("What is the square root of " + str(a) + "? (rounded up to an integer)")
    c = int(read_timeout())
    if c == math.ceil(math.sqrt(a)) : return True
    myprint("WRONG!")
    exit()

def chall_prime(i):
    a = random.randint(i**2, 10+int(i**3.5))
    myprint("What is the smallest prime higher than " + str(a) + " ?")
    c = int(read_timeout())
    min_val = prime_list[bisect_right(prime_list, a)]
    if c == min_val : return True
    myprint("WRONG!")
    exit()

challs = {0:chall_plus, 1:chall_minus, 2:chall_times, 3:chall_sqrt, 4:chall_prime}
prime_list = primes(15000)

myprint("Welcome to the SOAC, Swiss Olympiads in Abacus Counting . \nYou have five seconds to answer each question. \nGet ready, warm your fingers...")
time.sleep(2)



for i in range(6):
    c = random.randint(0, 1)
    challs[c]()

myprint("Congratulations, you passed the local selection. \nBut now only _real_ abacus lovers will be able to handle the difficulty.\nRemember, only five seconds for each question! Good luck!")
time.sleep(2)

for i in range(10):
    c = random.randint(0, 3)
    challs[c]()

myprint("Wow! You are among the best in swtitzerland.\nYou are selected to represent your nation in the world!\nBut, let me warn you - world finals require an arcane mastery of the abacus rarely seen among humans.")
time.sleep(2)
myprint("Are you ready?\nYou have only FIVE seconds for each question! Let's go!")
time.sleep(2)

for i in range(10):
    c = 4
    challs[c](i)

myprint("Amazing! poke{Y0u_are_7h3_w0rld_champion!}")
