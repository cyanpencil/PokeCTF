#! /bin/bash

set -ex

# Let's change to the directory where this script is
cd "$(dirname "$0")"

chars=("F" "01" "M")
chars_len=${#chars[@]}

for mode in `seq 0 $(( chars_len - 1 ))`; do
	echo $mode
	sed  "23s/\".*\"/\"${chars[$mode - 1]}\"/" -i ansize/ansize.go 
	go build -o ansize/ansize ansize/ansize.go 
	for no in {1..40}; do
		ansize/ansize pokemon_sprites/pokemon/${no}.png /tmp/ascii 80
		cat /tmp/ascii | aha -w -n -l > templates/banners/poke${no}_${mode}.html
	done
done
