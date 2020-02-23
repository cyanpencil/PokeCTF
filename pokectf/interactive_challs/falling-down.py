#!/usr/bin/python2
from __future__ import print_function
import signal, random, collections, sys

old_print = print
def print(*args, **kw):
    old_print(*args, **kw)
    sys.stdout.flush()

def solve(N, K):
    diff = collections.deque()
    for _ in range(K + 1):
        diff.append(0)
    cur = 0
    diff[0] = 1
    diff[-1] = -1
    for i in range(N):
        tmp = diff.popleft()
        cur += tmp
        diff.append(-cur)
        diff[0] += cur
    return cur

print("Hello there!")
N = random.randrange(8*10**4, 2*10**5)
K = random.randrange(3, 11)
answer = solve(N, K)
print("In how many ways can you get to the top of a staircase with %d stairs if you can take up to %d steps every time? (e.g. (4, 2) -> 5)\nYou have 4 seconds!" % (N, K))
signal.alarm(4)
t = raw_input().strip()
if t == str(answer):
    print("poke{Don't_f4ll_Down_tHOse_stairs}")
else:
    print("NOPE")

