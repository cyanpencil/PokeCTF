#!/usr/bin/env python3
import traceback, os, sys

DEBUG = "FLAG" not in os.environ

del sys.modules["os"]

def run():
    g = {"__builtins__": {}}
    for b in ["abs", "all", "any", "chr", "dict", "dir", "divmod", "enumerate", "eval", "filter", "float", "format", "frozenset", "getattr", "hasattr", "hash", "int", "iter", "len", "list", "map", "max", "min", "ord", "pow", "range", "round", "str", "sum", "tuple", "zip"]:
        g["__builtins__"][b] = __builtins__[b]
    if DEBUG:
        g["__builtins__"]["print"] = print
    while True:
        try:
            x = input(">>> ")
        except EOFError:
            break
        seen = set()
        r = ""
        for c in x:
            if c in seen: continue
            r += c
            seen.add(c)
        try:
            exec(r, g)
        except:
            print(traceback.format_exc())
    print("Quitting\nThank you, come again!")

if __name__ == "__main__":
    run()
