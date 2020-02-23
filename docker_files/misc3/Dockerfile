FROM ubuntu:latest
RUN apt update
RUN apt install -y python socat
RUN useradd -m poke
COPY pokectf/interactive_challs/falling-down.py /home/poke/falling-down.py
CMD su poke /bin/bash -c "socat tcp-listen:5008,reuseaddr,fork exec:'/home/poke/falling-down.py'"

