#!/usr/bin/env python3
import random, string, hashlib, base64
import fastecdsa.curve, fastecdsa.point
import shell

CHALLENGE_LENGTH = 20

CURVE = fastecdsa.curve.secp256k1
PRIVKEY = None
PUBKEY = None

def read_key():
    global PRIVKEY, PUBKEY
    with open("key") as f:
        p, x, y = map(int, map(str.strip, f.readlines()))
    PRIVKEY = p
    PUBKEY = fastecdsa.point.Point(x, y, curve=CURVE)

def encode(x):
    h = hex(x)[2:]
    if len(h) & 1:
        h = "0" + h
    return base64.b64encode(bytes.fromhex(h)).decode("utf-8")

def decode(x):
    return int(bytes.hex(base64.b64decode(x.encode("utf-8"))), 16)

def sign(msg):
    k = random.randrange(CURVE.q)
    t = CURVE.G * k
    c = int(hashlib.sha512(msg.encode("utf-8")).hexdigest(), 16)
    s = k + (PRIVKEY * c)
    return "{}.{}.{}".format(encode(t.x), encode(t.y), encode(s))

def validate_signature(msg, s):
    try:
        s = s.split(".")
        if len(s) != 3:
            return False
        x, y, s = map(decode, s)
    except:
        return False

    c = int(hashlib.sha512(msg.encode("utf-8")).hexdigest(), 16)
    t = fastecdsa.point.Point(x, y, curve=CURVE)
    return (CURVE.G * s) == (t + (PUBKEY * c))

def generate_challenge():
    return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(CHALLENGE_LENGTH))

def main():
    read_key()
    print("Welcome to the management server, as a reference, here is our public key:")
    print(PUBKEY)
    print()

    while True:
        try:
            m = input("""What do you want to do?
1. Sign a message
2. Get a shell
3. Quit
> """)
        except:
            print("Goodbye!")
            break
        if m.strip() == "1":
            m = input("What message would you like to sign?\n> ")
            if m.strip() == "Hello, world!":
                print("Thank you, here is your signature:")
                print(sign(m))
            else:
                print("I'm sorry, I can't endorse that statement")
        elif m.strip() == "2":
            r = generate_challenge()
            print("Please sign the following message to get access (without quotes): %r" % r)
            s = input("> ")
            if validate_signature(r, s):
                shell.run()
                break
            else:
                print("WRONG!")
        elif m.strip() == "3":
            print("Goodbye")
            break
        else:
            print("What are you saying, exactly?")

if __name__ == "__main__":
    main()
