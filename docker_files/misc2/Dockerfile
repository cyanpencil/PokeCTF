FROM ubuntu:latest
RUN apt update
RUN apt install -y socat frotz
RUN useradd -m poke
COPY pokectf/interactive_challs/zork1.z3 /home/poke/zork1.z3
EXPOSE 5003
CMD su poke /bin/bash -c "socat tcp-listen:5003,reuseaddr,fork exec:'frotz /home/poke/zork1.z3'"
