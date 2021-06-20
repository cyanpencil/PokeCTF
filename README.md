# PokeCTF
A quick-and-easy CTF framework for people who love ASCII and minimalism.

Here's a screenshot:

![cool ascii](https://www.github.com/cyanpencil/PokeCTF/raw/master/screen.png)


You can try a live version [here](http://pokectf.cyanpencil.xyz)

No javascript required.

---

# setup
`pip install -r pokectf/requirements.txt`. You also need [aha](https://github.com/theZiz/aha) to generate ANSI art.

PokeCTF uses a docker container for the web server, and a docker container for each interactive challenge that must be hosted on the server.

Edit and run `deploy.sh` to spawn all the docker containers and run the CTF. 

Define your set of challenges and flags in `pokectf/challs.py`

# Ansi art 
Each time a random pokemon from the first 40 of the first collection will be served in ANSI art. 

ANSI art images were generate with [ansize](https://www.github.com/jhchen/ansize) and then converted to HTML with [aha](https://github.com/theZiz/aha). 

You can generate your own images by placing them in `pokectf/pokemon_sprites/pokemon/[0..40].png` and running `pokectf/generate_pokemon_ascii.sh`. They will be placed in `pokemon/banners/poke[0..40].html` and served at random.

# Credits
This project was heavily inspired from @andreafioraldi's [ascii-ctf](https://github.com/andreafioraldi/ascii-ctf). 

Pokemon sprites from: https://www.kaggle.com/kvpratama/pokemon-images-dataset

Blurry text hack from: http://www.briankhuu.com/blog/self/2015/01/14/css-style-for-ascii-art.html

ASCII banner generator: http://www.network-science.de/ascii/
