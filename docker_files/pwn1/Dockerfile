FROM ubuntu:latest
RUN dpkg --add-architecture i386
RUN apt update
RUN apt install -y socat libc6:i386 libncurses5:i386 libstdc++6:i386
RUN useradd -m poke
COPY pokectf/static/pwn1 /home/poke/pwn1
RUN echo "poke{w3ll..g0Od_j0b_I_gu35s}" > /home/poke/flag
RUN chown poke -R /home/poke
RUN chmod -w -R /home/poke
EXPOSE 5006
CMD su poke /bin/bash -c "cd;socat tcp-listen:5006,reuseaddr,fork exec:'/home/poke/pwn1'"
