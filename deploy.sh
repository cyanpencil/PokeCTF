#!/bin/bash

cd $(dirname $0)

[[ $(sudo docker ps -q | wc -l) -ge 1 ]] && sudo docker stop $(sudo docker ps -q)

dbmount="$(pwd)/pokectf:/home/poke/pokectf"

# webserver
sudo docker build --file=./docker_files/main/Dockerfile -t pokectf:latest .
sudo docker run -v $dbmount -d -p 5000:5000 -it pokectf


# challenges
sudo docker build --file=./docker_files/pwn2/Dockerfile -t pokectf_pwn2:latest .
sudo docker run -d -p 5001:5001 -it pokectf_pwn2

sudo docker build --file=./docker_files/misc1/Dockerfile -t pokectf_misc1:latest .
sudo docker run -d -p 5002:5002 -it pokectf_misc1

sudo docker build --file=./docker_files/misc2/Dockerfile -t pokectf_misc2:latest .
sudo docker run -d -p 5003:5003 -it pokectf_misc2

sudo docker build --file=./docker_files/web1/Dockerfile -t pokectf_web1:latest .
sudo docker run -d -p 5004:5004 -it pokectf_web1

sudo docker build --file=./docker_files/web2/Dockerfile -t pokectf_web2:latest .
sudo docker run -d -p 5005:5005 -it pokectf_web2

sudo docker build --file=./docker_files/pwn1/Dockerfile -t pokectf_pwn1:latest .
sudo docker run -d -p 5006:5006 -it pokectf_pwn1

sudo docker build --file=./docker_files/crypto1/Dockerfile -t pokectf_crypto1:latest .
sudo docker run -d -p 5007:5007 -it pokectf_crypto1

sudo docker build --file=./docker_files/misc3/Dockerfile -t pokectf_misc3:latest .
sudo docker run -d -p 5008:5008 -it pokectf_misc3

sudo docker build --file=./docker_files/pwn3/Dockerfile -t pokectf_pwn3:latest .
sudo docker run -d -p 5009:5009 -it pokectf_pwn3

sudo docker build --file=./docker_files/gameboy/Dockerfile -t pokectf_gameboy:latest .
sudo docker run -d -p 1989:1989 -it gameboy
