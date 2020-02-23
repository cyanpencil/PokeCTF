from ascii_ctf import *

db.create_all()

def declare_chal(data):
    chal = Challenges.query.filter_by(name=data["name"]).first()
    if chal is not None:
        for n in data:
            if n == "name": continue
            setattr(chal, n, data[n])
    else:
        data["solves"] = "0"
        db.session.add(Challenges(**data))
    db.session.commit()

declare_chal({ "name": "Your first pwn",
    "category": "pwn",
    "score": 50,
    "info": """

Warm-up challenge!

Data: <a href="/static/pwn1">pwn1</a>
Source: <a href="/static/pwn1.c">pwn1.c</a>

nc www.cyanpencil.xyz 5006

""",
"flag": 'poke{w3ll..g0Od_j0b_I_gu35s}'
})

declare_chal({ "name": "Simple crackme",
    "category": "reverse",
    "score": 100,
    "info": """
Data: <a href="/static/reverse1">reverse1</a>

You shouldn't have trouble with this one...
""",
    "flag": 'poke{G0od_you_can_get_started_now}'
})

declare_chal({ "name": "RS-yAy!",
    "category": "crypto",
    "score": 100,
    "info": """

Pay attention - state of the art cryptography lies ahead.

You have been warned, you are only wasting your time here.

Data: <a href="/static/RS-yAy.zip">smells_funny.zip</a>

""",
"flag": 'poke{WHO_s4ys_maTh_has2b_H4rD?}'
})


declare_chal({ "name": "Flasky",
    "category": "web",
    "score": 100,
    "info": """

Well, this webservice has a python backend - no exploits available for you here, sorry.

I can give you the source code too, I'm really confident you cannot do anything about it.

(the flag is in /home/poke/flag, go catch it!)

Website: <a href="http://www.cyanpencil.xyz:5005/hello-template-injection?name=idiot">here</a>
Source code: <a href="/static/web2/flask_vuln.py">here</a>

""",
"flag": 'poke{3V3n_pYth0n_c4n_b_vuLn}'
})



declare_chal({ "name": "Dungeon",
    "category": "misc",
    "score": 100,
    "info": """

To get the flag, explore the upper floor of the house without dying...

nc www.cyanpencil.xyz 5003

""",
"flag": 'poke{1nt3r4ct1v3_f1cti0n_is_w4y_und3rr4t3d}'
})



declare_chal({ "name": "Acrobat abacus",
    "category": "misc",
    "score": 150,
    "info": """
Well, I hope you are quick with your hands...

nc www.cyanpencil.xyz 5002

""",
    "flag": 'poke{Y0u_are_7h3_w0rld_champion!}'
})



declare_chal({ "name": "A GIFt for you",
    "category": "stegano",
    "score": 150,
    "info": """

I heard you like GIFs.

I made a special one for you.


<a href="/static/stego1.gif">Here you go</a>

""",
"flag": 'poke{sp3eD_0f_soUnd!}'
})


declare_chal({ "name": "Falling down",
    "category": "misc",
    "score": 200,
    "info": """

This time your abacus won't save you...
Try to avoid calculating the same stuff all over again, please...

nc cyanpencil.xyz 5008

""",
"flag": 'poke{Don\'t_f4ll_Down_tHOse_stairs}'
})



declare_chal({ "name": "No, crack-me!",
    "category": "reverse",
    "score": 200,
    "info": """
Data: <a href="/static/reverse2">reverse2</a>

This flag-printing binary I just made is a bit slow.
I wonder if you can optimize my code a bit?

""",
    "flag": 'poke{Th4t_w4s_n0t.hard_I-h0pe}'
})


declare_chal({ "name": "Boring string",
    "category": "pwn",
    "score": 200,
    "info": """

I set up this printer service last week.
Do not forget to specify the format!

Data: <a href="/static/pwn2">pwn2</a>

nc www.cyanpencil.xyz 5001

""",
"flag": 'poke{I_h0p3_u_l1k3_str1ngs_:)}'
})


declare_chal({ "name": "League",
    "category": "pwn",
    "score": 300,
    "info": """

You are up against the very Pokemon League!
Choose wisely your pokemons ;)

Data: <a href="/static/league">league</a>

nc www.cyanpencil.xyz 5009

""",
"flag": 'poke{UR_p0k3mOn_cH4mp_c0ngRaT5!!1}'
})


declare_chal({ "name": "Dropbox",
    "category": "web + crypto",
    "score": 300,
    "info": """

I downloaded from github this cool file sharing app.

It also follows links! Since it is open source, for sure it is backdoor-free.

Website: <a href="http://www.cyanpencil.xyz:5004">here</a>
Source code: <a href="/static/web1/server.js">server.js</a>, <a href="/static/web1/package.json">package.json</a>


""",
"flag": 'poke{Wha7_1s_7his_CO0ki3_4boUt}'
})


# declare_chal({ "name": "Signage",
    # "category": "crypto",
    # "score": 300,
    # "info": """

# I thought I was smart when I made this administrative system. 
# Now I lost my access and my private key, and the only thing 
# I was able to recover was this compiled file.
# Can you help me?

# nc cyanpencil.xyz 5007


# Source code: <a href="/static/crypto1/entry.py">entry.py</a>

# """,
# "flag": 'poke{CrYpTo_4nd_sn3ks?U_M4D_br0!}'
# })



# declare_chal({ "name": "Curvaceous",
    # "category": "reverse",
    # "score": 300,
    # "info": """

# Listen, why don't you go watch some pokemon,
# and let the adults solve this serious reverse?

# <a href="/static/reverse3">Have fun</a>

# """,
# "flag": 'poke{Up_4nD_d0WN_it_go3$}'
# })

declare_chal({ "name": "Pureblood",
    "category": "reverse",
    "score": 300,
    "info": """

Listen, why don't you go watch some pokemon,
and let the adults solve this serious reverse?

<a href="/static/pureblood.tar">Have fun</a>

""",
"flag": 'poke{0h_tH3_pur1tY!}'
})


